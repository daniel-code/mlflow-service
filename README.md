# mlflow-service

Launch mlflow service via docker

using local file system as the artifacts of mlflow 

## Setup

1. modify .env
```dotenv
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_DATABASE=mlflow
```
2. launch mlflow
   1. docker-compose
   ```commandline
   docker-compose up -d
   ``` 
   2. local
   ````commandline
   mlflow server --backend-store-uri mysql+pymysql://${MYSQL_USER}:${MYSQL_PASSWORD}@db:3306/${MYSQL_DATABASE} --default-artifact-root . --host 0.0.0.0
   ````
   