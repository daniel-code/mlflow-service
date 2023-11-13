FROM python:3.8

WORKDIR /mlflow

COPY requirements.txt .
# Install python packages
RUN python -m pip install --upgrade pip  \
    && pip install -r requirements.txt

EXPOSE 5000
