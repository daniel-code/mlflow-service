# mlflow-service

Launch mlflow service via docker

using remote artifacts, [MinIO](https://min.io/)

## Setup

1. modify .env

   ```dotenv
   MYSQL_USER=
   MYSQL_PASSWORD=
   MYSQL_DATABASE=mlflow
   
   # MinIO
   MINIO_ROOT_USER=
   MINIO_ROOT_PASSWORD=
   MINIO_VOLUMES="/mnt/data"
   ```

2. Launch Service
   ```commandline
   docker-compose up -d
   ```
3. Create Buckets in MinIO
   ![creat_bucket.png](asstes%2Fcreat_bucket.png)
4. Create Assess Keys or Users of MinIO
   ![creat_access_key.png](asstes%2Fcreat_access_key.png)
5. Add Environment Variables
   add the following environment variables to your application.

   ```dotenv
   # mlflow
   MLFLOW_S3_ENDPOINT_URL=http://localhost:9000
   AWS_ACCESS_KEY_ID=
   AWS_SECRET_ACCESS_KEY=
   ```
6. Log to mlflow

   ```python
   import random
   import string
   
   from dotenv import load_dotenv
   
   import mlflow
   
   # load MLFLOW_S3_ENDPOINT_URL, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
   load_dotenv()
   
   
   def random_string(k=10):
       return ''.join(random.choices(string.ascii_letters, k=k))
   
   
   if __name__ == '__main__':
       mlflow.set_tracking_uri('http://localhost:5000/')
       mlflow.set_experiment('test')
       with mlflow.start_run() as run:
           print(run.info.run_id)
           for i in range(10):
               mlflow.log_metric('accuracy', random.random())
   
           with open('artifact.txt', 'w') as f:
               f.write(random_string())
   
           mlflow.log_artifact('artifact.txt')
   
   ```
