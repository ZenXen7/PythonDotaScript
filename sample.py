import pyautogui

distance = 200
while distance > 0:
        pyautogui.drag(distance, 0, duration=0.5)  
        distance -= 5
        pyautogui.drag(0, distance, duration=0.5)   
        pyautogui.drag(-distance, 0, duration=0.5)  
        distance -= 5
        pyautogui.drag(0, -distance, duration=0.5)  