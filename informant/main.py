from classes.voices import Voice
from controller.get_post_controller import PostController
from text_to_speak.tik_tok_text_to_speak import tik_tok_text_to_speak

from utils.log import log
from classes.RedditApi import redditApi
from classes.speech import Speech

from s3_manager import S3Manager

a = Speech("Testing testing", "./testing.wav")
S3Manager.upload(a.file_path, "test/testing.wav")
print(S3Manager.get_last_uploaded_file_url())
a.delete_generated_file()