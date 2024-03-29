import json

from classes.RedditApi import redditApi
from classes.post import Post
from classes.speech import Speech
from classes.redditArticle import RedditArticle
from classes.s3_manager import S3Manager
from utils.log import log

from text_to_speak.default_text_to_speak import default_text_to_speak

class PostController:
    @staticmethod
    def get_single_post(subreddit: str = 'askReddit'):
        res = {}
        posts = redditApi.get_subreddit_hot_posts(subreddit)

        choosen_post: Post = posts[0]
        choosen_post.subreddit_img = redditApi.get_subreddit_img(subreddit)
        choosen_post.set_replies_by_dict(redditApi.get_post_replies(choosen_post))
        post_speech_text = f'{choosen_post.title}. {choosen_post.content}'
        
        choosen_reply: RedditArticle = choosen_post.replies[0]
        choosen_reply.author_img = redditApi.get_user_avatar(choosen_reply.author)

        speech_type = Speech.get_speech_type([post_speech_text, choosen_reply.content])
        log.info(f"Speech Type: {speech_type}")

        post_speech = Speech(post_speech_text, f"{choosen_post.id}.mp3", speech_type)
        reply_speech = Speech(choosen_reply.content, f"{choosen_reply.id}.mp3", speech_type)
        
        post_speech.file_path = post_speech.upload_speech(choosen_post.id, "post")
        reply_speech.file_path = reply_speech.upload_speech(choosen_post.id, choosen_reply.id)

        res['post'] = choosen_post.to_json()
        res['post']['speech'] = post_speech.to_json()
        res['reply'] = choosen_reply.to_json()
        res['reply']['speech'] = reply_speech.to_json()
        log.info(f"FINISHED REQUEST")
        return res
    
