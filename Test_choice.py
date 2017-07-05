import requests
from self_info import self_info
from get_user_info import get_user_info
from get_user_id import get_user_id
from get_my_post import get_my_post
from get_user_post import  get_user_post
from like_post import like_a_post
from colorama import init
init()
from colorama import Back,Fore
def start_my_bot():
    Show_menu=True
    while Show_menu:
        print Back.LIGHTBLUE_EX+ Fore.RED+ "---welcome to the Instabot---"
        print Fore.BLACK + "The menu option  shows the menu choices...!"
        print Fore.BLACK + "Select the option menu to get the datails of user"
        menu_choices="Hello.....,what you want to do...? \n 1.self information of user \n 2.Information about other user \n 3.Get id of other user\n 4.Display My recent post \n 5.Disply recent post of other user \n 6.Get post id \n 7 .Like posts  \n 8. exit program"
        choice=raw_input(menu_choices)
        if len(choice)>0:
            choice=int(choice)

            if choice==1:
                self_info()
            if choice==2:
                insta_username=raw_input("Enter user name")
                get_user_info(insta_username)
            if choice==3:
                insta_username=raw_input("Enter the username of user")
                result=get_user_id(insta_username)
                print result
            if choice==4:
                get_my_post()
            if choice==5:
                insta_username = raw_input("Please enter user name")
                get_user_post(insta_username)

            if choice==6:
                insta_username=raw_input("Enter user name")
                res=get_user_id(insta_username)
                print res
            if choice==7:
                insta_username = raw_input("Please enter user name")

                like_a_post(insta_username)
            if choice==8:
                Show_menu= False


start_my_bot()