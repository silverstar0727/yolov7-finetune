import boto3
s3 = boto3.resource('s3') 

def download_s3_folder(s3, bucket_name, s3_folder, local_dir=None):
    bucket = s3.Bucket(bucket_name)
    for obj in bucket.objects.filter(Prefix=s3_folder):
        target = obj.key if local_dir is None \
            else os.path.join(local_dir, os.path.relpath(obj.key, s3_folder))
        if not os.path.exists(os.path.dirname(target)):
            os.makedirs(os.path.dirname(target))
        if obj.key[-1] == '/':
            continue
        bucket.download_file(obj.key, target)

if __name__ == "__main__":
    s3 = boto3.resource('s3') 
    download_s3_folder(s3=s3, bucket_name="jeongmin-mask-detection-test-dataset", s3_folder="images")
    download_s3_folder(s3=s3, bucket_name="jeongmin-mask-detection-test-dataset", s3_folder="annotations")