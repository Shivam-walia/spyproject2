#function defination

import requests

# import base url and access token

from constants import *
from get_post_id import get_post_id

#function defination

def like_a_post(insta_username):

  #Asks for the post id of user

    media_id=get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') %(media_id)

  #post request

    payload = {"access_token": APP_ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    print post_a_like
    #conditional check for reaponse code

    if post_a_like['meta']['code']==200:
        print "successfully liked...!"
    else:
        print "unsuccessfull ..please try again...!"


