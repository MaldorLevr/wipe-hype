import pyautogui
import settings
import time

def send_command(command):
    pyautogui.press('f1')
    pyautogui.typewrite(command)
    pyautogui.press('enter')
    pyautogui.press('f1')

def find_in_log(text):
    f = open(settings.rust_log_path, 'r', encoding='utf-8')
    for line in f:
        if text in line:
            return True
    return False

def send_command_and_await_response(command, response, timeout=60):
    # TODO: merge this function with wait_for_log
    f = open(settings.rust_log_path, 'r', encoding='utf-8')
    f.seek(0, 2)
    send_command(command)
    i = 0
    while True:
        if i >= timeout/0.1:
            return False
        line = f.readline()
        if response in line:
            return True
        if not line:
            time.sleep(0.1)
            i += 1

def wait_for_log(text, timeout=60):
    f = open(settings.rust_log_path, 'r', encoding='utf-8')
    f.seek(0, 2)
    i = 0
    while True:
        if i >= timeout/0.1:
            return False
        line = f.readline()
        print(line)
        if text in line:
            return True
        if not line:
            time.sleep(0.1)
            i += 1
