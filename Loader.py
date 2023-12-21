import os

# Clear console based on the operating system
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

# Clear the console
clear_console()

# Import necessary modules
import time
import random
import string
import os
import subprocess

# Rest of the code
def git_clone(url):
    try:
        subprocess.run(["git", "clone", url])
        print("Clone successful!")
    except subprocess.CalledProcessError as e:
        print("Clone failed:", e)

def run_zphisher():
    try:
        os.chdir("zphisher")
        subprocess.run(["bash", "zphisher.sh"])
        print("Zphisher executed successfully!")
    except subprocess.CalledProcessError as e:
        print("Zphisher execution failed:", e)

def run_user_finder():
    try:
        os.chdir("UserFinder")
        subprocess.run(["bash", "UserFinder.sh"])
        print("User Finder executed successfully!")
    except subprocess.CalledProcessError as e:
        print("User Finder execution failed:", e)

def run_port_scanner():
    try:
        os.chdir("PortScan")
        subprocess.run(["python3", "PortScan.py"])
        print("Port Scanner executed successfully!")
    except subprocess.CalledProcessError as e:
        print("Port Scanner execution failed:", e)

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

red_color_code = "\033[91m"
reset_color_code = "\033[0m"

# ASCII art
ascii_art = f"""
{red_color_code}
  _____    ___         __  ____               
 / ___ \  / _ \___ ___/ / / __/_ _____ ___    
/ / _ `/ / , _/ -_) _  / / _// // / -_|_-<    
\ \_,_/ /_/|_|\__/\_,_/ /___/\_, /\__/___/    
 \___/                      /___/             
              #developed by xenidev
{reset_color_code}
"""

# Delayed display of ASCII art
print(ascii_art)
time.sleep(2)

# Animated loading message
loading_messages = [
    "Loading...",
    "Preparing the tools...",
]

for loading_message in loading_messages:
    print(f"\r{red_color_code}{loading_message}{reset_color_code}", end="")
    time.sleep(1)

print("\n")

# Delayed display of available tools
tools = {
    1: "Zphisher",
    2: "User Finder",
    3: "Port Scanner",
    4: "SlowLoris"
}

# Display the available tools
print(f"{red_color_code}Available tools:{reset_color_code}")
for key, value in tools.items():
    print(f"[{red_color_code}{key}{reset_color_code}] {value}")

# Prompt the user for input
choice = input(f"{red_color_code}[RedEyes]{reset_color_code} : ")

# Check the user's choice and perform the corresponding action
if choice.isdigit() and int(choice) in tools:
    if tools[int(choice)] == "Zphisher":
        repository_url = "https://github.com/htr-tech/zphisher.git"
        git_clone(repository_url)
        time.sleep(1)  # Delay for 1 second after cloning
        run_zphisher()
    elif tools[int(choice)] == "User Finder":
        repository_url = "https://github.com/mishakorzik/UserFinder.git"
        git_clone(repository_url)
        time.sleep(1)  # Delay for 1 second after cloning
        run_user_finder()
    elif tools[int(choice)] == "Port Scanner":
        repository_url = "https://github.com/XDevyy/PortScan.git"
        git_clone(repository_url)
        time.sleep(1)  # Delay for 1 second after cloning
        run_port_scanner()
    elif tools[int(choice)] == "SlowLoris":
        repository_url = "https://github.com/gkbrk/slowloris"
        git_clone(repository_url)
        time.sleep(1)  # Delay for 1 second after cloning
        run_port_scanner()
else:
    print("Invalid choice!")
