import time
import random
import string
import os
import subprocess

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

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

print("""
  _____    ___         __  ____               
 / ___ \  / _ \___ ___/ / / __/_ _____ ___    
/ / _ `/ / , _/ -_) _  / / _// // / -_|_-<    
\ \_,_/ /_/|_|\__/\_,_/ /___/\_, /\__/___/    
 \___/                      /___/             
              #developed by xeni
""")

print("         <=======Loading=======>")
time.sleep(4)

print("Hi, Select the tool you need to run.")
time.sleep(3)

# Delayed display of available tools
tools = {
    1: "Zphisher",
    2: "User Finder"
}

# Display the available tools
print("Available tools:")
for key, value in tools.items():
    print(f"[{key}] {value}")

# Prompt the user for input
choice = input("\033[91m[RedEyes]\033[0m Enter the number of the tool to run: ")

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
else:
    print("Invalid choice!")
