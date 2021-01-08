#####AUTHOR: HADI EL-KADRI#####
# THIS PROGRAM WILL PROMPT THE USER TO CHOOSE A SHAPE (EITHER CUBE, PYRAMID, OR ELLIPSOID)
##IT WILL THEN ASK FOR DESIRED DIMENISIONS OF THE SHAPE
###IT WILL CALCULATE THE VOLUME OF THE SHAPE AND SAVE IT INTO A LIST ASSOCIATED WITH EACH SHAPE
#### THE VOLUME CALCULATED WILL BE DISPLAYED, AND THE PROGRAM WILL KEEP PROMPTING FOR SHAPES UNTIL THE USER QUITS
##### WHEN THE USER IS FINISHED, THE PROGRAM WILL DISPLAY A LIST OF VOLUMES CALCULATED ASSOCIATED WITH EACH SHAPE

#IMPORTING FUNCTIONS FROM THE VOLUME MODULE

from volumes import *

#CREATING THE LISTS TO CONTAIN THE VOLUMES CALCULATED

cubeList = []
pyramidList = []
ellipsoidList = []

#PROMPTING THE USER TO ENTER A DESIRED SHAPE
print("This program will calculate the volume of a cube, pyramid, or ellipsoid!")
userInput = input("\nPlease enter a desired shape: ")
userInput = userInput.lower()

#IF THE USER QUITS RIGHT AWAY
if userInput == 'q' or userInput == 'quit':
    print("You have reached the end of your session \nYou did not preform any volume calculations.")
    exit()

#IF THE USER HAS INPUT A VALUE THAT IS NOT Q THIS LOOP WILL RUN
else:
    while userInput.lower() != 'q' or userInput.lower() != 'quit':

        #IF THE USER HAS ENTERED A VALUE OTHER THAN THE REQUIRED VALUES IT WILL PROMPT TO THE USER TO TRY AGAIN
        if userInput not in ('c', 'cube','p', 'pyramid', 'e', 'ellipsoid', 'quit', 'q'):
            print("You have entered an invalid input.")
            userInput = input("\nPlease enter a desired shape: ")
            userInput = userInput.lower()

        #IF THE USER CHOSE A CUBE, THE CUBE VOLUME IS CALCULATED AND PUT INTO THE CUBE LIST, ANOTHER SHAPE IS ASKED FOR AFTER
        #CUBE LIST IS ALSO SORTED
        elif userInput == 'c' or userInput == 'cube':
            volCube = cubeVolume()
            cubeList.append(volCube)
            cubeList.sort()
            userInput = input("\nPlease enter a desired shape: ")
            userInput = userInput.lower()

        #IF THE USER CHOSE A PYRAMID, THE PYRAMID VOLUME IS CALCULATED AND PUT INTO THE PYRAMID LIST, ANOTHER SHAPE IS ASKED FOR AFTER
        #PYRAMID LIST IS ALSO SORTED
        elif userInput == 'p' or userInput == 'pyramid':
            volPyr = pyramidVolume()
            pyramidList.append(volPyr)
            pyramidList.sort()
            userInput = input("\nPlease enter a desired shape: ")
            userInput = userInput.lower()

        #IF THE USER CHOSE AN ELLIPSOID, THE ELLIPSOID VOLUME IS CALCULATED AND PUT INTO THE ELLISPOID LIST, ANOTHER SHAPE IS ASKED FOR AFTER
        #ELLIPSOID LIST IS ALSO SORTED
        elif userInput == 'e' or userInput == 'ellipsoid':
            volEllipsoid = elipsoidVolume()
            ellipsoidList.append(volEllipsoid)
            ellipsoidList.sort()
            userInput = input("\nPlease enter a desired shape: ")
            userInput = userInput.lower()

        #WHEN THE USER QUITS, THEY HAVE REACHED THE END OF THEIR SESSION
        #BRACKETS ARE TAKEN OFF OF THE LISTS
        elif userInput == 'q' or userInput == 'quit':
            print("\nYou have reached the end of your session.")
            cubeList = ", ".join(map(str, cubeList))
            pyramidList = ", ".join(map(str, pyramidList))
            ellipsoidList = ", ".join(map(str, ellipsoidList))

            #IF THE USER HAS NOT INPUT ANY SHAPES
            if len(cubeList) == 0 and len(pyramidList) == 0 and len(ellipsoidList) == 0:
                print("No volume calculations were made.") + exit()
            #IF THE USER INPUT ALL THE SHAPES
            elif len(cubeList) != 0 and len(pyramidList) != 0 and len(ellipsoidList) != 0:
                print("The volumes calculated for each shape are: \nCube:", cubeList, "\nPyramid:", pyramidList, "\nEllipsoid:", ellipsoidList) + exit()
            #IF THE USER INPUT PYRAMIDS AND ELLIPSOIDS BUT NOT CUBES
            elif len(cubeList) == 0 and len(pyramidList) != 0 and len(ellipsoidList) != 0:
                print("The volumes calculated for each shape are: \nCube: No shapes entered. \nPyramid:", pyramidList, "\nEllipsoid:", ellipsoidList) + exit()
            #IF THE USER INPUT CUBES AND PYRAMIDS BUT NOT ELLIPSOIDS
            elif len(cubeList) != 0 and len(pyramidList) != 0 and len(ellipsoidList) == 0:
                print("The volumes calculated for each shape are: \nCube:", cubeList, "\nPyramid:", pyramidList, "\nEllipsoid: No shapes entered.") + exit()
            #IF THE USER INPUT CUBES AND ELLIPSOIDS BUT NOT PYRAMIDS
            elif len(pyramidList) == 0 and len(cubeList) != 0 and len(ellipsoidList) != 0:
                print("The volumes calculated for each shape are: \nCube:", cubeList, "\nPyramid: No shapes entered. \nEllipsoid:", ellipsoidList) + exit()
            #IF THE USER ONLY INPUT ELLIPSOIDS
            elif len(cubeList) == 0 and len(pyramidList) == 0 and len(ellipsoidList) != 0:
                print("The volumes calculated for each shape are: \nCube: No shapes entered. \nPyramid: No shapes entered. \nEllipsoid:", ellipsoidList) + exit()
            #IF THE USER ONLY INPUT PYRAMIDS
            elif len(cubeList) == 0 and len(pyramidList) != 0 and len(ellipsoidList) == 0:
                print("The volumes calculated for each shape are: \nCube: No shapes entered. \nPyramid:", pyramidList, "\nEllipsoid: No shapes entered.") + exit()
            #IF THE USER ONLY INPUT CUBES
            elif len(cubeList) != 0 and len(pyramidList) == 0 and len(ellipsoidList) == 0:
                print("The volumes calculated for each shape are: \nCube:", cubeList, "\nPyramid: No shapes entered. \nEllipsoid: No shapes entered.") + exit()
