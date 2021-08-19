# Author: Joseph Marks
# This program processes data from a Pew Research poll about Internet
# usage and social media usage of participants. The survey looks at
# different participants across a wide range of demographics, eduational
# levels, income, and generations.
# The program accesses the survey data from the "Pew_Survey.csv" file.
# Please ensure that this file is saved in the same path/folder as you save this
# python program.

# To run from terminal window: python3 Marks.py
# To run from Anaconda terminal window: python Marks.py
# Please note an external package has been used for this program: matplotlib.
# Make sure this exzternal library is downloaded prior to running the program
# Installing external packages can be accomplished by typing in the terminal: pip install matplotlib
# matplotlib has been used to assist with presenting data in plots to graphically represent the data
# processed from the survey.

# Import the matplotlib library
import matplotlib.pyplot as plt
# open the pew survey file that has the survey data, then close it.
f = open("Pew_Survey.csv")
masterDataList = f.read().splitlines()
f.close()

# Create a list of the title headers from the file
titleList = []
titleList = masterDataList[0]

# create a list of all data rows from the file
dataList = []
dataList = masterDataList[1:]
cleanDataList = []

# Use a for loop to iterate through the datalist read in and split at commas
for i in range(len(dataList)):
    cleanDataList.append(dataList[i].split(","))

# Analysis of the survey results in its entirety, before looking at different demographics
# First analysis is total number of users that use each social media network - will be
# presented tabular style to the terminal and graphically as a pie plot.

# Total number of twitter users - for loop used to iterate through responses, and oneCounterInstagram
# respondents that used twitter (denoted as a '1' response in the survey)
twitterSum = 0

for i in range(len(cleanDataList)):
    twitterResponse = cleanDataList[i][4]
    if twitterResponse == '1':
        twitterSum = twitterSum + 1
    else:
        continue
print("The number of users that are using Twitter: {}".format(twitterSum))

# Total number of Instagram users - for loop used to iterate through responses, and counts
# respondents that used instagram (denoted as a '1' response in the survey)
instagramSum = 0

for i in range(len(cleanDataList)):
    instagramResponse = cleanDataList[i][5]
    if instagramResponse == '1':
        instagramSum = instagramSum + 1
    else:
        continue
print("The number of users that are using Instagram: {}".format(instagramSum))

# Total number of facebook users - for loop used to iterate through responses, and counts
# respondents that used facebook (denoted as a '1' response in the survey)
facebookSum = 0

for i in range(len(cleanDataList)):
    facebookResponse = cleanDataList[i][6]
    if facebookResponse == '1':
        facebookSum = facebookSum + 1
    else:
        continue
print("The number of users that are using Facebook: {}".format(facebookSum))

# Total number of snapchat users - for loop used to iterate through responses, and counts
# respondents that used snapchat (denoted as a '1' response in the survey)
snapChatSum = 0

for i in range(len(cleanDataList)):
    snapChatResponse = cleanDataList[i][7]
    if snapChatResponse == '1':
        snapChatSum = snapChatSum + 1
    else:
        continue
print("The number of users that are using SnapChat: {}".format(snapChatSum))

# Total number of youtube users - for loop used to iterate through responses, and counts
# respondents that used youtube (denoted as a '1' response in the survey)

youTubeSum = 0

for i in range(len(cleanDataList)):
    youTubeResponse = cleanDataList[i][8]
    if youTubeResponse == '1':
        youTubeSum = youTubeSum + 1
    else:
        continue
print("The number of users that are using YouTube: {}".format(youTubeSum))

# Total number of whatsapp users - for loop used to iterate through responses, and counts
# respondents that used whatsapp (denoted as a '1' response in the survey)

whatsAppSum = 0

for i in range(len(cleanDataList)):
    whatsAppResponse = cleanDataList[i][9]
    if whatsAppResponse == '1':
        whatsAppSum = whatsAppSum + 1
    else:
        continue
print("The number of users that are using WhatsApp: {}".format(whatsAppSum))


# Total number of pinterest users - for loop used to iterate through responses, and counts
# respondents that used pinterest (denoted as a '1' response in the survey)

pinterestSum = 0

for i in range(len(cleanDataList)):
    pinterestResponse = cleanDataList[i][10]
    if pinterestResponse == '1':
        pinterestSum = pinterestSum + 1
    else:
        continue
print("The number of users that are using Pinterest: {}".format(pinterestSum))


# Total number of linkedin users - for loop used to iterate through responses, and counts
# respondents that used linkedin (denoted as a '1' response in the survey)

linkedInSum = 0

for i in range(len(cleanDataList)):
    linkedInResponse = cleanDataList[i][11]
    if linkedInResponse == '1':
        linkedInSum = linkedInSum + 1
    else:
        continue
print("The number of users that are using LinkedIn: {}".format(linkedInSum))


# Total number of reddit users - for loop used to iterate through responses, and counts
# respondents that used reddit (denoted as a '1' response in the survey)

redditSum = 0

for i in range(len(cleanDataList)):
    redditResponse = cleanDataList[i][12]
    if redditResponse == '1':
        redditSum = redditSum + 1
    else:
        continue
print("The number of users that are using Reddit: {}".format(redditSum))
print("\n")


# This section of the program quantifies the frequency of internet use for the
# survey participants as a whole, without regard to demographics, generations, etc.

# Initialize counters to quantify the total of each response.
almostConstantlySum = 0 #response of 1
severalTimesPerDaySum = 0 #response of 2
aboutOncePerDaySum = 0 #response of 3
severalTimesPerWeekSum = 0 #response of 4
lessOftenSum = 0 #response of 5
dontKnowSum = 0 #response of 8
refusedSum = 0 #response of 9

# For loop used to iterate through my master list of data again, capturing the response
# of each participant, and tallying up the number of respondents in each category of frequency
# of internet usage. Conditionals used below to tally totals with if/elif statement.
for i in range(len(cleanDataList)):
    frequencyResponse = cleanDataList[i][1]
    if frequencyResponse == '1':
        almostConstantlySum = almostConstantlySum + 1
    elif frequencyResponse == '2':
        severalTimesPerDaySum = severalTimesPerDaySum + 1
    elif frequencyResponse == '3':
        aboutOncePerDaySum = aboutOncePerDaySum + 1
    elif frequencyResponse == '4':
        severalTimesPerWeekSum = severalTimesPerWeekSum + 1
    elif frequencyResponse == '5':
        lessOftenSum = lessOftenSum + 1
    elif frequencyResponse == '8':
        dontKnowSum = dontKnowSum + 1
    elif frequencyResponse == '9':
        refusedSum = refusedSum + 1
    else:
        continue

# Results that were quantified above are printed out to the terminal here.
print("The number of users that are using the internet almost constantly: {}".format(almostConstantlySum))
print("The number of users that are using the internet several times per day: {}".format(severalTimesPerDaySum))
print("The number of users that are using the internet about once per day: {}".format(aboutOncePerDaySum))
print("The number of users that are using the internet several times per week: {}".format(severalTimesPerWeekSum))
print("The number of users that are using the internet less often: {}".format(lessOftenSum))
print("The number of users that don't know: {}".format(dontKnowSum))
print("The number of users that refused: {}".format(refusedSum))
print("\n")




# Now I will look at the data from a few different persepectives, including the age/generations.
# I am interested in seeing how generations use the internet and social media differently.
# Now let's determine the most popular social media for age generations

# First section will total up the users that use the main social media networks asked about
# in the survey. Counters are initialized here, and below we will use our masterDataList to
# total up this information.
# gen z
genZSum = 0
genZTwitterSum = 0
genZInstagramSum = 0
genZFacebookSum = 0
genZSnapChatSum = 0
genZYouTubeSum = 0
genZWhatsAppSum = 0
genZPinterestSum = 0
genZLinkedinSum = 0
genZRedditSum = 0

# Iterate through the master data list, and if age is less than or equal to 24
# (how I am definining generation z), then I will capture their responses for
# social media use
for i in range(len(cleanDataList)):
    genZResponse = int(cleanDataList[i][23])
    if genZResponse <= 24:
        genZSum = genZSum + 1
        if cleanDataList[i][4] == '1':
            genZTwitterSum = genZTwitterSum + 1
        if cleanDataList[i][5] == '1':
            genZInstagramSum = genZInstagramSum + 1
        if cleanDataList[i][6] == '1':
            genZFacebookSum = genZFacebookSum + 1
        if cleanDataList[i][7] == '1':
            genZSnapChatSum = genZSnapChatSum + 1
        if cleanDataList[i][8] == '1':
            genZYouTubeSum = genZYouTubeSum + 1
        if cleanDataList[i][9] == '1':
            genZWhatsAppSum = genZWhatsAppSum + 1
        if cleanDataList[i][10] == '1':
            genZPinterestSum = genZPinterestSum + 1
        if cleanDataList[i][11] == '1':
            genZLinkedinSum = genZLinkedinSum + 1
        if cleanDataList[i][12] == '1':
            genZRedditSum = genZRedditSum + 1
    else:
        continue

# The total above have quantified generation z social media use. The totals are
# presented here to the terminal, and at the end of the program are plotted
print("The number of users that are gen Z are: {}".format(genZSum))
print("The number of gen Z users that use Twitter: {}".format(genZTwitterSum))
print("The number of gen Z users that use Instagram: {}".format(genZInstagramSum))
print("The number of gen Z users that use Facebook: {}".format(genZFacebookSum))
print("The number of gen Z users that use Snapchat: {}".format(genZSnapChatSum))
print("The number of gen Z users that use YouTube: {}".format(genZYouTubeSum))
print("The number of gen Z users that use WhatsApp: {}".format(genZWhatsAppSum))
print("The number of gen Z users that use Pinterest: {}".format(genZPinterestSum))
print("The number of gen Z users that use Linkedin: {}".format(genZLinkedinSum))
print("The number of gen Z users that use Reddit: {}".format(genZRedditSum))
print("\n")



# Now we will look at the millenials group. Estalishing counters here for each
# social media network
# millenials
millenialsSum = 0
millenialsTwitterSum = 0
millenialsInstagramSum = 0
millenialsFacebookSum = 0
millenialsSnapChatSum = 0
millenialsYouTubeSum = 0
millenialsWhatsAppSum = 0
millenialsPinterestSum = 0
millenialsLinkedinSum = 0
millenialsRedditSum = 0

# Iterate through my masterDataList, looking at respondents aged greater than or
# equal to 25, and less than or equal to 40.
for i in range(len(cleanDataList)):
    millenialsResponse = int(cleanDataList[i][23])
    if ((millenialsResponse >= 25) and (millenialsResponse <= 40)):
        millenialsSum = millenialsSum + 1
        if cleanDataList[i][4] == '1':
            millenialsTwitterSum = millenialsTwitterSum + 1
        if cleanDataList[i][5] == '1':
            millenialsInstagramSum = millenialsInstagramSum + 1
        if cleanDataList[i][6] == '1':
            millenialsFacebookSum = millenialsFacebookSum + 1
        if cleanDataList[i][7] == '1':
            millenialsSnapChatSum = millenialsSnapChatSum + 1
        if cleanDataList[i][8] == '1':
            millenialsYouTubeSum = millenialsYouTubeSum + 1
        if cleanDataList[i][9] == '1':
            millenialsWhatsAppSum = millenialsWhatsAppSum + 1
        if cleanDataList[i][10] == '1':
            millenialsPinterestSum = millenialsPinterestSum + 1
        if cleanDataList[i][11] == '1':
            millenialsLinkedinSum = millenialsLinkedinSum + 1
        if cleanDataList[i][12] == '1':
            millenialsRedditSum = millenialsRedditSum + 1
    else:
        continue

# Totals quantified above are presented here for the terminal, and will later be presented
# graphically in a pie chart.
print("The number of users that are millenials are: {}".format(millenialsSum))
print("The number of millenials users that use Twitter: {}".format(millenialsTwitterSum))
print("The number of millenials users that use Instagram: {}".format(millenialsInstagramSum))
print("The number of millenials users that use Facebook: {}".format(millenialsFacebookSum))
print("The number of millenials users that use Snapchat: {}".format(millenialsSnapChatSum))
print("The number of millenials users that use YouTube: {}".format(millenialsYouTubeSum))
print("The number of millenials users that use WhatsApp: {}".format(millenialsWhatsAppSum))
print("The number of millenials users that use Pinterest: {}".format(millenialsPinterestSum))
print("The number of millenials users that use Linkedin: {}".format(millenialsLinkedinSum))
print("The number of millenials users that use Reddit: {}".format(millenialsRedditSum))
print("\n")


# Now we will look at the next generation group, generation x
# genX
genXSum = 0
genXTwitterSum = 0
genXInstagramSum = 0
genXFacebookSum = 0
genXSnapChatSum = 0
genXYouTubeSum = 0
genXWhatsAppSum = 0
genXPinterestSum = 0
genXLinkedinSum = 0
genXRedditSum = 0

# Again, I will iterate through my data list and capture responses of people aged
# greater than or equal to 41, and less than or equal to 56 for this generation.
for i in range(len(cleanDataList)):
    genXResponse = int(cleanDataList[i][23])
    if ((genXResponse >= 41) and (genXResponse <= 56)):
        genXSum = genXSum + 1
        if cleanDataList[i][4] == '1':
            genXTwitterSum = genXTwitterSum + 1
        if cleanDataList[i][5] == '1':
            genXInstagramSum = genXInstagramSum + 1
        if cleanDataList[i][6] == '1':
            genXFacebookSum = genXFacebookSum + 1
        if cleanDataList[i][7] == '1':
            genXSnapChatSum = genXSnapChatSum + 1
        if cleanDataList[i][8] == '1':
            genXYouTubeSum = genXYouTubeSum + 1
        if cleanDataList[i][9] == '1':
            genXWhatsAppSum = genXWhatsAppSum + 1
        if cleanDataList[i][10] == '1':
            genXPinterestSum = genXPinterestSum + 1
        if cleanDataList[i][11] == '1':
            genXLinkedinSum = genXLinkedinSum + 1
        if cleanDataList[i][12] == '1':
            genXRedditSum = genXRedditSum + 1
    else:
        continue

# Totals are output to the terminal, and later will be plotted.
print("The number of users that are gen X are: {}".format(genXSum))
print("The number of gen X users that use Twitter: {}".format(genXTwitterSum))
print("The number of gen X users that use Instagram: {}".format(genXInstagramSum))
print("The number of gen X users that use Facebook: {}".format(genXFacebookSum))
print("The number of gen X users that use Snapchat: {}".format(genXSnapChatSum))
print("The number of gen X users that use YouTube: {}".format(genXYouTubeSum))
print("The number of gen X users that use WhatsApp: {}".format(genXWhatsAppSum))
print("The number of gen X users that use Pinterest: {}".format(genXPinterestSum))
print("The number of gen X users that use Linkedin: {}".format(genXLinkedinSum))
print("The number of gen X users that use Reddit: {}".format(genXRedditSum))
print("\n")



# Totaling values for the baby boomer generation.
# Boomers
BoomersSum = 0
BoomersTwitterSum = 0
BoomersInstagramSum = 0
BoomersFacebookSum = 0
BoomersSnapChatSum = 0
BoomersYouTubeSum = 0
BoomersWhatsAppSum = 0
BoomersPinterestSum = 0
BoomersLinkedinSum = 0
BoomersRedditSum = 0

# Interested in looking at respondents greater than or equal to 57, and less than or equal to 75.
for i in range(len(cleanDataList)):
    BoomersResponse = int(cleanDataList[i][23])
    if ((BoomersResponse >= 57) and (BoomersResponse <= 75)):
        BoomersSum = BoomersSum + 1
        if cleanDataList[i][4] == '1':
            BoomersTwitterSum = BoomersTwitterSum + 1
        if cleanDataList[i][5] == '1':
            BoomersInstagramSum = BoomersInstagramSum + 1
        if cleanDataList[i][6] == '1':
            BoomersFacebookSum = BoomersFacebookSum + 1
        if cleanDataList[i][7] == '1':
            BoomersSnapChatSum = BoomersSnapChatSum + 1
        if cleanDataList[i][8] == '1':
            BoomersYouTubeSum = BoomersYouTubeSum + 1
        if cleanDataList[i][9] == '1':
            BoomersWhatsAppSum = BoomersWhatsAppSum + 1
        if cleanDataList[i][10] == '1':
            BoomersPinterestSum = BoomersPinterestSum + 1
        if cleanDataList[i][11] == '1':
            BoomersLinkedinSum = BoomersLinkedinSum + 1
        if cleanDataList[i][12] == '1':
            BoomersRedditSum = BoomersRedditSum + 1
    else:
        continue

# Totals are quanitifed and printed out to the terminal, plotted later.
print("The number of users that are Boomers are: {}".format(BoomersSum))
print("The number of Boomers users that use Twitter: {}".format(BoomersTwitterSum))
print("The number of Boomers users that use Instagram: {}".format(BoomersInstagramSum))
print("The number of Boomers users that use Facebook: {}".format(BoomersFacebookSum))
print("The number of Boomers users that use Snapchat: {}".format(BoomersSnapChatSum))
print("The number of Boomers users that use YouTube: {}".format(BoomersYouTubeSum))
print("The number of Boomers users that use WhatsApp: {}".format(BoomersWhatsAppSum))
print("The number of Boomers users that use Pinterest: {}".format(BoomersPinterestSum))
print("The number of Boomers users that use Linkedin: {}".format(BoomersLinkedinSum))
print("The number of Boomers users that use Reddit: {}".format(BoomersRedditSum))
print("\n")


# The final generation that we will look at is post war, and that is anyone that is
# ages 76 or older.
# Post War
PostWarSum = 0
PostWarTwitterSum = 0
PostWarInstagramSum = 0
PostWarFacebookSum = 0
PostWarSnapChatSum = 0
PostWarYouTubeSum = 0
PostWarWhatsAppSum = 0
PostWarPinterestSum = 0
PostWarLinkedinSum = 0
PostWarRedditSum = 0

# Access data from respondents that fit this profile, of aged 76 or older
for i in range(len(cleanDataList)):
    PostWarResponse = int(cleanDataList[i][23])
    if ((PostWarResponse >= 76)):
        PostWarSum = PostWarSum + 1
        if cleanDataList[i][4] == '1':
            PostWarTwitterSum = PostWarTwitterSum + 1
        if cleanDataList[i][5] == '1':
            PostWarInstagramSum = PostWarInstagramSum + 1
        if cleanDataList[i][6] == '1':
            PostWarFacebookSum = PostWarFacebookSum + 1
        if cleanDataList[i][7] == '1':
            PostWarSnapChatSum = PostWarSnapChatSum + 1
        if cleanDataList[i][8] == '1':
            PostWarYouTubeSum = PostWarYouTubeSum + 1
        if cleanDataList[i][9] == '1':
            PostWarWhatsAppSum = PostWarWhatsAppSum + 1
        if cleanDataList[i][10] == '1':
            PostWarPinterestSum = PostWarPinterestSum + 1
        if cleanDataList[i][11] == '1':
            PostWarLinkedinSum = PostWarLinkedinSum + 1
        if cleanDataList[i][12] == '1':
            PostWarRedditSum = PostWarRedditSum + 1
    else:
        continue

# Totals for this age group are presented here to the terminal
print("The number of users that are PostWar are: {}".format(PostWarSum))
print("The number of PostWar users that use Twitter: {}".format(PostWarTwitterSum))
print("The number of PostWar users that use Instagram: {}".format(PostWarInstagramSum))
print("The number of PostWar users that use Facebook: {}".format(PostWarFacebookSum))
print("The number of PostWar users that use Snapchat: {}".format(PostWarSnapChatSum))
print("The number of PostWar users that use YouTube: {}".format(PostWarYouTubeSum))
print("The number of PostWar users that use WhatsApp: {}".format(PostWarWhatsAppSum))
print("The number of PostWar users that use Pinterest: {}".format(PostWarPinterestSum))
print("The number of PostWar users that use Linkedin: {}".format(PostWarLinkedinSum))
print("The number of PostWar users that use Reddit: {}".format(PostWarRedditSum))
print("\n")

# Now let's determine the most popular social media for income level
# Create counters for each income category from the survey, and will
# total social media use for each income bracket to see which are used
# most, and if there is correlation between income and preferred social network

oneCounterTwitter = 0
oneCounterInstagram = 0
oneCounterFacebook = 0
oneCounterSnapchat = 0
oneCounterYoutube = 0
oneCounterWhatsapp = 0
oneCounterPinterest = 0
oneCounterLinkedin = 0
oneCounterReddit = 0

twoCounterTwitter = 0
twoCounterInstagram = 0
twoCounterFacebook = 0
twoCounterSnapchat = 0
twoCounterYoutube = 0
twoCounterWhatsapp = 0
twoCounterPinterest = 0
twoCounterLinkedin = 0
twoCounterReddit = 0

threeCounterTwitter = 0
threeCounterInstagram = 0
threeCounterFacebook = 0
threeCounterSnapchat = 0
threeCounterYoutube = 0
threeCounterWhatsapp = 0
threeCounterPinterest = 0
threeCounterLinkedin = 0
threeCounterReddit = 0

fourCounterTwitter = 0
fourCounterInstagram = 0
fourCounterFacebook = 0
fourCounterSnapchat = 0
fourCounterYoutube = 0
fourCounterWhatsapp = 0
fourCounterPinterest = 0
fourCounterLinkedin = 0
fourCounterReddit = 0

fiveCounterTwitter = 0
fiveCounterInstagram = 0
fiveCounterFacebook = 0
fiveCounterSnapchat = 0
fiveCounterYoutube = 0
fiveCounterWhatsapp = 0
fiveCounterPinterest = 0
fiveCounterLinkedin = 0
fiveCounterReddit = 0

sixCounterTwitter = 0
sixCounterInstagram = 0
sixCounterFacebook = 0
sixCounterSnapchat = 0
sixCounterYoutube = 0
sixCounterWhatsapp = 0
sixCounterPinterest = 0
sixCounterLinkedin = 0
sixCounterReddit = 0

sevenCounterTwitter = 0
sevenCounterInstagram = 0
sevenCounterFacebook = 0
sevenCounterSnapchat = 0
sevenCounterYoutube = 0
sevenCounterWhatsapp = 0
sevenCounterPinterest = 0
sevenCounterLinkedin = 0
sevenCounterReddit = 0

eightCounterTwitter = 0
eightCounterInstagram = 0
eightCounterFacebook = 0
eightCounterSnapchat = 0
eightCounterYoutube = 0
eightCounterWhatsapp = 0
eightCounterPinterest = 0
eightCounterLinkedin = 0
eightCounterReddit = 0

nineCounterTwitter = 0
nineCounterInstagram = 0
nineCounterFacebook = 0
nineCounterSnapchat = 0
nineCounterYoutube = 0
nineCounterWhatsapp = 0
nineCounterPinterest = 0
nineCounterLinkedin = 0
nineCounterReddit = 0

# Access data list, and intereted in looking at first income bracket - less than $10,000
for i in range(len(cleanDataList)):
    incomeResponse = cleanDataList[i][27]
    if incomeResponse == '1':
        if cleanDataList[i][4] == '1':
            oneCounterTwitter = oneCounterTwitter + 1
        if cleanDataList[i][5] == '1':
            oneCounterInstagram = oneCounterInstagram + 1
        if cleanDataList[i][6] == '1':
            oneCounterFacebook = oneCounterFacebook + 1
        if cleanDataList[i][7] == '1':
            oneCounterSnapchat = oneCounterSnapchat + 1
        if cleanDataList[i][8] == '1':
            oneCounterYoutube = oneCounterYoutube + 1
        if cleanDataList[i][9] == '1':
            oneCounterWhatsapp = oneCounterWhatsapp + 1
        if cleanDataList[i][10] == '1':
            oneCounterPinterest = oneCounterPinterest + 1
        if cleanDataList[i][11] == '1':
            oneCounterLinkedin = oneCounterLinkedin + 1
        if cleanDataList[i][12] == '1':
            oneCounterReddit = oneCounterReddit + 1
    # Access data list, and intereted in looking at second income bracket - $10K - $20K
    if incomeResponse == '2':
        if cleanDataList[i][4] == '1':
            twoCounterTwitter = twoCounterTwitter + 1
        if cleanDataList[i][5] == '1':
            twoCounterInstagram = twoCounterInstagram + 1
        if cleanDataList[i][6] == '1':
            twoCounterFacebook = twoCounterFacebook + 1
        if cleanDataList[i][7] == '1':
            twoCounterSnapchat = twoCounterSnapchat + 1
        if cleanDataList[i][8] == '1':
            twoCounterYoutube = twoCounterYoutube + 1
        if cleanDataList[i][9] == '1':
            twoCounterWhatsapp = twoCounterWhatsapp + 1
        if cleanDataList[i][10] == '1':
            twoCounterPinterest = twoCounterPinterest + 1
        if cleanDataList[i][11] == '1':
            twoCounterLinkedin = twoCounterLinkedin + 1
        if cleanDataList[i][12] == '1':
            twoCounterReddit = twoCounterReddit + 1
    # Access data list, and intereted in looking at third income bracket - $20K - $30K
    if incomeResponse == '3':
        if cleanDataList[i][4] == '1':
            threeCounterTwitter = threeCounterTwitter + 1
        if cleanDataList[i][5] == '1':
            threeCounterInstagram = threeCounterInstagram + 1
        if cleanDataList[i][6] == '1':
            threeCounterFacebook = threeCounterFacebook + 1
        if cleanDataList[i][7] == '1':
            threeCounterSnapchat = threeCounterSnapchat + 1
        if cleanDataList[i][8] == '1':
            threeCounterYoutube = threeCounterYoutube + 1
        if cleanDataList[i][9] == '1':
            threeCounterWhatsapp = threeCounterWhatsapp + 1
        if cleanDataList[i][10] == '1':
            threeCounterPinterest = threeCounterPinterest + 1
        if cleanDataList[i][11] == '1':
            threeCounterLinkedin = threeCounterLinkedin + 1
        if cleanDataList[i][12] == '1':
            threeCounterReddit = threeCounterReddit + 1
    # Access data list, and intereted in looking at fourth income bracket - $30K - $40K
    if incomeResponse == '4':
        if cleanDataList[i][4] == '1':
            fourCounterTwitter = fourCounterTwitter + 1
        if cleanDataList[i][5] == '1':
            fourCounterInstagram = fourCounterInstagram + 1
        if cleanDataList[i][6] == '1':
            fourCounterFacebook = fourCounterFacebook + 1
        if cleanDataList[i][7] == '1':
            fourCounterSnapchat = fourCounterSnapchat + 1
        if cleanDataList[i][8] == '1':
            fourCounterYoutube = fourCounterYoutube + 1
        if cleanDataList[i][9] == '1':
            fourCounterWhatsapp = fourCounterWhatsapp + 1
        if cleanDataList[i][10] == '1':
            fourCounterPinterest = fourCounterPinterest + 1
        if cleanDataList[i][11] == '1':
            fourCounterLinkedin = fourCounterLinkedin + 1
        if cleanDataList[i][12] == '1':
            fourCounterReddit = fourCounterReddit + 1
    # Access data list, and interested in looking at fifth income bracket - $40K - $50K
    if incomeResponse == '5':
        if cleanDataList[i][4] == '1':
            fiveCounterTwitter = fiveCounterTwitter + 1
        if cleanDataList[i][5] == '1':
            fiveCounterInstagram = fiveCounterInstagram + 1
        if cleanDataList[i][6] == '1':
            fiveCounterFacebook = fiveCounterFacebook + 1
        if cleanDataList[i][7] == '1':
            fiveCounterSnapchat = fiveCounterSnapchat + 1
        if cleanDataList[i][8] == '1':
            fiveCounterYoutube = fiveCounterYoutube + 1
        if cleanDataList[i][9] == '1':
            fiveCounterWhatsapp = fiveCounterWhatsapp + 1
        if cleanDataList[i][10] == '1':
            fiveCounterPinterest = fiveCounterPinterest + 1
        if cleanDataList[i][11] == '1':
            fiveCounterLinkedin = fiveCounterLinkedin + 1
        if cleanDataList[i][12] == '1':
            fiveCounterReddit = fiveCounterReddit + 1
    # Access data list, and interested in looking at sixth income bracket - $50K - $75K
    if incomeResponse == '6':
        if cleanDataList[i][4] == '1':
            sixCounterTwitter = sixCounterTwitter + 1
        if cleanDataList[i][5] == '1':
            sixCounterInstagram = sixCounterInstagram + 1
        if cleanDataList[i][6] == '1':
            sixCounterFacebook = sixCounterFacebook + 1
        if cleanDataList[i][7] == '1':
            sixCounterSnapchat = sixCounterSnapchat + 1
        if cleanDataList[i][8] == '1':
            sixCounterYoutube = sixCounterYoutube + 1
        if cleanDataList[i][9] == '1':
            sixCounterWhatsapp = sixCounterWhatsapp + 1
        if cleanDataList[i][10] == '1':
            sixCounterPinterest = sixCounterPinterest + 1
        if cleanDataList[i][11] == '1':
            sixCounterLinkedin = sixCounterLinkedin + 1
        if cleanDataList[i][12] == '1':
            sixCounterReddit = sixCounterReddit + 1
    # Access data list, and interested in looking at seventh income bracket - $75K - $100K
    if incomeResponse == '7':
        if cleanDataList[i][4] == '1':
            sevenCounterTwitter = sevenCounterTwitter + 1
        if cleanDataList[i][5] == '1':
            sevenCounterInstagram = sevenCounterInstagram + 1
        if cleanDataList[i][6] == '1':
            sevenCounterFacebook = sevenCounterFacebook + 1
        if cleanDataList[i][7] == '1':
            sevenCounterSnapchat = sevenCounterSnapchat + 1
        if cleanDataList[i][8] == '1':
            sevenCounterYoutube = sevenCounterYoutube + 1
        if cleanDataList[i][9] == '1':
            sevenCounterWhatsapp = sevenCounterWhatsapp + 1
        if cleanDataList[i][10] == '1':
            sevenCounterPinterest = sevenCounterPinterest + 1
        if cleanDataList[i][11] == '1':
            sevenCounterLinkedin = sevenCounterLinkedin + 1
        if cleanDataList[i][12] == '1':
            sevenCounterReddit = sevenCounterReddit + 1
    # Access data list, and interested in looking at eighth income bracket - $100K - $150K
    if incomeResponse == '8':
        if cleanDataList[i][4] == '1':
            eightCounterTwitter = eightCounterTwitter + 1
        if cleanDataList[i][5] == '1':
            eightCounterInstagram = eightCounterInstagram + 1
        if cleanDataList[i][6] == '1':
            eightCounterFacebook = eightCounterFacebook + 1
        if cleanDataList[i][7] == '1':
            eightCounterSnapchat = eightCounterSnapchat + 1
        if cleanDataList[i][8] == '1':
            eightCounterYoutube = eightCounterYoutube + 1
        if cleanDataList[i][9] == '1':
            eightCounterWhatsapp = eightCounterWhatsapp + 1
        if cleanDataList[i][10] == '1':
            eightCounterPinterest = eightCounterPinterest + 1
        if cleanDataList[i][11] == '1':
            eightCounterLinkedin = eightCounterLinkedin + 1
        if cleanDataList[i][12] == '1':
            eightCounterReddit = eightCounterReddit + 1
    # Access data list, and interested in looking at ninth income bracket - greater than $150k
    if incomeResponse == '9':
        if cleanDataList[i][4] == '1':
            nineCounterTwitter = nineCounterTwitter + 1
        if cleanDataList[i][5] == '1':
            nineCounterInstagram = nineCounterInstagram + 1
        if cleanDataList[i][6] == '1':
            nineCounterFacebook = nineCounterFacebook + 1
        if cleanDataList[i][7] == '1':
            nineCounterSnapchat = nineCounterSnapchat + 1
        if cleanDataList[i][8] == '1':
            nineCounterYoutube = nineCounterYoutube + 1
        if cleanDataList[i][9] == '1':
            nineCounterWhatsapp = nineCounterWhatsapp + 1
        if cleanDataList[i][10] == '1':
            nineCounterPinterest = nineCounterPinterest + 1
        if cleanDataList[i][11] == '1':
            nineCounterLinkedin = nineCounterLinkedin + 1
        if cleanDataList[i][12] == '1':
            nineCounterReddit = nineCounterReddit + 1

# Create lists of the totals for each income bracket
oneIncomeList = [oneCounterTwitter, oneCounterInstagram, oneCounterFacebook, oneCounterSnapchat, oneCounterYoutube, oneCounterWhatsapp, oneCounterPinterest, oneCounterLinkedin, oneCounterReddit]
twoIncomeList = [twoCounterTwitter, twoCounterInstagram, twoCounterFacebook, twoCounterSnapchat, twoCounterYoutube, twoCounterWhatsapp, twoCounterPinterest, twoCounterLinkedin, twoCounterReddit]
threeIncomeList = [threeCounterTwitter, threeCounterInstagram, threeCounterFacebook, threeCounterSnapchat, threeCounterYoutube, threeCounterWhatsapp, threeCounterPinterest, threeCounterLinkedin, threeCounterReddit]
fourIncomeList = [fourCounterTwitter, fourCounterInstagram, fourCounterFacebook, fourCounterSnapchat, fourCounterYoutube, fourCounterWhatsapp, fourCounterPinterest, fourCounterLinkedin, fourCounterReddit]
fiveIncomeList = [fiveCounterTwitter, fiveCounterInstagram, fiveCounterFacebook, fiveCounterSnapchat, fiveCounterYoutube, fiveCounterWhatsapp, fiveCounterPinterest, fiveCounterLinkedin, fiveCounterReddit]
sixIncomeList = [sixCounterTwitter, sixCounterInstagram, sixCounterFacebook, sixCounterSnapchat, sixCounterYoutube, sixCounterWhatsapp, sixCounterPinterest, sixCounterLinkedin, sixCounterReddit]
sevenIncomeList = [sevenCounterTwitter, sevenCounterInstagram, sevenCounterFacebook, sevenCounterSnapchat, sevenCounterYoutube, sevenCounterWhatsapp, sevenCounterPinterest, sevenCounterLinkedin, sevenCounterReddit]
eightIncomeList = [eightCounterTwitter, eightCounterInstagram, eightCounterFacebook, eightCounterSnapchat, eightCounterYoutube, eightCounterWhatsapp, eightCounterPinterest, eightCounterLinkedin, eightCounterReddit]
nineIncomeList = [nineCounterTwitter, nineCounterInstagram, nineCounterFacebook, nineCounterSnapchat, nineCounterYoutube, nineCounterWhatsapp, nineCounterPinterest, nineCounterLinkedin, nineCounterReddit]

# Create a list I will use periodically in the program for the order we are looking at social media networks
socialMediaMasterList = ['Twitter', 'Instagram', 'Facebook', 'Snapchat', 'Youtube', 'WhatsApp', 'Pinterest', 'LinkedIn', 'Reddit']

# Determine the most used social media network for each income bracket/income lists created above, and print out to the terminal
# this is done for each income bracket below.
oneIncomeListMaxVal = max(oneIncomeList)
oneIncomeMaxValIndex = oneIncomeList.index(oneIncomeListMaxVal)
print("The most used social media of the under $10,000 income demographic is: {}".format(socialMediaMasterList[oneIncomeMaxValIndex]))

twoIncomeListMaxVal = max(twoIncomeList)
twoIncomeMaxValIndex = twoIncomeList.index(twoIncomeListMaxVal)
print("The most used social media of the greater than $10,000 and under $20,000 income demographic is: {}".format(socialMediaMasterList[twoIncomeMaxValIndex]))

threeIncomeListMaxVal = max(threeIncomeList)
threeIncomeMaxValIndex = threeIncomeList.index(threeIncomeListMaxVal)
print("The most used social media of the greater than $20,000 and under $30,000 income demographic is: {}".format(socialMediaMasterList[threeIncomeMaxValIndex]))

fourIncomeListMaxVal = max(fourIncomeList)
fourIncomeMaxValIndex = fourIncomeList.index(fourIncomeListMaxVal)
print("The most used social media of the greater than $30,000 and under $40,000 income demographic is: {}".format(socialMediaMasterList[fourIncomeMaxValIndex]))

fiveIncomeListMaxVal = max(fiveIncomeList)
fiveIncomeMaxValIndex = fiveIncomeList.index(fiveIncomeListMaxVal)
print("The most used social media of the greater than $40,000 and under $50,000 income demographic is: {}".format(socialMediaMasterList[fiveIncomeMaxValIndex]))

sixIncomeListMaxVal = max(sixIncomeList)
sixIncomeMaxValIndex = sixIncomeList.index(sixIncomeListMaxVal)
print("The most used social media of the greater than $50,000 and under $75,000 income demographic is: {}".format(socialMediaMasterList[sixIncomeMaxValIndex]))

sevenIncomeListMaxVal = max(sevenIncomeList)
sevenIncomeMaxValIndex = sevenIncomeList.index(sevenIncomeListMaxVal)
print("The most used social media of the greater than $75,000 and under $100,000 income demographic is: {}".format(socialMediaMasterList[sevenIncomeMaxValIndex]))

eightIncomeListMaxVal = max(eightIncomeList)
eightIncomeMaxValIndex = eightIncomeList.index(eightIncomeListMaxVal)
print("The most used social media of the greater than $100,000 and under $150,000 income demographic is: {}".format(socialMediaMasterList[eightIncomeMaxValIndex]))

nineIncomeListMaxVal = max(nineIncomeList)
nineIncomeMaxValIndex = nineIncomeList.index(nineIncomeListMaxVal)
print("The most used social media of the greater than $150,000 income demographic is: {}".format(socialMediaMasterList[nineIncomeMaxValIndex]))
print("\n")

# Now let's determine the most popular social media for geography
# Instantiate counters for social media network tallys for each geographic region.
# Are some social media networks more popular in different geographies?

northEastCounterTwitter = 0
northEastCounterInstagram = 0
northEastCounterFacebook = 0
northEastCounterSnapchat = 0
northEastCounterYoutube = 0
northEastCounterWhatsapp = 0
northEastCounterPinterest = 0
northEastCounterLinkedin = 0
northEastCounterReddit = 0

midWestCounterTwitter = 0
midWestCounterInstagram = 0
midWestCounterFacebook = 0
midWestCounterSnapchat = 0
midWestCounterYoutube = 0
midWestCounterWhatsapp = 0
midWestCounterPinterest = 0
midWestCounterLinkedin = 0
midWestCounterReddit = 0

southCounterTwitter = 0
southCounterInstagram = 0
southCounterFacebook = 0
southCounterSnapchat = 0
southCounterYoutube = 0
southCounterWhatsapp = 0
southCounterPinterest = 0
southCounterLinkedin = 0
southCounterReddit = 0

westCounterTwitter = 0
westCounterInstagram = 0
westCounterFacebook = 0
westCounterSnapchat = 0
westCounterYoutube = 0
westCounterWhatsapp = 0
westCounterPinterest = 0
westCounterLinkedin = 0
westCounterReddit = 0

# First interested in looking at North East responders from the masterlist data.
# For each responder in each of the four geographihes, total up users of each social network.
for i in range(len(cleanDataList)):
    geographyResponse = cleanDataList[i][21]
    if geographyResponse == '1':
        if cleanDataList[i][4] == '1':
            northEastCounterTwitter = northEastCounterTwitter + 1
        if cleanDataList[i][5] == '1':
            northEastCounterInstagram = northEastCounterInstagram + 1
        if cleanDataList[i][6] == '1':
            northEastCounterFacebook = northEastCounterFacebook + 1
        if cleanDataList[i][7] == '1':
            northEastCounterSnapchat = northEastCounterSnapchat + 1
        if cleanDataList[i][8] == '1':
            northEastCounterYoutube = northEastCounterYoutube + 1
        if cleanDataList[i][9] == '1':
            northEastCounterWhatsapp = northEastCounterWhatsapp + 1
        if cleanDataList[i][10] == '1':
            northEastCounterPinterest = northEastCounterPinterest + 1
        if cleanDataList[i][11] == '1':
            northEastCounterLinkedin = northEastCounterLinkedin + 1
        if cleanDataList[i][12] == '1':
            northEastCounterReddit = northEastCounterReddit + 1
    if geographyResponse == '2':
        if cleanDataList[i][4] == '1':
            midWestCounterTwitter = midWestCounterTwitter + 1
        if cleanDataList[i][5] == '1':
            midWestCounterInstagram = midWestCounterInstagram + 1
        if cleanDataList[i][6] == '1':
            midWestCounterFacebook = midWestCounterFacebook + 1
        if cleanDataList[i][7] == '1':
            midWestCounterSnapchat = midWestCounterSnapchat + 1
        if cleanDataList[i][8] == '1':
            midWestCounterYoutube = midWestCounterYoutube + 1
        if cleanDataList[i][9] == '1':
            midWestCounterWhatsapp = midWestCounterWhatsapp + 1
        if cleanDataList[i][10] == '1':
            midWestCounterPinterest = midWestCounterPinterest + 1
        if cleanDataList[i][11] == '1':
            midWestCounterLinkedin = midWestCounterLinkedin + 1
        if cleanDataList[i][12] == '1':
            midWestCounterReddit = midWestCounterReddit + 1
    if geographyResponse == '3':
        if cleanDataList[i][4] == '1':
            southCounterTwitter = southCounterTwitter + 1
        if cleanDataList[i][5] == '1':
            southCounterInstagram = southCounterInstagram + 1
        if cleanDataList[i][6] == '1':
            southCounterFacebook = southCounterFacebook + 1
        if cleanDataList[i][7] == '1':
            southCounterSnapchat = southCounterSnapchat + 1
        if cleanDataList[i][8] == '1':
            southCounterYoutube = southCounterYoutube + 1
        if cleanDataList[i][9] == '1':
            southCounterWhatsapp = southCounterWhatsapp + 1
        if cleanDataList[i][10] == '1':
            southCounterPinterest = southCounterPinterest + 1
        if cleanDataList[i][11] == '1':
            southCounterLinkedin = southCounterLinkedin + 1
        if cleanDataList[i][12] == '1':
            southCounterReddit = southCounterReddit + 1
    if geographyResponse == '4':
        if cleanDataList[i][4] == '1':
            westCounterTwitter = westCounterTwitter + 1
        if cleanDataList[i][5] == '1':
            westCounterInstagram = westCounterInstagram + 1
        if cleanDataList[i][6] == '1':
            westCounterFacebook = westCounterFacebook + 1
        if cleanDataList[i][7] == '1':
            westCounterSnapchat = westCounterSnapchat + 1
        if cleanDataList[i][8] == '1':
            westCounterYoutube = westCounterYoutube + 1
        if cleanDataList[i][9] == '1':
            westCounterWhatsapp = westCounterWhatsapp + 1
        if cleanDataList[i][10] == '1':
            westCounterPinterest = westCounterPinterest + 1
        if cleanDataList[i][11] == '1':
            westCounterLinkedin = westCounterLinkedin + 1
        if cleanDataList[i][12] == '1':
            westCounterReddit = westCounterReddit + 1

# Create lists for each region with the totals for users of each network
northEastGeographyList = [northEastCounterTwitter, northEastCounterInstagram, northEastCounterFacebook, northEastCounterSnapchat, northEastCounterYoutube, northEastCounterWhatsapp, northEastCounterPinterest, northEastCounterLinkedin, northEastCounterReddit]
midWestGeographyList = [midWestCounterTwitter, midWestCounterInstagram, midWestCounterFacebook, midWestCounterSnapchat, midWestCounterYoutube, midWestCounterWhatsapp, midWestCounterPinterest, midWestCounterLinkedin, midWestCounterReddit]
southGeographyList = [southCounterTwitter, southCounterInstagram, southCounterFacebook, southCounterSnapchat, southCounterYoutube, southCounterWhatsapp, southCounterPinterest, southCounterLinkedin, southCounterReddit]
westGeographyList = [westCounterTwitter, westCounterInstagram, westCounterFacebook, westCounterSnapchat, westCounterYoutube, westCounterWhatsapp, westCounterPinterest, westCounterLinkedin, westCounterReddit]



# Determine the most used social medi and lease used social media from accessing above lists of total values
# This is printed out to the terminal for the user. This exercise is performed for each geographic region.
northEastGeogrphyListMaxVal = max(northEastGeographyList)
northEastGeographyListMaxValIndex = northEastGeographyList.index(northEastGeogrphyListMaxVal)
northEastGeogrphyListMinVal = min(northEastGeographyList)
northEastGeographyListMinValIndex = northEastGeographyList.index(northEastGeogrphyListMinVal)
print("The most used social media in the Northeast region: {}".format(socialMediaMasterList[northEastGeographyListMaxValIndex]))
print("The least used social media in the Northeast region: {}".format(socialMediaMasterList[northEastGeographyListMinValIndex]))
print("\n")


midWestGeographyListMaxVal = max(midWestGeographyList)
midWestGeographyListMaxValIndex = midWestGeographyList.index(midWestGeographyListMaxVal)
midWestGeographyListMinVal = min(midWestGeographyList)
midWestGeographyListMinValIndex = midWestGeographyList.index(midWestGeographyListMinVal)
print("The most used social media in the Midwest region: {}".format(socialMediaMasterList[midWestGeographyListMaxValIndex]))
print("The least used social media in the Midwest region: {}".format(socialMediaMasterList[midWestGeographyListMinValIndex]))
print("\n")


southGeographyListMaxVal = max(southGeographyList)
southGeographyListMaxValIndex = southGeographyList.index(southGeographyListMaxVal)
southGeographyListMinVal = min(southGeographyList)
southGeographyListMinValIndex = southGeographyList.index(southGeographyListMinVal)
print("The most used social media in the South region: {}".format(socialMediaMasterList[southGeographyListMaxValIndex]))
print("The least used social media in the South region: {}".format(socialMediaMasterList[southGeographyListMinValIndex]))
print("\n")


westGeographyListMaxVal = max(westGeographyList)
westGeographyListMaxValIndex = westGeographyList.index(westGeographyListMaxVal)
westGeographyListMinVal = min(westGeographyList)
westGeographyListMinValIndex = westGeographyList.index(westGeographyListMinVal)
print("The most used social media in the West region: {}".format(socialMediaMasterList[westGeographyListMaxValIndex]))
print("The least used social media in the West region: {}".format(socialMediaMasterList[westGeographyListMinValIndex]))
print("\n")

# Now let's determine the frequency of internet usage for age generations
# Look at generation z, by age range and determine internet usage for respondents.
# Total up responses for each participant and will present to terminal and a pie chart.
# gen z
genZConstantlySum = 0
genZSeveralDaySum = 0
genZOnceSum = 0
genZSeveralWeekSum = 0
genZLessOftenSum = 0
genZDontKnowSum = 0
genZRefusedSum = 0

for i in range(len(cleanDataList)):
    genZFreqResponse = int(cleanDataList[i][23])
    if genZFreqResponse <= 24:
        if cleanDataList[i][1] == '1':
            genZConstantlySum = genZConstantlySum + 1
        if cleanDataList[i][1] == '2':
            genZSeveralDaySum = genZSeveralDaySum + 1
        if cleanDataList[i][1] == '3':
            genZOnceSum = genZOnceSum + 1
        if cleanDataList[i][1] == '4':
            genZSeveralWeekSum = genZSeveralWeekSum + 1
        if cleanDataList[i][1] == '5':
            genZLessOftenSum = genZLessOftenSum + 1
        if cleanDataList[i][1] == '8':
            genZDontKnowSum = genZDontKnowSum + 1
        if cleanDataList[i][1] == '9':
            genZRefusedSum = genZRefusedSum + 1
    else:
        continue

# Now look at millenials in the same way, defining by age response.
# millenials
millenialsConstantlySum = 0
millenialsSeveralDaySum = 0
millenialsOnceSum = 0
millenialsSeveralWeekSum = 0
millenialsLessOftenSum = 0
millenialsDontKnowSum = 0
millenialsRefusedSum = 0

for i in range(len(cleanDataList)):
    millenialsFreqResponse = int(cleanDataList[i][23])
    if ((millenialsFreqResponse >= 25) and (millenialsFreqResponse <= 40)):
        if cleanDataList[i][1] == '1':
            millenialsConstantlySum = millenialsConstantlySum + 1
        if cleanDataList[i][1] == '2':
            millenialsSeveralDaySum = millenialsSeveralDaySum + 1
        if cleanDataList[i][1] == '3':
            millenialsOnceSum = millenialsOnceSum + 1
        if cleanDataList[i][1] == '4':
            millenialsSeveralWeekSum = millenialsSeveralWeekSum + 1
        if cleanDataList[i][1] == '5':
            millenialsLessOftenSum = millenialsLessOftenSum + 1
        if cleanDataList[i][1] == '8':
            millenialsDontKnowSum = millenialsDontKnowSum + 1
        if cleanDataList[i][1] == '9':
            millenialsRefusedSum = millenialsRefusedSum + 1
    else:
        continue

# Access generation X data and quantify responses on usage.
# genX
genXConstantlySum = 0
genXSeveralDaySum = 0
genXOnceSum = 0
genXSeveralWeekSum = 0
genXLessOftenSum = 0
genXDontKnowSum = 0
genXRefusedSum = 0

for i in range(len(cleanDataList)):
    genXFreqResponse = int(cleanDataList[i][23])
    if ((genXFreqResponse >= 41) and (genXFreqResponse <= 56)):
        if cleanDataList[i][1] == '1':
            genXConstantlySum = genXConstantlySum + 1
        if cleanDataList[i][1] == '2':
            genXSeveralDaySum = genXSeveralDaySum + 1
        if cleanDataList[i][1] == '3':
            genXOnceSum = genXOnceSum + 1
        if cleanDataList[i][1] == '4':
            genXSeveralWeekSum = genXSeveralWeekSum + 1
        if cleanDataList[i][1] == '5':
            genXLessOftenSum = genXLessOftenSum + 1
        if cleanDataList[i][1] == '8':
            genXDontKnowSum = genXDontKnowSum + 1
        if cleanDataList[i][1] == '9':
            genXRefusedSum = genXRefusedSum + 1
    else:
        continue

# Baby boomers totaled up based on age 57 and older and less than or equal to 75.
# Boomer
boomerConstantlySum = 0
boomerSeveralDaySum = 0
boomerOnceSum = 0
boomerSeveralWeekSum = 0
boomerLessOftenSum = 0
boomerDontKnowSum = 0
boomerRefusedSum = 0

for i in range(len(cleanDataList)):
    boomerFreqResponse = int(cleanDataList[i][23])
    if ((boomerFreqResponse >= 57) and (boomerFreqResponse <= 75)):
        if cleanDataList[i][1] == '1':
            boomerConstantlySum = boomerConstantlySum + 1
        if cleanDataList[i][1] == '2':
            boomerSeveralDaySum = boomerSeveralDaySum + 1
        if cleanDataList[i][1] == '3':
            boomerOnceSum = boomerOnceSum + 1
        if cleanDataList[i][1] == '4':
            boomerSeveralWeekSum = boomerSeveralWeekSum + 1
        if cleanDataList[i][1] == '5':
            boomerLessOftenSum = boomerLessOftenSum + 1
        if cleanDataList[i][1] == '8':
            boomerDontKnowSum = boomerDontKnowSum + 1
        if cleanDataList[i][1] == '9':
            boomerRefusedSum = boomerRefusedSum + 1
    else:
        continue


# Post war respondents are evaluated as well,and totals based on their frequency responses.
# PostWar
postWarConstantlySum = 0
postWarSeveralDaySum = 0
postWarOnceSum = 0
postWarSeveralWeekSum = 0
postWarLessOftenSum = 0
postWarDontKnowSum = 0
postWarRefusedSum = 0

for i in range(len(cleanDataList)):
    postWarFreqResponse = int(cleanDataList[i][23])
    if ((postWarFreqResponse >= 76)):
        if cleanDataList[i][1] == '1':
            postWarConstantlySum = postWarConstantlySum + 1
        if cleanDataList[i][1] == '2':
            postWarSeveralDaySum = postWarSeveralDaySum + 1
        if cleanDataList[i][1] == '3':
            postWarOnceSum = postWarOnceSum + 1
        if cleanDataList[i][1] == '4':
            postWarSeveralWeekSum = postWarSeveralWeekSum + 1
        if cleanDataList[i][1] == '5':
            postWarLessOftenSum = postWarLessOftenSum + 1
        if cleanDataList[i][1] == '8':
            postWarDontKnowSum = postWarDontKnowSum + 1
        if cleanDataList[i][1] == '9':
            postWarRefusedSum = postWarRefusedSum + 1
    else:
        continue

# For each generation, the findings totaled above are printed out to the terminal for the user.
print("Internet use frequency of Gen Z:")
print("Use almost constantly: {}".format(genZConstantlySum))
print("Use several times per day: {}".format(genZSeveralDaySum))
print("Use about once per week: {}".format(genZOnceSum))
print("Use several times per week: {}".format(genZSeveralWeekSum))
print("Use less often: {}".format(genZLessOftenSum))
print("Do not know: {}".format(genZDontKnowSum))
print("Refused to answer: {}".format(genZRefusedSum))
print("\n")


print("Internet use frequency of Millenials:")
print("Use almost constantly: {}".format(millenialsConstantlySum))
print("Use several times per day: {}".format(millenialsSeveralDaySum))
print("Use about once per week: {}".format(millenialsOnceSum))
print("Use several times per week: {}".format(millenialsSeveralWeekSum))
print("Use less often: {}".format(millenialsLessOftenSum))
print("Do not know: {}".format(millenialsDontKnowSum))
print("Refused to answer: {}".format(millenialsRefusedSum))
print("\n")


print("Internet use frequency of Gen X:")
print("Use almost constantly: {}".format(genXConstantlySum))
print("Use several times per day: {}".format(genXSeveralDaySum))
print("Use about once per week: {}".format(genXOnceSum))
print("Use several times per week: {}".format(genXSeveralWeekSum))
print("Use less often: {}".format(genXLessOftenSum))
print("Do not know: {}".format(genXDontKnowSum))
print("Refused to answer: {}".format(genXRefusedSum))
print("\n")


print("Internet use frequency of Boomers:")
print("Use almost constantly: {}".format(boomerConstantlySum))
print("Use several times per day: {}".format(boomerSeveralDaySum))
print("Use about once per week: {}".format(boomerOnceSum))
print("Use several times per week: {}".format(boomerSeveralWeekSum))
print("Use less often: {}".format(boomerLessOftenSum))
print("Do not know: {}".format(boomerDontKnowSum))
print("Refused to answer: {}".format(boomerRefusedSum))
print("\n")


print("Internet use frequency of Post War:")
print("Use almost constantly: {}".format(postWarConstantlySum))
print("Use several times per day: {}".format(postWarSeveralDaySum))
print("Use about once per week: {}".format(postWarOnceSum))
print("Use several times per week: {}".format(postWarSeveralDaySum))
print("Use less often: {}".format(postWarLessOftenSum))
print("Do not know: {}".format(postWarDontKnowSum))
print("Refused to answer: {}".format(postWarRefusedSum))
print("\n")

# Custom colors are chosen for my pie charts as they present the data clearly.
colors = ['#F9968B','#F27348','#26474E','#76CDCD', '#2CCED2', '#B8E0F6', '#A4CCE3','#37667E','#DEC4D6']

# Parameters for the pie charts are defined below for the matplotlib library.
OSN_names = ['Twitter', 'Instagram', 'Facebook', 'SnapChat', 'YouTube', 'Whats App', 'Pinterest', 'LinkedIn', 'Reddit']
OSN_numbers = [twitterSum, instagramSum, facebookSum, snapChatSum, youTubeSum, whatsAppSum, pinterestSum, linkedInSum, redditSum]
OSN2_names = ['Almost Constantly', 'Several Times per Day', 'About Once Per Day', 'Several Times Per Week', 'Less Often', 'Dont Know', 'Refused']
OSN2_numbers = [almostConstantlySum, severalTimesPerDaySum, aboutOncePerDaySum, severalTimesPerWeekSum, lessOftenSum, dontKnowSum, refusedSum]
OSN3_names = ['Twitter', 'Instagram', 'Facebook', 'SnapChat', 'YouTube', 'Whats App', 'Pinterest', 'LinkedIn', 'Reddit']
OSN3_numbers = [genZTwitterSum, genZInstagramSum, genZFacebookSum, genZSnapChatSum, genZYouTubeSum, genZWhatsAppSum, genZPinterestSum, genZLinkedinSum, genZRedditSum]
OSN4_names = ['Twitter', 'Instagram', 'Facebook', 'SnapChat', 'YouTube', 'Whats App', 'Pinterest', 'LinkedIn', 'Reddit']
OSN4_numbers = [millenialsTwitterSum, millenialsInstagramSum, millenialsFacebookSum, millenialsSnapChatSum, millenialsYouTubeSum, millenialsWhatsAppSum, millenialsPinterestSum, millenialsLinkedinSum, millenialsRedditSum]
OSN5_names = ['Twitter', 'Instagram', 'Facebook', 'SnapChat', 'YouTube', 'Whats App', 'Pinterest', 'LinkedIn', 'Reddit']
OSN5_numbers = [genXTwitterSum, genXInstagramSum, genXFacebookSum, genXSnapChatSum, genXYouTubeSum, genXWhatsAppSum, genXPinterestSum, genXLinkedinSum, genXRedditSum]
OSN6_names = ['Twitter', 'Instagram', 'Facebook', 'SnapChat', 'YouTube', 'Whats App', 'Pinterest', 'LinkedIn', 'Reddit']
OSN6_numbers = [BoomersTwitterSum, BoomersInstagramSum, BoomersFacebookSum, BoomersSnapChatSum, BoomersYouTubeSum, BoomersWhatsAppSum, BoomersPinterestSum, BoomersLinkedinSum, BoomersRedditSum]
OSN7_names = ['Twitter', 'Instagram', 'Facebook', 'SnapChat', 'YouTube', 'Whats App', 'Pinterest', 'LinkedIn', 'Reddit']
OSN7_numbers = [PostWarTwitterSum, PostWarInstagramSum, PostWarFacebookSum, PostWarSnapChatSum, PostWarYouTubeSum, PostWarWhatsAppSum, PostWarPinterestSum, PostWarLinkedinSum, PostWarRedditSum]
OSN8_names = ['Almost Constantly', 'Several Times Per Day', 'About Once per Week', 'Several Time per week', 'Less Often', 'Do Not Know', 'Refused']
OSN8_numbers = [genZConstantlySum, genZSeveralDaySum, genZOnceSum, genZSeveralWeekSum, genZLessOftenSum, genZDontKnowSum, genZRefusedSum]
OSN9_names = ['Almost Constantly', 'Several Times Per Day', 'About Once per Week', 'Several Time per week', 'Less Often', 'Do Not Know', 'Refused']
OSN9_numbers = [millenialsConstantlySum, millenialsSeveralDaySum, millenialsOnceSum, millenialsSeveralWeekSum, millenialsLessOftenSum, millenialsDontKnowSum, millenialsRefusedSum]
OSN10_names = ['Almost Constantly', 'Several Times Per Day', 'About Once per Week', 'Several Time per week', 'Less Often', 'Do Not Know', 'Refused']
OSN10_numbers = [genXConstantlySum, genXSeveralDaySum, genXOnceSum, genXSeveralWeekSum, genXLessOftenSum, genXDontKnowSum, genXRefusedSum]
OSN11_names = ['Almost Constantly', 'Several Times Per Day', 'About Once per Week', 'Several Time per week', 'Less Often', 'Do Not Know', 'Refused']
OSN11_numbers = [boomerConstantlySum, boomerSeveralDaySum, boomerOnceSum, boomerSeveralWeekSum, boomerLessOftenSum, boomerDontKnowSum, boomerRefusedSum]
OSN12_names = ['Almost Constantly', 'Several Times Per Day', 'About Once per Week', 'Several Time per week', 'Less Often', 'Do Not Know', 'Refused']
OSN12_numbers = [postWarConstantlySum, postWarSeveralDaySum, postWarOnceSum, postWarSeveralWeekSum, postWarLessOftenSum, postWarDontKnowSum, postWarRefusedSum]

# Parameter inputs for matplotlib
fig, axs = plt.subplots(3, 4)

# I am presenting multiple pie charts, so I have defined titles for each, and determined the position,size,etc on the output screen
axs[0,0].pie(OSN_numbers, labels = OSN_names, colors = colors, autopct='%1.0f%%', pctdistance=0.8, labeldistance=1.07)
axs[0,0].set_title('Overall Social Media Use')

axs[0,1].pie(OSN2_numbers,labels = OSN2_names, colors = colors, autopct='%1.0f%%', pctdistance=0.8, labeldistance=1.07)
axs[0,1].set_title('Overall Internet Use Frequency')

axs[0,2].pie(OSN3_numbers,labels = OSN3_names, colors = colors, autopct='%1.0f%%', pctdistance=0.8, labeldistance=1.07)
axs[0,2].set_title('Gen Z Social Media Use')

axs[0,3].pie(OSN4_numbers,labels = OSN4_names, colors = colors, autopct='%1.0f%%', pctdistance=0.8, labeldistance=1.07)
axs[0,3].set_title('Millenials Social Media Use')

axs[1,0].pie(OSN5_numbers,labels = OSN5_names, colors = colors, autopct='%1.0f%%', pctdistance=0.8, labeldistance=1.07)
axs[1,0].set_title('Gen X Social Media Use')

axs[1,1].pie(OSN6_numbers,labels = OSN6_names, colors = colors, autopct='%1.0f%%', pctdistance=0.8, labeldistance=1.07)
axs[1,1].set_title('Boomers Social Media Use')

axs[1,2].pie(OSN7_numbers,labels = OSN7_names, colors = colors, autopct='%1.0f%%', pctdistance=0.8, labeldistance=1.07)
axs[1,2].set_title('Post War Social Media Use')

axs[1,3].pie(OSN8_numbers,labels = OSN8_names, colors = colors, autopct='%1.0f%%', pctdistance=0.8, labeldistance=1.07)
axs[1,3].set_title('Gen Z Internet Use Frequency')

axs[2,0].pie(OSN9_numbers,labels = OSN9_names, colors = colors, autopct='%1.0f%%', pctdistance=0.8, labeldistance=1.07)
axs[2,0].set_title('Millenials Internet Use Frequency')

axs[2,1].pie(OSN10_numbers,labels = OSN10_names, colors = colors, autopct='%1.0f%%', pctdistance=0.8, labeldistance=1.07)
axs[2,1].set_title('Gen X Internet Use Frequency')

axs[2,2].pie(OSN11_numbers,labels = OSN11_names, colors = colors, autopct='%1.0f%%', pctdistance=0.8, labeldistance=1.07)
axs[2,2].set_title('Boomers Internet Use Frequency')

axs[2,3].pie(OSN12_numbers,labels = OSN12_names, colors = colors, autopct='%1.0f%%', pctdistance=0.8, labeldistance=1.07)
axs[2,3].set_title('Post War Internet Use Frequency')

# Present the plots to the screen for user of program
plt.show()
