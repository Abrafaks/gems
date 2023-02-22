import keyboard
import mss
import cv2
import numpy
from time import time, sleep
import pyautogui

def get_screen():
    sct = mss.mss()
    screen = numpy.array(sct.grab(dimensions))
    return screen[:,:,:3]


def match_template(img):
    scr_remove = get_screen()
    result = cv2.matchTemplate(scr_remove, img, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    print(f"Max Val: {max_val} Max Loc: {max_loc}")
    if max_val > .95:
        w = img.shape[1]
        h = img.shape[0]
        x,y = max_loc
        pyautogui.click(x=(x+w/2), y=(y+h/2))
        # paint square on the image
        # cv2.rectangle(screen, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)
        # cv2.imshow('Result', screen)
        # cv2.waitKey()
        # cv2.destroyAllWindows()
        return True

    return False


dimensions = {
        'left': 0,
        'top': 0,
        'width': 3840,
        'height': 2160
    }

pyautogui.PAUSE = 0

print("Press 's' to start playing.")
print("Once started press 'q' to quit.")
keyboard.wait('s')

autoPlay = cv2.imread('autoPlay.png')
continueGame = cv2.imread('continue.png')
continueGame2 = cv2.imread('continue2.png')
difficulty = cv2.imread('difficulty.png')
dropdown = cv2.imread('dropdown.png')
explore = cv2.imread('explore.png')
toBattle = cv2.imread('toBattle.png')
okay = cv2.imread('okay.png')
bosschest = cv2.imread('bosschest.png')
miniboss = cv2.imread('miniboss.png')
mythicboss = cv2.imread('mythicboss.png')

while True:

    choseDifficulty = match_template(difficulty)
    sleep(.33)
    choseContinue = match_template(continueGame)
    choseContinue2 = match_template(continueGame2)
    clickExplore = match_template(explore)
    clickToBattle = match_template(toBattle)
    clickDropdown = match_template(dropdown)
    clickAutoPlay = match_template(autoPlay)
    clickOkay = match_template(okay)
    clickBosschest = match_template(bosschest)
    clickMiniboss = match_template(miniboss)
    clickMythicboss = match_template(mythicboss)



    if keyboard.is_pressed('q'):
        break

