import json

from classes.RedditApi import redditApi
from classes.post import Post
from classes.speech import Speech

from utils.log import log, LogType

from text_to_speak.default_text_to_speak import default_text_to_speak

class PostController:
    @staticmethod
    def get_single_post(subreddit: str = 'askReddit'):
        res = {}
        posts = redditApi.get_subreddit_hot_posts(subreddit)
        
        choosen_post: Post = posts[0]
        choosen_post.set_replies_by_dict(redditApi.get_post_replies(choosen_post))
        choosen_reply: RedditArticle = choosen_post.replies[0]
        
        post_speech_text = f'{choosen_post.title}. {choosen_post.content}'

        speech_type = Speech.get_speech_type([post_speech_text, choosen_reply.content])
        log(LogType.INFO, f"Speech Type: {speech_type}")

        post_speech = Speech(post_speech_text, choosen_post.id, speech_type)
        reply_speech = Speech(choosen_reply.content, choosen_reply.id, speech_type)
      
        res['post'] = choosen_post.toJson()
        res['post']['speech'] = post_speech.toJson()
        res['reply'] = choosen_reply.toJson()
        res['reply']['speech'] = reply_speech.toJson()
        log(LogType.INFO, f"FINISHED REQUEST")
        return json.dumps(res)
    
        
        
        