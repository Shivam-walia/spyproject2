#get_user_id file is created
#Requests library is added
import requests
#Base address and app token
from constants import  *
# function definanation
def get_user_id(insta_username):
    #Request url is generated

    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') %(insta_username,APP_ACCESS_TOKEN)
    print 'Get request url= %s' % (request_url)

    user_info = requests.get(request_url).json()
#condition check  for response code

    if user_info['meta']['code']==200:
        #check the length of string

        if len(user_info['data']):
            return user_info['data'][0]['id']

        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()

