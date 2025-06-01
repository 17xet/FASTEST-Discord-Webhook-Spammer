import requests
import time
import threading
import os
from pystyle import Colors, Colorate

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

os.system('title ghost')

def print_banner():
    banner = """
                                                                      
                                     ____        _     __             _    _____               
                                    / __ \\____ _(_)___/ /__  _____   | |  / /__ \\            
                                   / /_/ / __ `/ / __  / _ \\/ ___/   | | / /__/ /             
                                  / _, _/ /_/ / / /_/ /  __/ /       | |/ // __/               
                                 /_/ |_|\\__,_/_/\\__,_/\\___/_/        |___//____/            
                          ┌────────────────────────────┬───────────────────────────────────┐   
                          │   (¯`·.¸¸.·´¯`·.¸¸.·´¯)    │ ┌───────────────────────────────┐ │   
                          │   ( \                 / )  │ │ https://youtube.com/@17xet    │ │   
                          │  ( \ )               ( / ) │ │                               │ │   
                          │ ( ) ( Made - by 17xet ) ( )│ │ https://github.com/17xet      │ │   
                          │  ( / )               ( \ ) │ │                               │ │   
                          │   ( /                 \ )  │ │ https://discord.gg/3bDXuSTr   │ │   
                          │    (_.·´¯`·.¸¸.·´¯`·.¸_)   │ └───────────────────────────────┘ │   
                          └────────────────────────────┴───────────────────────────────────┘   
    """
    print(Colorate.Horizontal(Colors.green_to_blue, banner))

def send_message(webhook_url, message, i):
    while True:
        response = requests.post(webhook_url, json={"content": message})
        if response.status_code == 204:
            print(Colorate.Horizontal(Colors.green_to_cyan, f"[+] Message {i+1} sent successfully!"))
            break
        elif response.status_code == 429:
            print(Colorate.Horizontal(Colors.red_to_yellow, "[-] Rate limited. Waiting before retrying..."))
            retry_after = int(response.headers.get("Retry-After", 5))
            time.sleep(retry_after)
        else:
            print(Colorate.Horizontal(Colors.red_to_purple, f"[-] Failed to send message {i+1}. Status Code: {response.status_code}"))
            break

def send_webhook_message(webhook_url, message, count, delay):
    threads = []
    for i in range(count):
        thread = threading.Thread(target=send_message, args=(webhook_url, message, i))
        threads.append(thread)
        thread.start()
        time.sleep(delay / 1000)  

    for thread in threads:
        thread.join()
    
    input(Colorate.Horizontal(Colors.blue_to_cyan, "\nAll messages sent. Press Enter to continue..."))
    clear_screen()  
    main()  

def main():
    while True:
        clear_screen()  
        print_banner()
        webhook_url = input(Colorate.Horizontal(Colors.blue_to_cyan, "Enter Webhook > "))
        message = input(Colorate.Horizontal(Colors.blue_to_cyan, "Enter Message > "))
        count = int(input(Colorate.Horizontal(Colors.blue_to_cyan, "How Many Messages > ")))
        delay = int(input(Colorate.Horizontal(Colors.blue_to_cyan, "Delay (Ms) 0 = no delay > ")))
        
        send_webhook_message(webhook_url, message, count, delay)

if __name__ == "__main__":
    main()
