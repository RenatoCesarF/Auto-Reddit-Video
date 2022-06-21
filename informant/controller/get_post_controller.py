import json

from classes.RedditApi import redditApi
from classes.post import Post
from classes.speech import Speech

from text_to_speak.default_text_to_speak import default_text_to_speak

class PostController:
    @staticmethod
    def get_single_post(subreddit: str = 'askReddit'):
        res = {}
        posts = redditApi.get_subreddit_hot_posts(subreddit)
        
        choosen_post: Post = posts[0]
        choosen_post.set_replies_by_dict(redditApi.get_post_replies(choosen_post))
        #if speech text is bigger than 200 chars. set type os speech to default elsse, set to tik tok
        post_speech = Speech(f'{choosen_post.title}. {choosen_post.content}',
                             choosen_post.id)
        
        choosen_reply: RedditArticle = choosen_post.replies[0]
        reply_speech = Speech(choosen_reply.content, choosen_reply.id)
      
        res['post'] = choosen_post.toJson()
        res['post']['speech'] = post_speech.toJson()
        res['reply'] = choosen_reply.toJson()
        res['reply']['speech'] = reply_speech.toJson()
        print(f"[FINISH] (lenght {post_speech.lenght_in_seconds})")
        return json.dumps(res)
    
        
        
        