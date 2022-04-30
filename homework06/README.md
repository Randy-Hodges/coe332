# Deployment of Flask App to Kubernetes
This homework consists of the deployment of the flask app developed in homework 5 into kubernetes. This is a good example of deploying an app and database to kubernetes, as well as using persistent volume claims.

### File Descriptions
- redis_app.py: App from hw05.
- Dockerfile: Builds the docker image.
- rhodges-test-pvc.yml: Creates the persistent volume claim in kubernetes.
- rhodges-test-redis-deployment.yml: Creates a pod to run a redis database. Utilizes the persistent volume claim
- rhodges-test-redis-service.yml: Creates one IP for the redis pods that can be used for accessing the redis database.
- rhodges-test-flask-deployment.yml: Creates multiple pods that run the flask app.
- rhodges-test-flask-service.yml: Creates one IP for the flask pods that someone can use to access the app.


## Deploying to Kubernetes
This assignment was deployed to the class kubernetes service, hosted at coe332-k8s.tacc.cloud. The following instructions include references to coe332-k8s.tacc.cloud, but this can be any location that runs kubernetes. 

### Deployment
#### Copying files
The first step in deploying the service to kubernetes is having the correct files in the kubernetes deployment. There are two main ways to do this. You can either "git clone" this repository or you can scp the files from one location to coe332-k8s.tacc.cloud. I copied the files using 
```
scp rhodges* rhodges@coe332-k8s.tacc.cloud:
scp python-debug.yml rhodges@coe332-k8s.tacc.cloud:
```
#### Deploying in Kubernetes
Once all the files are copied over, all of the pods/services can be created by using the "kubectl apply" command. All files will need to be "applied" and can be done individually or all at once.
For applying individual files, this looks like:
```
kubectl apply -f <filename>
```
For applying all the files:
```
kubectl apply -f <folder path>
```
If you copied over the files using the command in the "copying files" section, all of the files will be in the root directory and \<folder path\> can be replaced with a period ("." without the quotes). You should find a "filename configured" for each yml file in this homework06 folder.

### Useful Kubernetes Tips
Here are some useful tips for navigating the deployment.
Useful commands for viewing contents:
```
kubectl get services
kubectl get pods
kubectl get pods -o wide
```
These commands list services, list all pods, and list all pods with more detail respectively.

The pods exist on a private network. If you want to interact with individual pods, you will need to exec into a python container. Using the name of the python debug container (found through "kubectl get pods"), you can exec into a python container using 
```
kubectl exec -it <pod_name> -- /bin/bash
```
You can check that the redis database is usable by using the following commands (make sure redis is installed. If not, use pip install redis):
```
python
import redis
rd = redis.StrictRedis(host=<redis service IP>, port=6379, db=0) # IP obtained through "kubectl get services"
rd.set(<key>, <value>)
rd.get(<key>)
```






