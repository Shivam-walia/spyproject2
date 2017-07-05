#import required files
import requests
from  constants import *
from get_user_id import get_user_id

#function initiated
def get_user_info(insta_username):
    user_id=get_user_id(insta_username)
    if user_id==None:
        print"The user does dot exist"
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()


    if user_info['meta']['code'] == 200:
        # conitional check
        if len(user_info['data']):
            print 'username : %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you ae following %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts %s' % (user_info['data']['counts']['media'])
        else:
            print 'user do not exist'
    else:
        print'status code other tha 200 recieved'