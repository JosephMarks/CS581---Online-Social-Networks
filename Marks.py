# Author:  Joseph Marks

#  youtube.py searches YouTube for videos matching a search term and max results

# To run from terminal window:   python3 Marks.py
# To run from Anaconda terminal window: python Marks.py
# Please note external packages have been used including pandas, csv, collections, and unidecode
# Please ensure these external packages have been downloaded prior to running program
# Installing external packages can be accomplished by typing in terminal: pip install [package name]

from googleapiclient.discovery import build      # use build function to create a service object
import pandas as pd                    
import csv
from collections import OrderedDict
import unidecode

# put your API key into the API_KEY field below, in quotes
API_KEY = "AIzaSyANBYBfavwass2l05uUM0XndBxeSRGfV5U"

API_NAME = "youtube"

# this should be the latest version
API_VERSION = "v3"       

# this is my defined function
def youtubeSearch(search_term, search_max):
    youtube = build(API_NAME, API_VERSION, developerKey=API_KEY)

    search_data = youtube.search().list(q=search_term, part="id,snippet", maxResults=search_max).execute()

    # initializing dictionary data structures to hold my search results
    resultsDictionary = {}
    rankedDictionary = {}

    # initializing counters to track number of results - First counter for comprehensive results, second for ranked top 5 like ratio results
    counter_1 = 0
    counter_2 = 0

    # for loop to capture search results
    for search_instance in search_data.get("items", []):
        if search_instance["id"]["kind"] == "youtube#video":
            
            # increment my counter - found a video result
            
            # video id variable populated 
            videoId = search_instance["id"]["videoId"]
            # video title variable populated
            title = search_instance["snippet"]["title"]
            title = unidecode.unidecode(title)
            
            # we are accessing the statistics section of the video resource
            video_data = youtube.videos().list(id=videoId,part="statistics").execute()
            for video_instance in video_data.get("items",[]):
                viewCount = video_instance["statistics"]["viewCount"]
                if 'dislikeCount' not in video_instance["statistics"]:
                    dislikeCount = 0
                else:
                    dislikeCount = video_instance["statistics"]["dislikeCount"]
                if 'likeCount' not in video_instance["statistics"]:
                    likeCount = 0
                else:
                    likeCount = video_instance["statistics"]["likeCount"]

            # we are accessing the contentDetails section of the video resource
            video_data_content = youtube.videos().list(id=videoId,part="contentDetails").execute()
            for video_conent in video_data_content.get("items",[]):
                duration = video_conent["contentDetails"]["duration"]

            
                
            # Main dictionary with full results ---- will be printed to the console, and saved to the csv file
            resultsDictionary[videoId] = {}
            resultsDictionary[videoId]["Video ID"] = videoId
            resultsDictionary[videoId]["View Count"] = viewCount
            resultsDictionary[videoId]["Like Count"] = likeCount
            resultsDictionary[videoId]["Dislike Count"] = dislikeCount
            resultsDictionary[videoId]["Duration"] = duration
            resultsDictionary[videoId]["Title"] = title
            counter_1 = counter_1 + 1

            # computation of like percent to be used for ranking top 5 videos -- here, I have conditional to check viewCount. If viewCount == 0, I continue
            # to next iteration of the for loop as I don't want to include in my top 5 ranking
            viewCount = int(viewCount)
            if viewCount != 0:
                likePercent = round(((int(likeCount) / int(viewCount))*100),2)
                
            else:
                continue

            # Dictionary to display limited parameters, descending by like percent --- also displayed to the console
            rankedDictionary[videoId] = {}
            rankedDictionary[videoId]["Like Percentage"] = likePercent
            rankedDictionary[videoId]["View Count"] = viewCount
            rankedDictionary[videoId]["Like Count"] = likeCount
            rankedDictionary[videoId]["Title"] = title
            counter_2 = counter_2 + 1
            

    # print statement to the console
    print("Here are your search results for: {}\nThe maximum number of results specified: {}\n".format(search_term, search_max))

    # pandas utilized to create a dataframe for ease and neatness of printing to console
    df_results = pd.DataFrame.from_dict(resultsDictionary, orient='index').reset_index(drop=True)
    df_results.index = pd.RangeIndex(start=1, stop=counter_1+1, step=1)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)
    print(df_results)
    print("\n")
    
    # lambda function used -- collection package being used to order my dictionary descending by like percentage
    ordered = OrderedDict(sorted(rankedDictionary.items(), key = lambda i: -i[1]['Like Percentage']))
    
    # print statement, using format string to tell user what is being displayed
    print("Below I have displayed the top five videos for {} for like percentage, ranked in descending order..\n".format(search_term))

    # pandas utilized to create a second dataframe for ranked by like percentage display to console
    df_ranked_results = pd.DataFrame.from_dict(ordered, orient='index').reset_index(drop=True)
    df_ranked_results.index = pd.RangeIndex(start=1, stop=counter_2+1, step=1)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)
    df_results3 = df_ranked_results.head(5)
    print(df_results3)

    # Format print statement used to let user know of csv output file - also file name is customized based on search terms
    print("\n")
    print("Make sure to not forget to reference the csv file named {}_Results.csv that I have prepared for you for search results for {}!!\n".format(search_term, search_term))
    suffix = "_Results.csv"
    prefix = search_term
    file_name = prefix + suffix
    
    df_results.to_csv(file_name, encoding='utf-8')

# Calls my defined function above, but first asks for search term and search max input from user
search_term = input("What would you like to search for today? ")
while True:
    try:
        search_max = int(input("What is the maximum  number of results today? "))
    except:
        print("You will need to input an integer for the search. Please try again.. ")
        continue
    else:
        print("Thank you for using Youtube Search Pro today! Your results will be displayed, and a csv output file saved momentarily... \n")
        break

# Once input values supplied from user, function called with parameters passed in here
youtubeSearch(search_term, search_max)

