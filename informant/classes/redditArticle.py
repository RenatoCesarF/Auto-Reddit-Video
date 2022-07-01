from __future__ import annotations
from ast import Dict
from json import JSONEncoder

from utils.clean_text import clean_text

class RedditArticle(JSONEncoder):
    id: str
    author: str
    author_img: str = None
    content: str
    mk_content: str
    subreddit: str
    url: str
    up_votes_amount: int
    
    def __init__(self, author: str, content: str, subreddit: str, 
                 url: str, id: str, up_votes_amount: int = 0):
        self.author = author
        self.mk_content = content
        self.content = clean_text(str(content))
        self.subreddit = subreddit
        self.up_votes_amount = up_votes_amount
        self.url = url
        self.id = id
        
    @staticmethod
    def create_article_from_dict(data: Dict) -> RedditArticle:
        id = data.get('id')
        author = data.get('author')
        ups = data.get('ups')
        subreddit = data.get('subreddit')
        body = data.get('body')
        url = "data.get('url')"
        
        reply = RedditArticle(author, body, subreddit, url, id, ups)
        return reply
    
            
    def to_json(self) -> Dict:
        dictObject = {
            'id': self.id, 
            'author': self.author, 
            'authorImage': self.author_img,
            'content': self.mk_content,
            'subreddit': self.subreddit,
            'upVotesAmount': self.up_votes_amount,
            'url': self.url
        }
        return dictObject;    
    
    def __get_self_representation_in_string(self) -> str:
        return (
            f"ID: {self.id}\n"
            f"author: {self.author}\n"
            f"subreddit: {self.subreddit}\n"
            f"url: {self.url}\n"
            f"up votes: {self.up_votes_amount}\n"
            f"content: {self.content}\n"
        )
    def __str__(self) -> str:
        return self.__get_self_representation_in_string()
    
    def default(self, o):
        return o.__dict__
    