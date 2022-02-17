#!/usr/bin/python3

from ast import Raise
import json
import logging
import math

from numpy import average


DECAY_FACTOR = 0.02
TURBIDITY_THRESH = 1.0

def calc_turbidity(water_samples: list, num_samples:int = 5) -> float:
    '''
    Calculates the turbidity of the water using the average of the num_samples most recent data collects and the equation:
        T = a0 * I90.
    Where 
        T = Turbidity in NTU Units 
        a0 = Calibration constant
        I90 = Ninety degree detector current

    Args: 
        water_samples (list): The most recent data collection of water samples (from turbidity_data.json).
        num_samples (int): number of samples to be used when calculating the turbidity.

    Returns:
        T (float): Turbidity in NTU Units
    '''
    # Note: While the data in turbidity_data.json appears to be sorted in order of time, I am not making the 
    # assumption that this will always be the case. If this is always the case, there would be no need to sort.

    if len(water_samples) == 0:
        raise ValueError('Water sample list is empty')

    # sorts the water data by time
    # note: datetime parsing is not necessary due to how the string is formated, otherwise this could be used
    #   in the lambda function: datetime.strptime(data_collect['datetime'], "%Y-%m-%d %H:%M")
    water_sorted_time = sorted(water_samples, key=lambda data_collect: data_collect['datetime'], reverse = True)
    water_recent = water_sorted_time[0:num_samples+1]

    sampleTs = [sample['calibration_constant']*sample['detector_current'] for sample in water_recent]
    T = sum(sampleTs)/num_samples
    
    return T
    

def calc_time_water_safe(T0: float) -> float:
    '''
    Calculates minimum time to fall below threshold turbidity using
        Ts > T0(1-d)**b     <=>    log(Ts/T0)/log(1-d) = b    
    Where
        Ts = Turbidity threshold for safe water
        T0 = Current turbidity
        d = decay factor per hour, expressed as a decimal
        b = hours elapsed

    Args:
        T0 (float): Current turbidity

    Returns: 
        (float) hours elapsed
    '''
    if T0 < TURBIDITY_THRESH:
        b = 0.0
    else:
        b = math.log(TURBIDITY_THRESH/T0, (1 - DECAY_FACTOR))
    return b

def main():
    logging.basicConfig(level=logging.INFO)
    
    # Get water samples
    with open("turbidity_data.json", "r") as f:
        water_samples = json.load(f)

    # Calculate important values
    T = calc_turbidity(water_samples['turbidity_data'])
    hours_until_water_safe = calc_time_water_safe(T)

    # Log important info
    print(f'Average turbidity based on most recent five measurements = {T} NTU')
    if T >= TURBIDITY_THRESH:
        logging.warning('Turbidity is above threshold for safe use')
    else:
        logging.info('Turbidity is below threshold for safe use')
    print(f'Minimum time required to return below a safe threshold = {hours_until_water_safe} hours')
    

if __name__ == "__main__":
    main()
