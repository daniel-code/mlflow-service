"""
This script shows how to log metric and artifacts to mlflow.
The environment variables
- MLFLOW_TRACKING_INSECURE_TLS: If true, the mlflow client will not verify TLS certificates since we are running in self-signed certificates.
- MLFLOW_ENABLE_SYSTEM_METRICS_LOGGING: If true, the mlflow client will log system metrics to mlflow.
- MLFLOW_TRACKING_USERNAME: The mlflow client username
- MLFLOW_TRACKING_PASSWORD: The mlflow client password

Please reference https://www.mlflow.org/docs/latest/auth/index.html#authenticating-to-mlflow for more authenticating information.
"""

import random
import string
import time

from dotenv import load_dotenv

import mlflow
import os

# load MLFLOW_S3_ENDPOINT_URL, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
load_dotenv()

os.environ["MLFLOW_TRACKING_INSECURE_TLS"] = "true"
os.environ["MLFLOW_ENABLE_SYSTEM_METRICS_LOGGING"] = "true"


def random_string(k=10):
    return "".join(random.choices(string.ascii_letters, k=k))


if __name__ == "__main__":
    mlflow.set_tracking_uri("https://localhost:5000/")
    mlflow.set_experiment("Default")
    with mlflow.start_run() as run:
        run_id = run.info.run_id
        for i in range(10):
            # upload metric to mlflow
            mlflow.log_metric("accuracy", random.random())

        with open("artifact.txt", "w") as f:
            f.write(random_string())
        # upload artifact to mlflow
        mlflow.log_artifact("artifact.txt")
        time.sleep(15)  # make run time longer than first system metric log

    # Users who had read privilege could download artifacts.
    mlflow.artifacts.download_artifacts(
        run_id=run_id,
        artifact_path="artifact.txt",
        dst_path="test",
    )
