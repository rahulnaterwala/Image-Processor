# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s):
# Date:
# Description:

import cmpt120imageProj
import numpy

# Basic Manipulations

def invertImage(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            pixel = img[x][y]
            r = 255 - pixel[0]
            g = 255 - pixel[1]
            b = 255 - pixel[2]
            img[x][y] = [r,g,b]

    return img

def flipHorizontal(img):
    #create a blank canvas to add inverted pixels too
    blankImg = cmpt120imageProj.createBlackImage(len(img),len(img[0]))
    #go through pixels and set them in reverse order horizontally
    for x in range(len(img)):
        for y in range(len(img[0])):
            blankImg[x][y] = img[(len(img)-1)-x][y]


    img = blankImg

    return img

def flipVertical(img):
    #create a blank canvas to add inverted pixels too
    blankImg = cmpt120imageProj.createBlackImage(len(img),len(img[0]))
    #go through pixels and set them in reverse order vertically
    for x in range(len(img)):
        for y in range(len(img[0])):
            blankImg[x][y] = img[x][(len(img[0])-1)-y]


    img = blankImg

    return img

# Intermediate Manipulations

def removeRed(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            pixel = img[x][y]
            # sets red value in pixel to 0
            img[x][y] = [pixel[0]*0,pixel[1],pixel[2]]

    return img

def removeGreen(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            pixel = img[x][y]
            # sets green value in pixel to 0
            img[x][y] = [pixel[0],pixel[1]*0,pixel[2]]

    return img

def removeBlue(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            pixel = img[x][y]
            # sets blue value in pixel to 0
            img[x][y] = [pixel[0],pixel[1],pixel[2]*0]

    return img

def convertGrayscale(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            pixel = img[x][y]
            # take the average of the rgb channels, then set it to the r,g,b positions
            pixelaverage = (pixel[0] + pixel[1] + pixel[2])/3
            img[x][y] = [pixelaverage,pixelaverage,pixelaverage]

    return img

def applySepia(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            pixel = img[x][y]
            # Apply the formula to convert each channel to sepia values
            SepiaRed = int(pixel[0]*0.393+pixel[1]*0.769+pixel[2]*0.189)
            SepiaGreen = int(pixel[0]*0.349+pixel[1]*0.686+pixel[2]*0.168)
            SepiaBlue = int(pixel[0]*0.272+pixel[1]*0.534+pixel[2]*0.131)
            # Check if values are greater than 255, if they are set them to 255
            if SepiaRed > 255:
                SepiaRed = 255
            if SepiaGreen > 255:
                SepiaGreen = 255
            if SepiaBlue > 255:
                SepiaBlue = 255
            # Set values to back to pixel
            img[x][y] = [SepiaRed,SepiaGreen,SepiaBlue]

    return img

def decreaseBrightness(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            pixel = img[x][y]
            # subtract 10 from every channel
            red = pixel[0]-10
            green = pixel[1]-10
            blue = pixel[2]-10
            # check if values are less than 0
            if red < 0:
                red = 0
            if green < 0:
                green = 0
            if blue < 0:
                blue = 0
            img[x][y] = [red,green,blue]

    return img

def increaseBrightness(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            pixel = img[x][y]
            # add 10 from every channel
            red = pixel[0]+10
            green = pixel[1]+10
            blue = pixel[2]+10
            # check if values are more than 255
            if red > 255:
                red = 255
            if green > 255:
                green = 255
            if blue > 255:
                blue = 255
            img[x][y] = [red,green,blue]

    return img

# Advanced Manipulations

def rotateLeft(img):

    # Create blank image with dimensions inverted
    blankImg = cmpt120imageProj.createBlackImage(len(img[0]),len(img))

    for x in range(len(img)):
        for y in range(len(img[0])):
            # Use same code from flip horizontal but map them to [y][x] instead of [x][y]
            # This is because we inverted dimensions on the blank image
            blankImg[y][x] = img[(len(img)-1)-x][y]

    img = blankImg

    return img

def rotateRight(img):

    # Create a blank image with dimensions inverted
    blankImg = cmpt120imageProj.createBlackImage(len(img[0]),len(img))

    for x in range(len(img)):
        for y in range(len(img[0])):
            # Use same code from flip vertical but map them to [y][x] instead of [x][y]
            # This is because we inverted dimensions on the blank image
            blankImg[y][x] = img[x][(len(img[0])-1)-y]

    img = blankImg

    return img

def pixelate(img):
    # Check if width is divisible by 4, if not
    # Checks what the remainder is, and then splices the list to remove it
    if len(img) % 4 == 1:
        img = img[:-1]
    elif len(img) % 4 == 2:
        img = img[:-2]
    elif len(img) % 4 == 3:
        img = img[:-3]

    # Initialize a counter to determine how many columns there are
    counter = 0
    for column in img:
        # Check if height is divisible by 4, if not
        # Checks what the remainder is, and then splices the list to remove it
        if len(column) % 4 == 1:
            z = img[counter]
            img[counter] = z[:-1]
        elif len(column) % 4 == 2:
            z = img[counter]
            img[counter] = z[:-2]
        elif len(column) % 4 == 3:
            z = img[counter]
            img[counter] = z[:-3]
        counter += 1
    # Create a set of for loops that iterates over every 4th pixel
    # This will be the top left of the 4x4 pixel
    for x in range(0,len(img),4):
        for y in range(0,len(img[0]),4):
            averagered = 0
            averagegreen = 0
            averageblue = 0
            for i in range(4):
                for j in range(4):
                    # A set of for loops that add the colour values of each channel in a 4x4 area
                    averagered += img[x+i][y+j][0]
                    averagegreen += img[x+i][y+j][1]
                    averageblue += img[x+i][y+j][2]
            # Find the average of each channel
            averagered = int(averagered/16)
            averagegreen = int(averagegreen/16)
            averageblue = int(averageblue/16)

            for k in range(4):
                for l in range(4):
                    # Reassign the average value to the 4x4 square
                    img[x+k][y+l] = [averagered,averagegreen,averageblue]

    return img

def binarize(img):
    img = convertGrayscale(img)
    initialthreshold = 0
    pixels = 0
    # Calculate initialthreshold
    for x in range(len(img)):
        for y in range(len(img[0])):
            initialthreshold += img[x][y][0]
            pixels += 1
    initialthreshold = initialthreshold // pixels
    # Setup the background and foreground to apply pixels to
    background = cmpt120imageProj.createBlackImage(len(img),len(img[0]))
    foreground = cmpt120imageProj.createBlackImage(len(img),len(img[0]))
    # Go through all pixels and set them to either foreground or background
    for i in range(len(img)):
        for j in range(len(img[0])):
            # If pixel is <= the initialthreshold, set it to background
            if img[i][j][0] <= initialthreshold:
                background[i][j] = img[i][j]
            # Else if image is > initialthreshold, set it to foreground
            elif img[i][j][0] > initialthreshold:
                foreground[i][j] = img[i][j]
    # Initialize variables for the while loop
    continue_bool = True
    backgroundaverage = 0
    foregroundaverage = 0
    threshold1 = initialthreshold
    threshold2 = 0

    while continue_bool:
        # Get averages for background and foreground
        for k in range(len(img)):
            for l in range(len(img[0])):
                backgroundaverage += background[k][l][0]
                foregroundaverage += foreground[k][l][0]
        backgroundaverage = backgroundaverage // pixels
        foregroundaverage = foregroundaverage // pixels
        # Calculate new threshold
        threshold2 = (backgroundaverage + foregroundaverage) // 2
        # conditionals to check whether to end loop or find new threshold
        if threshold1 - threshold2 <= 10:
            continue_bool = False
        else:
            threshold1 = threshold2
    # For loops to cycle through image and set values to either white or black
    # Depending on threshold
    for m in range(len(img)):
        for n in range(len(img[0])):
            if img[m][n][0] <= threshold2:
                img[m][n] = [0,0,0]
            elif img[m][n][0] > threshold2:
                img[m][n] = [255,255,255]


    return img