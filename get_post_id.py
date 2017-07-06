#get_post_id is initialised

import requests
#Acces token and base url imported

from constants import *

from get_user_id import get_user_id

#function defination

def get_post_id(insta_username):

    #Takes the user id

    user_id = get_user_id(insta_username)

    #codition check

    if user_id == None:

        print 'User does not exist!'

        exit()
    #Request url will be generated

    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    #Checks response code

    if user_media['meta']['code'] == 200:
        #length must be more than 0

        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print 'There is no recent post of the user!'
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()
