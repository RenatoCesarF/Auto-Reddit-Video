from typing import Dict
from json import JSONEncoder
import json

from requests import delete

class Post(JSONEncoder):
    __id: str
    title: str
    author: str
    content: str
    subreddit: str
    url: str
    up_votes_amount: int
    
    def default(self, o):
        return o.__dict__
    
    def __init__(self, title: str, author: str, content: str, 
                 subreddit: str, url: str, up_votes_amount: int = 0):
        self.title = title
        self.author = author
        self.content = content
        self.subreddit = subreddit
        self.up_votes_amount = up_votes_amount
        self.url = url
        
        urlSplited = url.split('/')
        self.__id = urlSplited[-2]
    
    
    def toJson(self) -> Dict:
        dictObject = {
            'id': self.__id, 
            'title': self.title, 
            'author': self.author, 
            'content': self.content,
            'subreddit': self.subreddit,
            'upVotesAmount': self.up_votes_amount,
            'url': self.url  
        }
        return dictObject;

    def get_id(self) -> str:
        return self.__id
    
    def get_self_representation_in_string(self) -> str:
        return (
            f"ID: {self.__id}\n"
            f"title: {self.title}\n"
            f"author: {self.author}\n"
            f"subreddit: {self.subreddit}\n"
            f"url: {self.url}\n"
            f"up votes: {self.up_votes_amount}\n"
            f"content: {self.content}\n"
        )
            
    def __str__(self) -> str:
        return self.get_self_representation_in_string()
      
                
    def __repr__(self) -> str:
        return self.get_self_representation_in_string()
            
 