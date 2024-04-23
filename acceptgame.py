import pyautogui
import time

def click_accept_button(image_paths):
    try:
        print('Looking for button.')
        button_found = False
        while not button_found:
            for image_path in image_paths:
                accept_button_location = pyautogui.locateOnScreen('test2.png', minSearchTime=100000, confidence=0.7) # unsure about the min search time
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


image_paths = ['play.png', 'wtf.png', 'image3.png']  # trying to iterate images

click_accept_button(image_paths)
