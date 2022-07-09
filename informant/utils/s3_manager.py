from os import getenv
import boto3
from dotenv import load_dotenv

load_dotenv()

class _S3Manager:
    """Can Upload or delete file from S3"""
    bucket_name: str = 'auto-reddit-data'
    region: str = 'us-east-2'
    last_file_path:str
    def __init__(self):
        print("Creating S3 manager")
        access_key = getenv("AWS_ACCESS_KEY")
        secret_key = getenv("AWS_SECRET_KEY")
        password = getenv("AWS_PASSWORD")

        self.session = boto3.Session(
            region_name= self.region,
            aws_access_key_id= access_key,
            aws_secret_access_key= secret_key,
        )
        
        self.resource = self.session.resource('s3')
        self.bucket = self.resource.Bucket(self.bucket_name)
        print("S3 manager created!")

    def upload(self, file_origin: str, file_name: str):
        """Uploads a file to AWS S3
        :param: file_origin - where the file come from, file path or url
        :param: file_name - where the file will be located and its name. doesn't need './'"""
        already_exists = self.check_if_file_exists(file_name)
        if already_exists:
            print("File already uploaded")
            return
        
        result = self.bucket.upload_file(file_origin, file_name)
        self.last_file_path = file_name
        return file_name
    
    def check_if_file_exists(self, file_to_search: str):
        for file in self.bucket.objects.all():
            if file.key == file_to_search:
                return True
        return False
        
    def delete(self,file_path):
        """Delets a file from AWS S3,
        :param: folder and file name where its located. Doesn't need './' """
        result = self.resource.Object(self.bucket_name, file_path).delete()
        print(result)
        
    def get_last_uploaded_file_url(self, file_path: str = None):
        if file_path is None:
            file_path = self.last_file_path
        already_exists = self.check_if_file_exists(file_path)
        if already_exists:
            print("File already uploaded")
            return

        return f"https://{self.bucket_name}.s3.{self.region}.amazonaws.com/{self.last_file_path}"
        
    def ping(self):
        return "pong"
    
S3Manager = _S3Manager()
