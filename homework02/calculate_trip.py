#!/usr/bin/env python3

import json
import math

class Robot:
    def __init__(self, latitude, longitude, speed):
        self.longitude = longitude
        self.latitude = latitude
        self.speed = speed
        self.site_name = 'initial'


def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    '''Calculates the distance between two points on mars in km'''
    mars_radius = 3389.5    # km
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )


def run_robot_trip(sites: dict)-> None:
    '''Calculates a robot trip on mars given a list of sites'''
    sample_times = {
        "stony": 1.0,
        "iron": 2.0,
        "stony-iron": 3.0
    }
    total_time = 0
    site_count = 0
    # Side note - using a robot class isn't really required here. It just feels natural to me.
    robot = Robot(latitude = 16.0, longitude = 82.0, speed = 10)

    for landing_site in sites["sites"]:
        # Calculate time to move and sample meteorite
        print(f'{robot.site_name} -> site {landing_site["site id"]} | ', end='')
        dist_to_next_site = calc_gcd(robot.latitude, robot.longitude, landing_site["latitude"], landing_site["longitude"])
        travel_time = dist_to_next_site/robot.speed
        sample_time = sample_times[landing_site["composition"]] # selects the sample time based on the meteorite composition
        total_leg_time = travel_time + sample_time
        total_time += total_leg_time

        # Print results
        print(f'Travel time: {travel_time: .2f} hrs, Sample time: {sample_time: .2f} hrs, Section time: {total_leg_time: .2f} hrs')

        # Set Robot's new data to the old site
        robot.latitude = landing_site['latitude']
        robot.longitude = landing_site['longitude']
        robot.site_name = f'site {landing_site["site id"]}'
        
        site_count += 1

    print("==========================")
    print(f'Number of sites visited: {site_count}, Total time elapsed: {total_time: .2f} hours')
    return


def main():
    # Get landing site data
    with open("landing_sites.json", "r") as f:
        sites = json.load(f)
    # Run simulation of robot exploring landing site data (results outputted to console)
    run_robot_trip(sites)

if __name__ == "__main__":
    main()

    
    

