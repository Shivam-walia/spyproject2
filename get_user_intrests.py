                                    #objective to take user intrests and plot using matplot library

#Get user intrests initialised
#Requests library added
import requests
from constants import *
from get_user_post import get_user_post

#function defination

def user_intrests(insta_username):
 # fetch current user post
    media_id=get_user_post(insta_username)
    request_url=(BASE_URL + 'tags/%s/tag-name') %(APP_ACCESS_TOKEN)
    print "Get request url : %s" %(request_url)
    intrests_info=requests.get(request_url).json()
    print intrests_info

   # if intrests_info['meta']['data']==200:
    #    if len(intrests_info['data']):

            #return intrests_info['data'][0]['tags']
        #else:
            #return None
    #else:

        #print 'Status code other than 200 received!'
        #exit()

insta_username=raw_input("Enter the user name")

user_intrests(insta_username)
