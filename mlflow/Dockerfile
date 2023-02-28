FROM python:3.8-slim-buster

WORKDIR /mlflow

COPY requirements.txt .
# Install python packages
RUN python -m pip install --upgrade pip  \
    && pip install -r requirements.txt

EXPOSE 5000
CMD mlflow server --backend-store-uri mysql+pymysql://${MYSQL_USER}:${MYSQL_PASSWORD}@db:3306/${MYSQL_DATABASE} --default-artifact-root s3://mlflow --host 0.0.0.0
