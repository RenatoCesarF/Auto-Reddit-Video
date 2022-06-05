from email import header
import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv()
REDDIT_SECRET = getenv('REDDIT_SECRET')
REDDIT_CLIENT_KEY = getenv('REDDIT_CLIENT_KEY')
REDDIT_PASSWORD = getenv('REDDIT_PASSWORD')

DEFAULT_REDDIT_URL = 'https://oauth.reddit.com/api/v1'
USERNAME = 'auto-reddit-video'
headers = {'User-Agent': 'auto-video/0.0.1'}
TOKEN = ""

def main():
    TOKEN = get_access_token()
    headers['Authorization'] = f'bearer {TOKEN}'
    
    requested_url = f'{DEFAULT_REDDIT_URL}/r/python/news'
    posts = requests.get(requested_url, headers=headers)
    print(requested_url)
    print(posts.json())
    
def get_access_token():    
    auth = requests.auth.HTTPBasicAuth(REDDIT_CLIENT_KEY, REDDIT_SECRET)
    data = {
        'grant_type': 'password',
        'username': USERNAME,
        'password': REDDIT_PASSWORD
    }

    res = requests.post("https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=headers)
    return res.json()['access_token']



if __name__ == '__main__':
    main()