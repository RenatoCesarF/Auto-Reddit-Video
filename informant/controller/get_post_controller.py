import json

from classes.RedditApi import redditApi
from classes.post import Post
from text_to_speak.tik_tok_text_to_speak import text_to_speak

class PostController:
    def get_single_post(subreddit: str):
        res = {}
        posts = redditApi.get_subreddit_hot_posts(subreddit)
        
        choosen_post: Post = posts[0]
        replies = redditApi.get_post_replies(choosen_post)
        
        choosen_post.set_replies(replies)
        
        res['post'] = choosen_post.toJson()
        res['title_speach_path'] = text_to_speak(choosen_post.title, filename=f'../audios/{choosen_post.id}.mp3')
        return json.dumps(res)
    
    def get_post_by_url(subreddit: str, post_id: str, url_posfix: str):
        post = redditApi.get_post_by_url_paramters(subreddit, post_id, url_posfix)
        return post
        
        
        