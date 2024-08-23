import pyautogui



def start_game():
    print('Starting game..')
    image_path = 'wtf.png'
    try:
        location = pyautogui.locateOnScreen(image_path, confidence=0.7)
        if location is not None:
            print('Starting game')
            center = pyautogui.center(location)
            pyautogui.doubleClick(center)
        else:
            print('Failed')
    except Exception as e:
        print(f'An error occured: {e}')
        

start_game()

