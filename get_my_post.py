#Get my post is initialised
#import requests
import requests

from constants import *
#for downloading images
import urllib

#function iniatilised
def get_my_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    my_media = requests.get(request_url).json()
#responce code for request
    if my_media['meta']['code']==200:
        #coditional check
        if len(my_media['data']):
            image_name=my_media['data'][0]['id'] + '.jpeg'
            image_url=my_media['data'][0]['images']['standard_resolution']['url']
            #To fetch or retrieve user image
            urllib.urlretrieve(image_url,image_name)
            print 'Image downloaded successfully...!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'

    return None