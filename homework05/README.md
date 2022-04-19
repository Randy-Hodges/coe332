# Sample Redis database with Flask app
This homework is the creation of a flask app that interacts with a redis database. This is a great example of how to use a redis database and containerize a database and flask app.

## Download the original data
Before running or containerizing the app, it is important to download the orignal data and put it in the root folder of the docker container. This data contains the meteorite landings that are being analyzed. The data can be found here:
```
https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
```
and can be dowloaded with 
```
wget --no-check-certificate --content-disposition https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
```
 ### Docker
#### How to pull and use my existing image on Docker Hub:
Run the command 
```
docker pull rhodgesd/redis_app:hw05
```
while having docker installed. You should receive 'hw05: Pulling from rhodgesd/redis_app' and then a success message.
#### How to build an image from the Dockerfile:
Navigate to the directory of the dockerfile and run
```
docker build -t rhodgesd/redis_app:hw05 .
```
Or alternatively, replace the '.' with the path to the dockerfile. If all goes well, the final terminal line should look like 
'Successfully tagged rhodgesd/redis_app:hw05'

## Run the redis database
First pull down one of the existing redis bases. 
```
docker pull redis:6
```
Then run the following command:
```
docker run -d -p 6411:6379 -v $(pwd)/data:/data:rw --name=rhodges-redis redis:6 --save 1 1
```
Breaking down the above command:
docker run | run a docker container
-d | run it in the background
-p 6411:6379 | specify the port to be used
-v $(pwd)/data:/data | mount the container data (/data) to the local directory's data folder ($(pwd)/data)
:rw | mount the data for reading and writing
--name=rhodges-redis | name of the container
redis:6 | docker image to be used for the redis server
--save 1 1 | save the data every (1) seconds (the first 1) and have (1) backups (the second 1)
## Build an run the containerized flask app
Run the following commands while in the directory of the dockerfile:
```
 docker build -t rhodgesd/redis_app:hw05 .
 docker run -d -p 5011:5000 rhodgesd/redis_app:hw05
 ```
The app should now be running.
## Interact with the app
The app currently supports to routes, a GET and a POST for /data:
```
curl localhost:5011/data
curl -X POST localhost:5011/data
```
The GET route will return the data that is stored in the redis database and the post method will update the database.
