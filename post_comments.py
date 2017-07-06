#post comments initialised
import requests
from constants import  *
from get_post_id import get_post_id
def post_comment(insta_username):

    media_id=get_post_id(insta_username)
    comment_text=raw_input("Enter your comment here...:-")
    payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
    request_url=(BASE_URL + 'media/%s/comments') %(media_id)
    print 'POST request url : %s ' %(request_url)
    comment_on_post=requests.post(request_url,payload).json()
    print comment_on_post
    if comment_on_post['meta']['code'] == 200:
        print'successfully add a new comment'
    else:
        print"unable to comment .. please Try again..!"
insta_username=raw_input("Enter the username")
post_comment(insta_username)