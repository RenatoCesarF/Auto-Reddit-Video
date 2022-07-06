from dotenv import load_dotenv

from classes.instagram_api import InstagramAPI
from classes.log import log
load_dotenv()


            
insta = InstagramAPI(publication_type="REELS")
result = insta.publish("http://techslides.com/demos/sample-videos/small.mp4", "testing api posting")
print(result)


