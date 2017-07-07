#library for drawing objects

from  textblob import TextBlob

from textblob.sentiments import NaiveBayesAnalyzer

#request library initialised

import requests
from get_post_id import get_post_id

#takes the access token and base url
from constants import *

#function defination
def delete_negative(insta_username):

    #takes the post id of user
    media_id=get_post_id(insta_username)

    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print "Get request url : %s" %(request_url)
    comments_data=requests.get(request_url).json()

#condition check whether responce 200
    if comments_data['meta']['code'] == 200:

        #length must be greater than o

        if len(comments_data['data']):

            #loop exit when no comment found

            for val in range(0,len(comments_data['data'])):
                comment_id=comments_data['data'][val]['id']
                comment_text = comments_data['data'][val]['text']

                #use of blob lib to analyse negativ comments if any
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if blob.sentiment.p_neg > blob.sentiment.p_pos:
                    print 'Negative comment : %s' % (comment_text)
                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (
                    media_id, comment_id, APP_ACCESS_TOKEN)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()

            #responce code condition check

                    if delete_info['meta']['code'] == 200:
                        print 'Comment successfully deleted!\n'
                    else:
                        print 'Unable to delete comment!'
                else:
                    print 'Positive comment : %s\n' % (comment_text)

        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'


