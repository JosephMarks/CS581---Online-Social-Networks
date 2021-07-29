# Author: Joseph Marks

# This program accesses data from a twitter user site. It allows for the users
# to input a twitter screenname to lookup and will continue asking for screennames
# to look up until the user types "Stop".
# The program will output information on the twitter profile retrieved, including The
# user screenname, username, user ID, user description, location, number of friends,
# and number of followers. Additionally, the program will print to the scrrn the screennames
# of the five most recent followers of the user account, and the most 5 recent tweets.

# To run from terminal window:   python3 Marks.py
# To run from Anaconda terminal window: python Marks.py
# Please note external packages have been used including tweepy, and textwrap
# Please ensure these external packages have been downloaded prior to running program
# Installing external packages can be accomplished by typing in terminal: pip install [package name]

# Tweepy used to work with the Twitter API
# Textwrap used to format my output in a more professional way
import tweepy
import textwrap

# Consumer key, consumer key secren as well as access token and token secret enetered here.
# These are obtained from Twitter by registering for a developer account to use their API.
CONSUMER_KEY = "eE4HjeLxW3qMRHEh6DXhiJUuF"
CONSUMER_KEY_SECRET = "4aHK55bp0sJfILiS0aOuYoTvz6GOcXbJUkboDttDyhCAHU6taV"
ACCESS_TOKEN = "1416426245395525632-Dj5rugddeAu2CGJdjmj3O4eQbXk9JH"
ACCESS_TOKEN_SECRET = "sRctkoSWQwbdduHPUdM2nvnCMvz4UCUqzGamztyz8POfq"

# Authentication
authenticate = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
authenticate.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#  use wait_on_rate_limit to avoid going over Twitter's rate limits
api = tweepy.API(authenticate, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

# Defined function to obtain user information and display to the console
def getUserInformation(userInput):
    # assign to twitter_user variable
    twitter_user = api.get_user(userInput)
    # Convert to a string
    twitter_user_id = str(twitter_user.id)
    # Get Basic Account Information, and provide to the user on the console
    print("\n")
    print("************************************************************************")
    print("               Twitter User Information")
    print("************************************************************************")
    print("twitter_user screen name: ",twitter_user.screen_name)
    print("twitter_user name: ", twitter_user.name)
    print("twitter_user id: ", twitter_user.id)
    print("twitter_user description: ", textwrap.fill(twitter_user.description, 50))
    print("twitter_user location: ", twitter_user.location)
    print("twitter_user friend_count: ", twitter_user.friends_count)
    print("twitter_user followers_count: ", twitter_user.followers_count)
    print("\n")


    # Determine an Account’s Friends
    friends = []


    # Creating a Cursor
    #cursor = tweepy.Cursor(api.followers, screen_name=userInput)

    print("************************************************************************")
    print("\nMost recent 5 followers of {}: ".format(twitter_user.name))
    print("************************************************************************")
    # Counter initiated,and used below to number followers for output.
    follower_counter = 1
    try:
        # Creating a cursor to capture the 5 followers of the profile
        for follower in tweepy.Cursor(api.followers, twitter_user_id).items(5):
            print("{}. {} ".format(follower_counter, follower.screen_name))
            follower_counter = follower_counter + 1
    # Exception used in case information not accessible, as in a private account.
    # In this case, I will notify that no followers were able to be found.
    except:
        print("There were no followers found for {}.".format(twitter_user.name))

    print("\n")

    print("************************************************************************")
    print("\nMost recent 5 tweets of {}: ".format(twitter_user.name))
    print("************************************************************************")

    # Initializing counter so I can number the tweets to be output below
    counter = 1
    try:
        #variable to capture 5 tweets from the user's profile
        statuses = api.user_timeline(twitter_user_id)
        for status in statuses[:5]:
            print("TWEET {}: {} ".format(counter, textwrap.fill(status.text,60)))
            counter = counter + 1
            print("\n")

    except:
        # Exception used again in this instance for private/locked profiles
        print("There were no tweets found for {}.".format(twitter_user.name))
        print("\n")

# Routine as a loop that will continue to ask for username input until the user enters "stop"
while True:
    # Variable to capture what the user inputs when prompted
    userInput = input('What twitter username would you like to look up?')
    # If user inputs "stop", the while loop will stop, ending the program
    if userInput.upper() == 'STOP':
        print("Thank you for using the Twitter search program. Program will now stop.")
        break
    # If "stop" is not provided as the input, proceed with calling the 'getUserInformation' function defined above.
    else:
        try:
            # Function defined above, with userInput (username) as the parameter.
            getUserInformation(userInput)
        except:
            # If the username doesn't exist, I want to alert the user and allow to try again.
            print("This user does not extist, please try again..")
            continue
