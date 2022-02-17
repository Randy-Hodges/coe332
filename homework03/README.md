# Analyzation of water samples
This project aims to use water sample data to determine if a selection of water is clean and if not, how long one needs to wait until it is clean. This project is a good example of using good documentation, unit testing, and logging.

## Scripts
#### analyze_water.py
Takes in the data set turbidity_data.json and determines if the most recent selections of water are clean. If not, the program uses a decay formula to determine how long needs to be waited until the water is clean. 

#### test_analyze_water.py
This file contains unit tests for the functions in analyze_water.py.

## How to run and interpret the code
First one needs to download the data set, turbidity_data.json, from https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json
One can do this by running the command
```
wget --no-check-certificate --content-disposition https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json
```
while in the homework03 directory.

Once the data exists, one can run the program by using 

```
python3 analyze_water.py
```
The output of this program will inform about the turbidity of the water and how long one needs to wait until the water is clean. Example output:

Average turbidity based on most recent five measurements = 0.44321040000000006 NTU
INFO:root:Turbidity is below threshold for safe use
Minimum time required to return below a safe threshold = 0.0 hours

One can also run unit tests of the program by using the command 'pytest' in the terminal.
