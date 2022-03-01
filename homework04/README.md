# Containerization with meteorite landing data analysis
This project aims to refactor some existing code (using best practices) that analyzes meteorite landing data and aims to containerize all of the files used to analyze the data. This homework is a great example of how to use containerization tools such as Docker to containerize a project. 

## Scripts
#### ml_data_analysis.py
Takes in a data set via a command line entry and uses it to analyze aspects such as the average mass of a meteorite and location of meteorites.

#### test_ml_data_analysis.py
This file contains unit tests for the functions in test_ml_data_analysis.py.

#### Dockerfile
Used to create the docker image.

## How to run and interpret the code
### Basics
Having access to the files in the repo, you can simply run
```
python3 ml_data_analysis.py [Json file name] 
```
In order to see the output from the program. 
Here is a sample output:
```
Summary data following meteorite analysis: 

Average Mass of 30 meteor(s): 
 83857.3

Hemisphere summary data:
There were 21 meteors found in the Northern & Eastern quadrant
There were 6 meteors found in the Northern & Western quadrant
There were 3 meteors found in the Southern & Western quadrant
There were 0 meteors found in the Southern & Eastern quadrant

Class summary data:
The L5 class was found 1 time(s)
The H6 class was found 1 time(s)
The EH4 class was found 2 time(s)
The Acapulcoite class was found 1 time(s)
The L6 class was found 6 time(s)
The LL3-6 class was found 1 time(s)
The H5 class was found 3 time(s)
The L class was found 2 time(s)
```

### Dataset
A great sample data set can be found here: https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
One can retrieve this by running the command
```
wget --no-check-certificate --content-disposition https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
```
The input data to ml_data_analysis.py is expected to be a JSON file which has one key which contains a list of dictionaries. One of the fastest ways to learn the format is through seeing it. Here is an example:
```
{
  "meteorite_landings": [
    {
      "name": "Ruiz",
      "id": "10001",
      "recclass": "L5",
      "mass (g)": "21",
      "reclat": "50.775",
      "reclong": "6.08333",
      "GeoLocation": "(50.775, 6.08333)"
    },
    {
      "name": "Beeler",
      "id": "10002",
      "recclass": "H6",
      "mass (g)": "720",
      "reclat": "56.18333",
      "reclong": "10.23333",
      "GeoLocation": "(56.18333, 10.23333)"
    }
  ]
}
```
### Docker
#### How to pull and use my existing image on Docker Hub:
Run the command 
```
docker pull rhodgesd/ml_data_analysis:hw04
```
while having docker installed. You should receive 'hw04: Pulling from rhodgesd/ml_data_analysis' and then a success message.
#### How to build an image from the Dockerfile:
Navigate to the directory of the dockerfile and run
```
docker build -t rhodgesd/ml_data_analysis:hw04 .
```
Or alternatively, replace the '.' with the path to the dockerfile. If all goes well, the final terminal line should look like 
'Successfully tagged rhodgesd/ml_data_analysis:hw04'

#### Run the containerized code against the sample data inside the container
You can use the following commands to run the code on the sample data set.
```
docker run --rm -it rhodgesd/ml_data_analysis:hw04
cd code
ml_data_analysis.py Meteorite_Landings.json 
```
This should have output similar to what is shown under 'Basics'.

#### Run the containerized code against user-provided data that they may have found on the web
To run your own data against the file in the container, mount your data into the container when running it through
```
docker run --rm -it -v [PATH TO DATA]:/code rhodgesd/ml_data_analysis:hw04
```
'PATH TO DATA' can either be the path to your data, or it can be '$PWD' if you have already navigated to the directory where the data is located. 
Then you will follow the same steps as when running the sample data, except with your data as an argument.
```
docker run --rm -it rhodgesd/ml_data_analysis:hw04
cd code
ml_data_analysis.py [YOUR DATA FILE NAME]
```
The output of the code should have output similar to what is shown under 'Basics'.

#### Run the containerized test suite with pytest
```
docker run --rm -it rhodgesd/ml_data_analysis:hw04
cd code
pytest
```
This will output the results of the unit tests to the screen. It should look like the following:
```
==================================================================== test session starts =====================================================================
platform linux -- Python 3.6.8, pytest-7.0.0, pluggy-1.0.0
rootdir: /code
collected 4 items                                                                                                                                            

test_ml_data_analysis.py ....                                                                                                                          [100%]

===================================================================== 4 passed in 0.03s ======================================================================
```


docker run --rm -it rhodgesd/ml_data_analysis:hw04 /bin/bash

docker run --rm rhodgesd/ml_data_analysis:hw04 ml_data_analysis.py Meteorite_Landings.json 

