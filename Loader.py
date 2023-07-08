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

red_color_code = "\033[91m"
white_color_code = "\033[97m"
reset_color_code = "\033[0m"

print(f"{red_color_code}"
      """
  _____    ___         __  ____               
 / ___ \  / _ \___ ___/ / / __/_ _____ ___    
/ / _ `/ / , _/ -_) _  / / _// // / -_|_-<    
\ \_,_/ /_/|_|\__/\_,_/ /___/\_, /\__/___/    
 \___/                      /___/             
              #developed by xeni
""" f"{reset_color_code}")

print("         <=======Loading=======>")

# Loading bar animation
bar_width = 20
total_time = 4  # Total time for loading animation (in seconds)
start_time = time.time()

while time.time() - start_time < total_time:
    elapsed_time = time.time() - start_time
    completed = int((elapsed_time / total_time) * bar_width)
    remaining = bar_width - completed

    # Print the loading bar animation
    print(f"\r[{red_color_code}{'=' * completed}{white_color_code}>{reset_color_code}{'.' * remaining}]",
          f"{white_color_code}{int((elapsed_time / total_time) * 100)}%{reset_color_code}",
          end="")
    time.sleep(0.1)

print("\nHi, Select the tool you need to run.")

# Delayed display of available tools
tools = {
    1: "Zphisher",
    2: "User Finder"
}

# Display the available tools
print("Available tools:")
for key, value in tools.items():
    print(f"[{red_color_code}{key}{reset_color_code}] {value}")

# Prompt the user for input
choice = input(f"{red_color_code}[RedEyes]{reset_color_code} Enter the number of the tool to run: ")

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
