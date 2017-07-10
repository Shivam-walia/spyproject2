#post comments initialised
#Request library is imported
import requests
from constants import  *
#Imports the post id of user
from get_post_id import get_post_id

#function defination for post comment

def delete_comment(insta_username):
#Takes the post id of user
    media_id=get_post_id(insta_username)
    comment_id=get_post_id(insta_username)
#inpur or enter comment

    request_url=(BASE_URL + 'media/%s/comments/?access_token=%s') %(media_id,comment_id,APP_ACCESS_TOKEN)
    print 'DEL request url : %s ' %(request_url)
  #fetch url and info
    Delete_post=requests.delete(request_url).json()
    print Delete_post
#Response code check
    if Delete_post['meta']['code'] == 200:
        print'successfully Deleted a  comment'
    else:
        print"unable to Delete .. please Try again..!"
#insta_username=raw_input("Enter user name")
#delete_comment(insta_username)
