import requests
from constants import *
#function initialised
def self_info():
    request_url=(BASE_URL+ 'users/self/?access_token=%s') %(APP_ACCESS_TOKEN)
    print 'Get request url= %s' %(request_url)
    user_info=requests.get(request_url).json()
