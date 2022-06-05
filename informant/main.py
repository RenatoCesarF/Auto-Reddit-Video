from ast import List
from ctypes import Array
from typing import Dict
import requests
from os import getenv
from dotenv import load_dotenv

from post import Post

load_dotenv()
REDDIT_SECRET = getenv('REDDIT_SECRET')
REDDIT_CLIENT_KEY = getenv('REDDIT_CLIENT_KEY')
REDDIT_PASSWORD = getenv('REDDIT_PASSWORD')

DEFAULT_REDDIT_URL = 'https://oauth.reddit.com'
USERNAME = 'auto-reddit-video'

headers = {'User-Agent': 'auto-video/0.0.1'}
token = ""

def main():
    token = get_access_token()
    headers['Authorization'] = f'bearer {token}'

    postsResponse = request_reddit_api_info('/r/AskReddit/hot').json()
    postsData: Array[Post] = get_response_posts_info(postsResponse)
    
    for post in postsData:
        print(post.toJson())

     
def get_access_token():    
    auth = requests.auth.HTTPBasicAuth(REDDIT_CLIENT_KEY, REDDIT_SECRET)
    data = {
        'grant_type': 'password',
        'username': USERNAME,
        'password': REDDIT_PASSWORD
    }

    res = requests.post("https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=headers)
    return res.json()['access_token']

def request_reddit_api_info(path: str) -> requests.Response:
    requested_url = f'{DEFAULT_REDDIT_URL}{path}'
    response = requests.get(requested_url, headers=headers)
    return response

def get_response_posts_info(posts: requests.Response) -> Array[Post]:
    postsInstances: Array[Post] = []
    children = posts['data']['children']
    for post in children:
        postsInstances.append(get_post_data_by_json(post))
        
    return postsInstances
          
def get_post_data_by_json(post: Dict)-> Post:
    data = post['data']
    if data == None:
        raise Exception("no data was found in post")
    
    post = Post(title=data['title'], 
                subreddit=data['subreddit_name_prefixed'],
                author=data['author'],
                up_votes_amount=data['ups'],
                content=data['selftext'],
                url=data['url']
            )
    
    return post


if __name__ == '__main__':
    main()