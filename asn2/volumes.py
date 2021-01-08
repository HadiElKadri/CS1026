# AUTHOR: HADI EL-KADRI #
#THIS PROGRAM PROMPTS THE USER TO ENTER VALUES ASSOCIATED WITH THE SELECTED SHAPE
#THE CALCULATIONS ARE MADE BASED UPON THE VALUES ENTERED, AND THE FINAL VOLUME WILL BE RETURNED

#FROM MATH, PI WAS IMPORTED FOR ELLIPSOID CALCULATION
import math

#THIS FUNCTION WILL CALCULATE THE VOLUME OF A CUBE BASED ON AN INPUTTED VALUE, PRINT THE VOLUME, AND RETURN IT
def cubeVolume():
    sidelength = float(input("Please input a side length: "))
    volume = sidelength ** 3
    volume = round(volume, 3)
    print("A cube with side length {} has the volume {}" .format(sidelength, volume))
    return volume

#THIS FUNCTION WILL CALCULATE THE VOLUME OF A PYRAMID BASED ON INPUTTED VALUES, PRINT THE VOLUME, AND RETURN IT
def pyramidVolume ():
    b = float(input("Please enter a base length: "))
    h = float(input("Please enter a height length: "))
    volume = ((b**2) * h) / 3
    volume = round(volume, 3)
    print("A pyramid with base {} and height {} has the volume {}" .format(b, h, volume))
    return volume

#THIS FUNCTION WILL CALCULATE THE VOLUME OF AN ELLIPSOID BASED ON INPUTTED VALUES, PRINT THE VOLUME, AND RETURN IT
def elipsoidVolume ():
    r1 = float(input("Please enter the first radius: "))
    r2 = float(input("Please enter the second radius: "))
    r3 = float(input("Please enter the third radius: "))
    volume = (4 * math.pi * r1 * r2 *r3) / 3
    volume = round(volume, 3)
    print("An ellipsoid with radii {}, {}, and {}, has the volume {}" .format(r1, r2, r3, volume))
    return volume
