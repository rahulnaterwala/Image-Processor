# CMPT 120 Yet Another Image Processer
# Starter code for main.py
# Author(s):
# Date:
# Description:

import cmpt120imageProj
import cmpt120imageManip
import tkinter.filedialog
import pygame
pygame.init()

# list of system options
system = [
            "Q: Quit",
            "O: Open Image",
            "S: Save Image",
            "R: Reload Image"
         ]

# list of basic operation options
basic = [
          "1: Invert",
          "2: Flip Horizontal",
          "3: Flip Vertical",
          "4: Switch to Intermeidate Functions",
          "5: Switch to Advanced Functions"
         ]

# list of intermediate operation options
intermediate = [
                  "1: Remove Red Channel",
                  "2: Remove Green Channel",
                  "3: Remove Blue Channel",
                  "4: Convert to Grayscale",
                  "5: Apply Sepia Filter",
                  "6: Decrease Brightness",
                  "7: Increase Brightness",
                  "8: Switch to Basic Functions",
                  "9: Switch to Advanced Functions"
                 ]

# list of advanced operation options
advanced = [
                "1: Rotate Left",
                "2: Rotate Right",
                "3: Pixelate",
                "4: Binarize",
                "5: Switch to Basic Functions",
                "6: Switch to Intermediate Functions"
             ]

# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("") # an empty line
    menuString.append("Choose the following options:")
    menuString.append("") # an empty line
    menuString += system
    menuString.append("") # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")
        menuString.append("Enter your Choice (Q/O/S/R or 1-5)")
    elif state["mode"] == "intermediate":
        menuString.append("--Intermediate Mode--")
        menuString += intermediate
        menuString.append("")
        menuString.append("Enter your Choice (Q/O/S/R or 1-9)")
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")
        menuString.append("Enter your Choice (Q/O/S/R or 1-6)")
    else:
        menuString.append("Error: Unknown mode!")

    return menuString

# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary
#(e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
    """
        Input:  state - a dictionary containing the state values of the application
                img - the 2d array of RGB values to be operated on
        Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """
    userInput = state["lastUserInput"].upper()
    # handle the system functionalities
    if userInput.isalpha(): # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)
        if userInput == "Q": # this case actually won't happen, it's here as an example
            print("Log: Quitting...")
        # ***add the rest to handle other system functionalities***
        elif userInput == "O":
            tkinter.Tk().withdraw()
            openFilename = tkinter.filedialog.askopenfilename()
            img = cmpt120imageProj.getImage(openFilename)
            appStateValues["lastOpenFilename"] = openFilename
            cmpt120imageProj.showInterface(img, "Image", generateMenu(appStateValues))
        elif userInput == "S":
            tkinter.Tk().withdraw()
            saveFilename = tkinter.filedialog.asksaveasfilename()
            cmpt120imageProj.saveImage(img,saveFilename)
            appStateValues["lastSaveFilename"] = saveFilename
        elif userInput == "R":
            img = cmpt120imageProj.getImage(appStateValues["lastOpenFilename"])
            cmpt120imageProj.showInterface(img, "Image", generateMenu(appStateValues))
        else: # unrecognized user input
            print("Log: Unrecognized user input: " + userInput)

    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit(): # has to be a digit for manipulation options
        print("Log: Doing manipulation functionalities " + userInput)
        # ***add the rest to handle other manipulation functionalities***
        if appStateValues["mode"] == "basic":
            if userInput == "1":
                img = cmpt120imageManip.invertImage(img)
                cmpt120imageProj.showInterface(img, "Inverse", generateMenu(appStateValues))
            elif userInput == "2":
                img = cmpt120imageManip.flipHorizontal(img)
                cmpt120imageProj.showInterface(img, "Flip Horizontal", generateMenu(appStateValues))
            elif userInput == "3":
                img = cmpt120imageManip.flipVertical(img)
                cmpt120imageProj.showInterface(img, "Flip Vertical", generateMenu(appStateValues))
            elif userInput == "4":
                state["mode"] = "intermediate"
                cmpt120imageProj.showInterface(img, "Image", generateMenu(appStateValues))
            elif userInput == "5":
                state["mode"] = "advanced"
                cmpt120imageProj.showInterface(img, "Image", generateMenu(appStateValues))

        elif appStateValues["mode"] == "intermediate":
            if userInput == "1":
                img = cmpt120imageManip.removeRed(img)
                cmpt120imageProj.showInterface(img, "Remove Red", generateMenu(appStateValues))
            elif userInput == "2":
                img = cmpt120imageManip.removeGreen(img)
                cmpt120imageProj.showInterface(img, "Remove Green", generateMenu(appStateValues))
            elif userInput == "3":
                img = cmpt120imageManip.removeBlue(img)
                cmpt120imageProj.showInterface(img, "Remove Blue",
                generateMenu(appStateValues))
            elif userInput == "4":
                img = cmpt120imageManip.convertGrayscale(img)
                cmpt120imageProj.showInterface(img, "Convert to Grayscale",
                    generateMenu(appStateValues))
            elif userInput == "5":
                img = cmpt120imageManip.applySepia(img)
                cmpt120imageProj.showInterface(img, "Apply Sepia Filter",
                    generateMenu(appStateValues))
            elif userInput == "6":
                img = cmpt120imageManip.decreaseBrightness(img)
                cmpt120imageProj.showInterface(img, "Decrease Brightness",
                    generateMenu(appStateValues))
            elif userInput == "7":
                img = cmpt120imageManip.increaseBrightness(img)
                cmpt120imageProj.showInterface(img, "Increase Brightness",
                    generateMenu(appStateValues))
            elif userInput == "8":
                state["mode"] = "basic"
                cmpt120imageProj.showInterface(img, "Image", generateMenu(appStateValues))
            elif userInput == "9":
                state["mode"] = "advanced"
                cmpt120imageProj.showInterface(img, "Image", generateMenu(appStateValues))

        elif appStateValues["mode"] == "advanced":
            if userInput == "1":
                img = cmpt120imageManip.rotateLeft(img)
                cmpt120imageProj.showInterface(img, "Rotate Left", generateMenu(appStateValues))
            elif userInput == "2":
                img = cmpt120imageManip.rotateRight(img)
                cmpt120imageProj.showInterface(img, "Rotate Left", generateMenu(appStateValues))
            elif userInput == "3":
                img = cmpt120imageManip.pixelate(img)
                cmpt120imageProj.showInterface(img, "Pixelate", generateMenu(appStateValues))
            elif userInput == "4":
                img = cmpt120imageManip.binarize(img)
                cmpt120imageProj.showInterface(img, "Binarize", generateMenu(appStateValues))
            elif userInput == "5":
                state["mode"] = "basic"
                cmpt120imageProj.showInterface(img, "Image", generateMenu(appStateValues))
            elif userInput == "6":
                state["mode"] = "intermediate"
                cmpt120imageProj.showInterface(img, "Image", generateMenu(appStateValues))


    else: # unrecognized user input
            print("Log: Unrecognized user input: " + userInput)

    return img

# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }

currentImg = cmpt120imageProj.createBlackImage(600, 400) # create a default 600 x 400 black image
cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))
# note how it is used

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT:
            #another way to quit the program is to click the close botton
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")