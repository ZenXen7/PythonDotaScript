import pyautogui
import time

global button_found
global hero_found

def click_accept_button(image_paths):
    global button_found
    try:
        print('Looking for button.')
        button_found = False
        while not button_found:
            for image_path in image_paths:
                accept_button_location = pyautogui.locateOnScreen('test2.png', minSearchTime=100000, confidence=0.7)
                if accept_button_location is not None:
                    print("Button found!")
                    accept_button_center = pyautogui.center(accept_button_location)
                    pyautogui.click(accept_button_center)
                    print("Match accepted! Exiting....")
                    button_found = True
                    break  
            if not button_found:
                print("Button not found. Retrying...")
                time.sleep(2)

    except pyautogui.ImageNotFoundException:
        print("Button not found. Retrying...")
        time.sleep(2)

def find_hero():
    hero_found = False       
    try:
        if button_found is True:
          print('Looking for hero.')
          hero_found = False
          while not hero_found:
            if button_found is True:
                print('Picking Phantom Assassin')
                pick_hero_location = pyautogui.locateOnScreen('PA.png', minSearchTime=100000, confidence=0.7)
                if pick_hero_location is not None:
                    print('Hero found!')
                    pick_hero_center = pyautogui.center(pick_hero_location)
                    pyautogui.click(pick_hero_center)
                    print("PA Picked")
                    hero_found = True
                    
    except pyautogui.ImageNotFoundException:
        print("Hero not found. Retrying...")
        time.sleep(2)

def pick_hero():
    try:
        if hero_found is True:
            print('Picking hero..')
            hero_picked = False
            while not hero_picked:
                print('Selecting hero')
                lock_hero_location = pyautogui.locateOnScreen('PA.png', minSearchTime=10000, confidence=0.7)
                if lock_hero_location is not None:
                    print('Hero locked')
                    lock_hero_center = pyautogui.center(lock_hero_location)
                    pyautogui.click(lock_hero_center)
                    print("Done")
                    hero_picked = True
    except pyautogui.ImageNotFoundException:
        print("Hero not picked. Retrying... ")
        time.sleep(2)
        
    
    


image_paths = ['play.png', 'wtf.png', 'test2.png']  # trying to iterate images

# click_accept_button(image_paths)
find_hero()
