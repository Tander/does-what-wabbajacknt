from time import sleep

import pyautogui
from pyscreeze import Box

pyautogui.FAILSAFE = True
print(f'Screen size: {pyautogui.size()}')
counter = 0

def look_for_button() -> bool:
    try:
        btn: Box = pyautogui.locateOnScreen('download.png')
        print(f'{counter + 1} buttons!')
    except pyautogui.ImageNotFoundException:
        return False

    button_x = btn.left + (btn.width / 2)
    button_y = btn.top + (btn.height / 2)

    pyautogui.click(x=button_x, y=button_y, clicks=1, button='left')
    pyautogui.moveTo(button_x, 10)
    return True

while True:
    result = look_for_button()
    counter += int(result)
    if counter > 600:
        raise StopIteration(f'Too much buttons, probably a failure')
    sleep(3)
