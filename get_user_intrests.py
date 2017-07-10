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
from get_post_id import get_post_id
#function defination

def user_intrests(insta_username):
 # fetch current user post
    media_id=get_user_post(insta_username)
    request_url=(BASE_URL +'tags/search/?q=baddi_university&access_token=%s') %(APP_ACCESS_TOKEN)
    print "Get request url : %s" %(request_url)
    intrests_info=requests.get(request_url).json()


    if intrests_info['meta']['code']==200:

        if len(intrests_info['data']):

            for val in range(0, len(intrests_info['data'])):
                get_post_id = intrests_info['data'][val]
                use_text = intrests_info['data'][val]['text']

            if intrests_info[0]=='#':
                print "These are the hashtags used : %s " %(intrests_info)

        else:
            return None
    else:

        print 'Status code other than 200 received!'
        exit()

user_intrests("rahul")


