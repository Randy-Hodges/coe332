# Robotic Investigation of 5 Meteor Sites in Syrtis Major

## Overview
The files for this homework represent a simulation of a robot exploring meteorite landing sites in the Syrtis Major crater located on mars. This project is a great example of how to create a JSON file with one script and then use that JSON file in another. 

## File Descriptions
generate_sites.py:
This file randomly generates five landing sites in the crater and also includes a random meteorite composition for each site. The output from running this file is a JSON file (landing_sites.json) which contains the data of each site.

calculate_trip.py:
This file simulates a robot traveling to each randomly generated site from landing_sites.json. It calculates the time spent during each leg of the trip using latitude and longitude values, the radius of mars, a robot speed of 10km/hour, and factors in meterite composition.

## Running the code
First generate_sites.py should be run by using the command 

'''
python3 generate_sites.py
'''

or by simply running generate_sites.py as an executable.

After that, calculate_trip.py should be executed using 

'''
python3 calculate_trip.py
'''

or by running calculate_trip.py as an executable.
The results of the simulation will be shown in the terminal.

If you are lazy like I am and don't want to type all of that, you could also run a bash script that I made that runs both of the above commands

```
./run_robot.sh
```

When looking at the results, each leg of the trip should be under 16 hours (that is about how long it would take the robot to cross the entire diameter of the crater). The results of the output will show an example exploration of a mars rover for each leg in it's 5 leg journey of exploring meteorite sites.