import json
from classes.RedditApi import RedditApi
from classes.post import Post
from text_to_speak.tik_tok_text_to_speak import text_to_speak


class PostController:
    def get_single_post(subreddit: str):
        res = {}
        redditApi = RedditApi()
        posts = redditApi.get_subreddit_hot_posts(subreddit)
        
        choosenPost: Post = posts[0]
        res['post'] = choosenPost.toJson()
        res['title_speach_path'] = text_to_speak(choosenPost.title, filename=f'../audios/{choosenPost.get_id()}.mp3')
        # res['content_speach_path'] = text_to_speak(choosenPost.title, filename=f'./audios/{choosenPost.get_id()}.mp3')
        
        return json.dumps(res)