import pyautogui
import keyboard
import time

def main():
    while True:
        pyautogui.typewrite("Nigger")
        pyautogui.hotkey("enter")
        
        if keyboard.is_pressed('x'):
            break

if __name__ == "__main__":
    main()

