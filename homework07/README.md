# Final Project Diagram
This homework folder only contains one image. This image is a diagram which explains an aspect of the final project for coe332. The diagram consists of a large bubble (the kubernetes namespace, representing everything that will be deployed to kubernetes) which encapsulates many smaller bubbles. These smaller bubbles represent the different deployments that will exist in kubernetes for the final project. Each deployment has a name and might contain additional tags. The tag "PVC" stands for persistent volume claim and means that a specific deployment will request more storage space from kubernetes. The tag "service" means that a particular deployment will have a service also deployed for it. The service will make it so that we can easily access a particular type of deployment, regardless of how many copies of that deployment there might be in the kubernetes system. 

In this diagram there are workers, flask APIs, Redis databases, and a UI. Beginning with the Redis database, any deployment with the name "redis" in it means that that deployment will focus on the utilization of a redis database. If the deployment contains "jobs" in the name, it will focus on handling the computation of different analysis jobs that are submitted to the system. If the deployment name conatins "flask" in it, it will focus on the RESTFUL API tasks for the project and will act as the front end for the project. The flask API is what will submit jobs to the job deployments. Lastly there is the UI deployment, which will contain a user interface for users of the system.







Link to final project: https://github.com/Randy-Hodges/coe332-Final-Project
