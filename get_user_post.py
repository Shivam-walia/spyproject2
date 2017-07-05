import requests
from constants import *
from get_user_id import  get_user_id
import urllib
#function initialised
def get_user_post(insta_username):
    user_id=get_user_id(insta_username)
    if user_id==None:
        print 'The user does not exists...!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()
    if user_media['meta']['code'] == 200:
 # coditional check
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Image downloaded successfully...!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'
    return None