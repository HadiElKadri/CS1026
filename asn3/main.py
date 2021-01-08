from sentiment_analysis import compute_tweets #importing function

#if a user enters a correct file
validFile = False

while not validFile:
    try:

#prompting the user to input desired files
        tweets = input("Please enter a file containing tweets: ")
        keywords = input("Please enter a file containing keywords: ")

        output = (compute_tweets(tweets, keywords)) #calling the function
#printing the results for each region
        print("\nFor the Eastern timezone, the average score of happiness is:", output[0][0])
        print("There were", output[0][1], "tweets counted. \n")
        print("For the Central timezone, the average score of happiness is:", output[1][0])
        print("There were", output[1][1], "tweets counted. \n")
        print("For the Mountain timezone, the average score of happiness is:", output[2][0])
        print("There were", output[2][1], "tweets counted. \n")
        print("For the Pacific timezone, the average score of happiness is:", output[3][0])
        print("There were", output[3][1], "tweets counted. \n")

#determining and printing which region is the happiest
        if output[0][0] > output[1][0] and output[0][0] > output[2][0] and output[0][0] > output[3][0]:
            print("The Eastern region is the happiest :D")
        elif output[1][0] > output[0][0] and output[1][0] > output[2][0] and output[1][0] > output[3][0]:
            print("The Central region is the happiest :D")
        elif output[2][0] > output[0][0] and output[2][0] > output[1][0] and output[2][0] > output[3][0]:
            print("The Mountain region is the happiest :D")
        elif output[3][0] > output[0][0] and output[3][0] > output[1][0] and output[3][0] > output[2][0]:
            print("The Pacific region is the happiest :D")

        if output != []:
            validFile = True
    except IndexError:
        print("You have entered an invalid file!")
        print("****************************************************")
