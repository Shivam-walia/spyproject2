#post comments initialised
#Request library is imported
import requests
from constants import  *
#Imports the post id of user
from get_post_id import get_post_id

#function defination for post comment

def post_comment(insta_username):
#Takes the post id of user
    media_id=get_post_id(insta_username)
#inpur or enter comment
    comment_text=raw_input("Enter your comment here...:-")
    payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
    request_url=(BASE_URL + 'media/%s/comments') %(media_id)
    print 'POST request url : %s ' %(request_url)
  #fetch url and info
    comment_on_post=requests.post(request_url,payload).json()
    print comment_on_post
#Response code check
    if comment_on_post['meta']['code'] == 200:
        print'successfully add a new comment'
    else:
        print"unable to comment .. please Try again..!"
