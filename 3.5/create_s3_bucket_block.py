from time import sleep
from prefect_aws import S3Bucket, AwsCredentials
import dotenv
import os

dotenv.load_dotenv("./.env")

aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")


AWS_CREDENTIALS_NAME = "aws-credentials"

def create_aws_creds_block():
    my_aws_creds_obj = AwsCredentials(
        aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key
    )
    my_aws_creds_obj.save(name=AWS_CREDENTIALS_NAME, overwrite=True)


def create_s3_bucket_block():
    aws_creds = AwsCredentials.load(AWS_CREDENTIALS_NAME)

    my_s3_bucket_obj = S3Bucket(
        bucket_name="aws-prefect-general-storage", credentials=aws_creds
    )
    my_s3_bucket_obj.save(name="prefect-general-bucket", overwrite=False)


if __name__ == "__main__":
    create_aws_creds_block()
    sleep(5)
    create_s3_bucket_block()
