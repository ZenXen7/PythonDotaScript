import pyautogui
import time

def click_accept_button(image_paths):
    try:
        print('Looking for button.')
        while True:
            for image_path in image_paths:
                accept_button_location = pyautogui.locateOnScreen('wtf.png', confidence=0.7)
                if accept_button_location is not None:
                    print("Button found!")
                    accept_button_center = pyautogui.center(accept_button_location)
                    pyautogui.click(accept_button_center)
                    print("Match accepted! Exiting....")
                    time.sleep(5)
                    exit()
            time.sleep(2)
    
    except pyautogui.ImageNotFoundException:
        print("Button not found. Retrying...")
        time.sleep(0.5)


image_paths = ['play.png', 'wtf.png', 'image3.png']  # working on iterating each image

click_accept_button(image_paths)
