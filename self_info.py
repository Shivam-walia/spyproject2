#Self info  file is created
#import required files and library
import requests
from constants import *

#function initialised

def self_info():
    #Generates request url
    request_url=(BASE_URL+ 'users/self/?access_token=%s') %(APP_ACCESS_TOKEN)
    print 'Get request url= %s' %(request_url)
    user_info=requests.get(request_url).json()

    #Condition check for request

    if user_info['meta']['code']==200:
        #conitional check

        if len(user_info['data']):

     # The user details is displayed

            print 'username : %s' %(user_info['data']['username'])
            print 'No. of followers: %s' %(user_info['data']['counts']['followed_by'])
            print 'No. of people you ae following %s' %(user_info['data']['counts']['follows'])
            print 'No. of posts %s' %(user_info['data']['counts']['media'])


        else:
            print 'user do not exist'
    else:
        print'status code other tha 200 recieved'