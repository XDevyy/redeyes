import time
import random
import string
import os
import subprocess

def run_zphisher():
    try:
        subprocess.run(["cd", "zphisher"])
        subprocess.run(["bash", "zphisher.sh"])
        print("Zphisher executed successfully!")
    except subprocess.CalledProcessError as e:
        print("Zphisher execution failed:", e)

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
    1: "Zphisher"
}

# Display the available tools
print("Available tools:")
for key, value in tools.items():
    print(f"[{key}] {value}")

# Prompt the user for input
choice = input("Enter the number of the tool to run: ")

# Check the user's choice and perform the corresponding action
if choice.isdigit() and int(choice) in tools:
    if tools[int(choice)] == "Zphisher":
        run_zphisher()
else:
    print("Invalid choice!")
