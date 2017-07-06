                                    #objective to take user intrests and plot using matplot library
import  matplotlib
#import matplotlib.pyplot as plt
#labels ='High', 'low' 'none'
#sizes=[60,30,10]
#explode=(0.1,0,0)
#fig1, ax1 = plt.subplots()
#ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
 #       shadow=True, startangle=90)
#ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

#plt.show()

#Get user intrests initialised
#Requests library added
import requests
from constants import *
from get_user_post import get_user_post

#function defination

def user_intrests(insta_username):
 # fetch current user post
    media_id=get_user_post(insta_username)
    request_url=(BASE_URL +'tags/search/?q=baddi_university&access_token=%s') %(APP_ACCESS_TOKEN)
    print "Get request url : %s" %(request_url)
    intrests_info=requests.get(request_url).json()
    print intrests_info

    if intrests_info['meta']['code']==200:

        if len(intrests_info['data']):

            return intrests_info['data'][0]
        else:
            return None
    else:

        print 'Status code other than 200 received!'
        exit()

insta_username=raw_input("Enter the user name")

user_intrests(insta_username)
