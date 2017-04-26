import steam
import datetime
import time
import subprocess
import pyautogui
from rustcmd import send_command
from win32util import does_window_exist
from webbrowser import open as web_open

def get_last_update_time(client, branch='public'):
    info = client.get_product_info(apps=[252490])
    if info == None:
        return None
    return datetime.datetime.fromtimestamp(int(info['apps'][252490]['depots']['branches']['public']['timeupdated']))

def stop_steam():
    subprocess.run('taskkill /im Steam.exe /F', check=True)

def launch_rust():
    # web_open('http://playrust.com')
    web_open('steam://run/252490')
    found_rust = False
    while not found_rust:
        found_rust = does_window_exist('Rust Configuration')
    print('Rust Configuration is open')
    pyautogui.press('enter')

def connect_to_server(ip):
    send_command('connect ' + ip)

def wait_for_menu():
    # TODO: wait properly
    time.sleep(10)
    print("initializing wipe hype")
    send_command('echo Wipe Hype Initialized')

def launch_updated_rust():
    stop_steam()
    launch_rust()
    wait_for_menu()
    # rustopia ip 74.91.125.225:28026
    connect_to_server('74.91.125.225:28026')

def start_update_loop(wait_time=10):
    client = steam.SteamClient()
    print('Logging into Steam anonymously...')
    client.anonymous_login()
    print('Logged into Steam.')
    
    prev_update_time = get_last_update_time(client)

    while True:
        update_time = get_last_update_time(client)
        print(update_time.strftime('%c'))
        #if update_time != prev_update_time:
        if True:
            launch_updated_rust()
            break
        prev_update_time = update_time
        time.sleep(wait_time)

if __name__ == '__main__':
    start_update_loop()