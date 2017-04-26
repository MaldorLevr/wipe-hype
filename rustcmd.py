import pyautogui

def send_command(command):
    pyautogui.press('f1')
    pyautogui.typewrite(command)
    pyautogui.press('enter')
    pyautogui.press('f1')

# def find_in_log(text):
#     f = open("")