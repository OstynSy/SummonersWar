import time
import pyautogui
import random
import cv2

def rand_coord_click(coord):
    var = 50
    x, y = coord
    randx = random.randrange(x - var, x + var)
    randy = random.randrange(y - var, y + var)
    pyautogui.click(randx, randy)

def start():
    print("begin-start")
    coord = pyautogui.locateCenterOnScreen("3start.png", grayscale=True, confidence=.5)
    rand_coord_click(coord)
    time.sleep(1)
    print("end-start")


def start_auto():
    print("begin-startauto")
    coord = pyautogui.locateCenterOnScreen("startauto.png", grayscale=True)
    rand_coord_click(coord)
    print("end-startauto")


def reward():
    print("begin-reward")
    found = False
    while found is False:
        coord = pyautogui.locateCenterOnScreen("reward.png", grayscale=True)
        if coord is not None:
            rand_coord_click(coord)
            found = True
    secs = random.randrange(1, 2)
    time.sleep(secs)
    print("end-reward")


def victory():
    print("begin-victory")
    coord = pyautogui.locateCenterOnScreen("victory.png", grayscale=True)
    rand_coord_click(coord)
    secs = random.randrange(1, 2)
    time.sleep(secs)
    print("end-victory")


def ok():
    print("begin-ok")
    coord = pyautogui.locateCenterOnScreen("ok.png", grayscale=True)
    rand_coord_click(coord)
    secs = random.randrange(1, 2)
    time.sleep(secs)
    print("end-ok")


def next_stage():
    print("begin-nextstage")
    coord = pyautogui.locateCenterOnScreen("nextstage.png", grayscale=True)
    rand_coord_click(coord)
    secs = random.randrange(1, 2)
    time.sleep(secs)
    print("end-nextstage")


def main():
    cont = True
    while cont is True:
        start()
        reward()
        victory()
        ok()
        next_stage()


if __name__ == "__main__":
    main()