import requests
from constants import *
import urllib

#function iniatilised
def get_my_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    my_media = requests.get(request_url).json()

    if my_media['meta']['code']==200:
        #coditional check
        if len(my_media['data']):
            image_name=my_media['data'][0]['id'] + '.jpeg'
            image_url=my_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url,image_name)
            print 'Image downloaded successfully...!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'

    return None