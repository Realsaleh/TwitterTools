import tweepy
import os
import sys
import time

validyes = ["y" , "yes", "Y", "Yes", "YES"]
validback = ["B", "b"]
validhelp = ["help", "HELP", "Help"]

def get_twitter_api():
    consumer_key = " Your_API_key"
    consumer_secret = "Your_API_secret_key"
    access_token = "Your_Access_token"
    access_token_secret = "Access_token_ssecret"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

def actSendTweet():
    api = get_twitter_api()
    Tweet = str(input("Say Somthing:"))
    Image = str(input("Does Your Tweet Include Image? Y/N?"))
    if Image in validyes:
        TweetImage = input("Give Me Your Image Address?")
        api.update_with_media(TweetImage, Tweet)
        print ("Your Tweet Was Sent Successfully.")
    else:
        print("OK! :)")
        api.update_status(status =(Tweet))
        print ("Your Tweet Was Sent Successfully.")
        UserInput = input("What Can I Do For You? :)")

def actUnFollow():
    api = get_twitter_api()
    print ("Loading Followers...")
    followers = []
    for follower in tweepy.Cursor(api.followers).items():
        followers.append(follower)

    print("Found %s Followers, Finding Friends..." % len(followers))
    friends = []
    for friend in tweepy.Cursor(api.friends).items():
        friends.append(friend)

    friend_dict = {}
    for friend in friends:
        friend_dict[friend.id] = friend

    follower_dict = {}
    for follower in followers:
        follower_dict[follower.id] = follower

    non_friends = [friend for friend in friends if friend.id not in follower_dict]

    print ("Unfollowing %s People Who Don't Follow You Back" % len(non_friends))
    print ("This Will Take Approximately Please Wait...")

    for nf in non_friends:
        print ("Unfollowing %s" % nf.screen_name)
        try:
            nf.unfollow()
        except:
            print ("Something Went Wrong, Sleeping For 5 Seconds And Then Trying Again.")
            time.sleep(5)
            nf.unfollow()
        print ("Congrat,No None Follower Remaining.")
        UserInput = input("What Can I Do For You? :)")

def actHelp():
    print("[+]HELP Menu[+]")
    print("[-]For Sending Tweet Send '1'")
    print("[-]For Unfollowing People Who Don't Follow You Back Send '2'")
    print("[-]For Following Back To All Of Your Followers Send '3'")
    print("[-]To Return To The Main Menu In Each Section Send 'B'")
    UserInput = input("What Can I Do For You?:)")

def actFollow():
    api = get_twitter_api()
    for follower in tweepy.Cursor(api.followers).items():
            follower.follow()
            print ("User", follower.screen_name ,"Was Followed.")
    UserInput = input("What Can I Do For You?:)")

os.system("title Twitter Tools v1.0")
os.system('cls' if os.name == 'nt' else 'clear')
print ("[-] Twitter Tools v1.0")
print ("[-] Coded By RealSalehn ")
print ("[-] https://github.com/Realsaleh/TwitterTools ")
print ("[-] To See Help Menu Send Me 'HELP'.")

UserInput = input("What Can I Do For You?:)")

while True:
    if UserInput == "1":
        actSendTweet()
    elif UserInput == "2":
        actUnFollow()
    elif UserInput in validhelp:
        actHelp()
    elif UserInput == "3":
        actFollow()
    elif UserInput in validback:
        UserInput = input("What Can I Do For You?:)")
    else:
        print("Error!")
        actHelp()
        UserInput = input("What Can I Do For You?:)")