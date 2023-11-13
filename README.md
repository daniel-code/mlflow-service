# mlflow-service

Launch mlflow service via docker

using remote artifacts, [MinIO](https://min.io/)

## Setup

1. modify .env from .env.example

   ```dotenv
    # postgres
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_DB=mlflow
    
    # mlflow
    BUCKET_NAME=mlflow
    
    # MinIO
    MINIO_ROOT_USER=
    MINIO_ROOT_PASSWORD=
    MINIO_VOLUMES=/mnt/data
    
    # project
    MLFLOW_S3_ENDPOINT_URL=http://localhost:9000
    ## usually same as `MINIO_ROOT_USER` and `MINIO_ROOT_PASSWORD`
    AWS_ACCESS_KEY_ID=
    AWS_SECRET_ACCESS_KEY=
   ```

2. Launch Service
   ```commandline
   docker-compose up -d
   ```
3. Create `mlflow` Bucket on MinIO
    1. GUI
       ![creat_bucket.png](asstes%2Fcreat_bucket.png)
    2. CLI
       ```commandline
       docker exec -d minio mkdir /mnt/data/mlflow
       ```
4. Create Assess Keys or Users of MinIO
   ![creat_access_key.png](asstes%2Fcreat_access_key.png)
5. Add Environment Variables
   add the following environment variables to your application.

   ```dotenv
   # project
   MLFLOW_S3_ENDPOINT_URL=http://localhost:9000
   ## usually same as `MINIO_ROOT_USER` and `MINIO_ROOT_PASSWORD`
   AWS_ACCESS_KEY_ID=
   AWS_SECRET_ACCESS_KEY=
   ```
6. Log to mlflow [log_metric.py](log_metric.py)
