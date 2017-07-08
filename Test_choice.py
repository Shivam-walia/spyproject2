#Test file is initialised

#imports the request library

import requests

#import all the required files
from self_info import self_info
from get_user_info import get_user_info
from get_user_id import get_user_id
from get_my_post import get_my_post
from get_user_post import  get_user_post
from get_post_id import get_post_id
from like_post import like_a_post
from post_comments import post_comment
from Negtive_comments_delete import delete_negative
#from get_user_intrests import user_intrests
from get_test_hashtag import  get_hashtag
#colour coding colorama library is used
from colorama import init
init()

#background and front colour added
from colorama import Back,Fore

#function initialised
def start_my_bot():
    Show_menu=True

    #loop will be executed for menu choices
    while Show_menu:
        print Back.WHITE+ Fore.RED+ "---welcome to the Instabot---"
        print Fore.BLACK + "The menu option  shows the menu choices...!"
        print Fore.BLACK + "Select the option menu to get the datails of user"
        menu_choices="Hello.....,what you want to do...? \n 1.self information of user \n 2.Information about other user \n 3.Get id of other user\n 4.Display My recent post \n 5.Disply recent post of other user \n 6.Get post id \n 7 .Like posts  \n 8.Comment on posts\n 9. Delete negative comments\n 10.Get user intrests \n 11.Get hashtags on comments\n 12. Exit program"
        choice=raw_input(menu_choices)

        #checks for string length
        if len(choice)>0:
            choice=int(choice)
        #self info of the user
            if choice==1:
                self_info()
        #Getting another user info
            if choice==2:
                insta_username=raw_input("Enter user name")
                get_user_info(insta_username)
        #Getting id of another user
            if choice==3:
                insta_username=raw_input("Enter the username of user")
                result=get_user_id(insta_username)
                print result
        #own recent posts
            if choice==4:
                get_my_post()
        #User recent post
            if choice==5:
                insta_username = raw_input("Please enter user name")
                get_user_post(insta_username)
        #Post id of another user
            if choice==6:
                insta_username=raw_input("Enter user name")
                res=get_post_id(insta_username)
                print res
        #like a post of user
            if choice==7:
                insta_username = raw_input("Please enter user name")

                like_a_post(insta_username)
        #comment on user posts
            if choice==8:
                insta_username=raw_input("please enter user name")
                post_comment(insta_username)
        #Deletes negative comments on posts
            if choice==9:
                insta_username=raw_input("please enter user name")
                delete_negative(insta_username)
        #Getting user intrests
 #           if choice==10:
  #              insta_username=raw_input("please enter user name")
   #             user_intrests(insta_username)
        #Getting comments hashtags
            if choice==11:
                insta_username=raw_input("please enter user name")
                get_hashtag(insta_username)
        #Exit From program
            if choice==12:
                Show_menu= False


#function calling to start instabot
start_my_bot()