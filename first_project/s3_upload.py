import os
import boto3


AWS_ACCESS_KEY_ID = 'AKIA6GBMFKS6T7ZPN5NR'
AWS_SECRET_ACCESS_KEY = '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'
AWS_REGION_NAME = 'eu-north-1'
S3_BUCKET_NAME = 'indus-django'


def upload_image_to_s3(file_path, s3_key):
    s3 = boto3.client('s3',
                      aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                      region_name=AWS_REGION_NAME)
    try:
        s3.upload_file(file_path, S3_BUCKET_NAME, s3_key)
        print(f"Uploaded {file_path} to S3 bucket.")
    except Exception as e:
        print(f"Error uploading {file_path} to S3 bucket: {e}")


MEDIA_ROOT = r'F:\code\Django-Project\first_project\media'

for root, dirs, files in os.walk(MEDIA_ROOT):
    for file in files:
        if file.endswith(('jpg', 'jpeg', 'png', 'gif')):
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, MEDIA_ROOT)
            s3_key = f"media/{relative_path}"
            upload_image_to_s3(file_path, s3_key)
