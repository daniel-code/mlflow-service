FROM python:3.8-slim-buster

WORKDIR /mlflow

COPY requirements.txt .
# Install python packages
RUN python -m pip install --upgrade pip  \
    && pip install -r requirements.txt

EXPOSE 5000
CMD mlflow server --backend-store-uri mysql+pymysql://${MARIADB_USER}:${MARIADB_PASSWORD}@db:3306/${MARIADB_DATABASE} --default-artifact-root s3://${BUCKET_NAME} --host 0.0.0.0
