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
