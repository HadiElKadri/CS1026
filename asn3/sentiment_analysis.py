####### AUTHOR : HADI EL-KADRI ###########
#### THIS PROGRAM WILL TAKE TWEETS FROM 4 DIFFERENT REGIONS AND ANALYSE THEM####
###KEYWORDS WITH SENTIMENT VALUES WILL BE USED TO DETERMINE THE HAPPINESS SCORE OF EACH REGION BASED ON THE TWEETS###

#the complete function that analyzes the tweets and computes the average happiness score
def compute_tweets(tweets, keywords):

#define my lists
    keywordsList = []
    valueList = []
    tweetList = []
    latitudeList = []
    longitudeList = []
    newTweetList = []
    newLatitudeList = []
    newLongitudeList = []
    sentTotalsWithZERO= []
    sentTotalsWithoutZERO= []
    resultTotals = []

#CONSTANTS
    LATITUDE1 = 24.660845
    LATITUDE2 = 49.189787
    LONG1 = -125.242264
    LONG2 = -115.236428
    LONG3 = -101.998892
    LONG4 = -87.518395
    LONG5 = -67.444574

#opening the files for reading
    try:
        readKeywords = open(keywords,"r",encoding="utf‐8")
        readTweets = open(tweets,"r", encoding="utf-8")

#putting the keywords into a list and the sentiment values into a list
        for line in readKeywords:
            keywordsread = line.split(",") #splitting the KEYWORDS by the comma
            keywordsread[1] = keywordsread[1].strip() #stripping the new line function
            keywordsList.append(keywordsread[0]) #making 2 lists, 1 for the keyword
            valueList.append(int(keywordsread[1])) #1 for its value resepectively

#splitting the tweets into 3 lists, latitude, longitude, and the whole tweet, REMOVING UNECESSARY PUNCTUATION
        for line in readTweets:
            tweetsread= line.split(" ", 5) #splitting the TWEETS by its spaces
            tweetsread[5] = tweetsread[5].strip() #removing the \n function
            tweetList.append(removePunctuationTweet(tweetsread[5]).lower()) #making a list of each tweet
            latitudeList.append(removePunctuationLocation(tweetsread[0])) #making a list of latitudes
            longitudeList.append(removePunctuationLocation(tweetsread[1])) #making a list of longitutdes

#splitting each tweet into a list of words and identifying the total keywords and happiness score in each tweet
        for i in range(len(tweetList)):
            tweetsAsList = tweetList[i].split()
            valueofSentiment = 0
            keyCount= 0
            for j in range(len(keywordsList)):
                for k in range(len(tweetsAsList)):
                    if keywordsList[j] == tweetsAsList[k]:
                        keyCount = keyCount + 1
                        valueofSentiment = valueofSentiment + valueList[j]

#finding the average score by taking the score and dividing by the number of keywords
            try:
                valueofSentiment = valueofSentiment / keyCount

            except ZeroDivisionError:
                valueofSentiment = valueofSentiment

            sentTotalsWithZERO.append(valueofSentiment) #making a list of the sentiment scores including scores of 0

#MAKING NEW LISTS APPENDING ALL TWEETS THAT DO CONTAIN KEYWORDS ALONG WITH THEIR LATITUDES, LONGITUDES, AND VALUES

        for i in range(len(sentTotalsWithZERO)):
            if (sentTotalsWithZERO[i]) != 0:
                sentTotalsWithoutZERO.append(sentTotalsWithZERO[i]) #new list of sentiment scores exluding those with score of 0(have no keywords)
                newTweetList.append(tweetList[i]) #new list of tweets who DO contain keywords
                newLatitudeList.append(latitudeList[i]) #new list of latitudes that correspond with tweets that do contain keywords
                newLongitudeList.append(longitudeList[i]) #new list of longitudes that correspond with tweets that do contain keywords
            eCount = 0
            cCount = 0
            mCount = 0
            pCount = 0
            eHappiness = 0
            cHappiness = 0
            mHappiness = 0
            pHappiness = 0

#calculating the happiness score and tweet count IF they are in the regions
        for i in range(len(newLatitudeList)):

            if LATITUDE1 <= float(newLatitudeList[i]) <= LATITUDE2:
                if LONG1 <= float(newLongitudeList[i]) <= LONG2:
                    pCount = pCount + 1
                    pHappiness = pHappiness + sentTotalsWithoutZERO[i]
                elif LONG2 <= float(newLongitudeList[i]) <= LONG3:
                    mCount = mCount + 1
                    mHappiness = mHappiness + sentTotalsWithoutZERO[i]
                elif LONG3 <= float(newLongitudeList[i]) <= LONG4:
                    cCount = cCount + 1
                    cHappiness = cHappiness + sentTotalsWithoutZERO[i]
                elif LONG4 <= float(newLongitudeList[i]) <= LONG5:
                    eCount = eCount + 1
                    eHappiness = eHappiness + sentTotalsWithoutZERO[i]

#if there are no tweets in a region
        try:
            eHappiness = eHappiness / eCount
        except ZeroDivisionError:
            eHappiness = eHappiness
        try:
            cHappiness = cHappiness / cCount
        except ZeroDivisionError:
            cHappiness = cHappiness
        try:
            mHappiness = mHappiness /mCount
        except ZeroDivisionError:
            mHappiness = mHappiness
        try:
            pHappiness = pHappiness / pCount
        except ZeroDivisionError:
            pHappiness = pHappiness

#creating tuples for each region
        easternR = round(eHappiness, 3), eCount
        centralR = round(cHappiness, 3), cCount
        mountainR = round(mHappiness, 3), mCount
        pacificR = round(pHappiness, 3), pCount

#making a list of all the tuples
        resultTotals.append(easternR)
        resultTotals.append(centralR)
        resultTotals.append(mountainR)
        resultTotals.append(pacificR)

#results if an incorrect file is entered
    except IOError:
        resultTotals = []
    except ValueError:
        resultTotals = []
    except RuntimeError:
        resultTotals = []
    return(resultTotals)


#FUNCTION TO REMOVE PUNCT FROM TWEETS
def removePunctuationTweet(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for i in range(0,len(string)):
       if string[i] not in punctuations:
        no_punct = no_punct + string[i]
    return no_punct

#FUNCTION TO REMOVE PUNCT FROM LATS AND LONGS
def removePunctuationLocation(locationValue):
    punctuations = ',[]'
    no_punct = ""
    for i in range(0,len(locationValue)):
       if locationValue[i] not in punctuations:
        no_punct = no_punct + locationValue[i]
    return no_punct
