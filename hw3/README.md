# Homework 3
Created following Python files to capture, forward and save images
Capture.py - to Capture images from USB webcam
forwarder.py - to forward the message to Cloud
imagesaver.py - save image on Object Storage

Following docker files were created for different container instances
Dockerfile.openCV - OpenCV container to capture the images from USB webcam
Dockerfile.mosquitto - Mosquitto Broker container on Jetson
Dockerfile.forwarder - Message forwardercontainer on Jetson to forward messages to Cloud
Dockerfile.broker - Mosquitto broker container on the cloud
Dockerfile.imagesaver - Container on the cloud to save images to Object Storage

URL for Object Storage where image was saved (sent only one image instead of multiple images)
https://cloud.ibm.com/objectstorage/crn%3Av1%3Abluemix%3Apublic%3Acloud-object-storage%3Aglobal%3Aa%2F74ee9121a3ea44418e566179df80a228%3A306f87f4-ee08-40a4-a67b-086d133d0ae8%3A%3A?bucket=p100-os-bucket1&bucketRegion=us-east&endpoint=s3.us-east.cloud-object-storage.appdomain.cloud&paneId=bucket_overview<br>
cos://us-east/p100-os-bucket1/myimage.jpg

Git Repository
https://github.com/jayeshparikh/w251/tree/master/hw3
