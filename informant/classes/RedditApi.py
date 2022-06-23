from ctypes import Array
from typing import Dict
from requests import Response, get, post, auth as request_auth
from os import getenv
from dotenv import load_dotenv

from classes.post import Post

USERNAME = 'auto-reddit-video'
DEFAULT_REDDIT_URL = 'https://oauth.reddit.com'

class RedditApi:
    def __init__(self):
        load_dotenv()
        self.__REDDIT_SECRET = getenv('REDDIT_SECRET')
        self.__REDDIT_CLIENT_KEY = getenv('REDDIT_CLIENT_KEY')
        self.__REDDIT_PASSWORD = getenv('REDDIT_PASSWORD')
        self.__headers = {'User-Agent': 'auto-video/0.0.1'}
        self.__token = ''
        self.__token = self._get_access_token()
        self.__headers['Authorization'] = f'bearer {self.__token}'

    def _get_access_token(self): 
        auth = request_auth.HTTPBasicAuth(self.__REDDIT_CLIENT_KEY, self.__REDDIT_SECRET)
        data = {
            'grant_type': 'password',
            'username': USERNAME,
            'password': self.__REDDIT_PASSWORD
        }

        res = post("https://www.reddit.com/api/v1/access_token", auth=auth, data=data,
                   headers=self.__headers)
        
        if res.json().get('access_token') is None:
            raise Exception('Access Token Dennied or None')
        
        return res.json()['access_token']

    def get_subreddit_hot_posts(self, subreddit: str):
        postsResponse = self.request_reddit_api(f'/r/{subreddit}/hot')
        postsData: Array[Post] = Post.create_posts_from_response(postsResponse)
        return postsData
    
    def request_reddit_api(self, path: str) -> Dict:
        requested_url = f'{DEFAULT_REDDIT_URL}{path}'
        print(f"[REQUEST] path: {path}")
       
        response: dict = get(requested_url, headers=self.__headers, params={'limit': '10'}).json()

        if type(response) is list: #is a reply data
            response = response[1]
        if response.get('data') is None:
            raise Exception(f'request faild on path {path}. \
                            response: {str(response)}')
        return response

    def get_post_replies(self, post: Post) -> Array:
        path = f'/{post.subreddit}/comments/{post.id}/{post.url_posfix}'
        replies = self.request_reddit_api(path).get('data').get('children')
        
        if len(replies) == 0:
            raise Exception(f"This post Doesnt have replies \n path: {path}")
        
        return replies

    


redditApi = RedditApi()