#post comments initialised
import requests
from constants import  *
from get_user_post import get_user_post
def post_comment(insta_username):

    media_id=get_user_post(insta_username)
    comment_txt=raw_input("Enter your comment here...:-")

    request_url=(BASE_URL + 'media/%s/comments') + (media_id)
    payload={"access_token:":APP_ACCESS_TOKEN,"text" : comment_txt}
    print 'POST request url : %s ' %(request_url)
    comment_on_post=requests.post(request_url,payload).json()

    if comment_on_post['meta']['code']==200:
        print'successfully add a new comment'
    else:
        print"unable to comment .. please Try again..!"
insta_username=raw_input("Enter the username")
post_comment(insta_username)