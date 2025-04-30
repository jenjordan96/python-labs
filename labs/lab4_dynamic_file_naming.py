import os
from datetime import datetime

# Step 1: Set up the folder
folder_name = "dynamic_files"
os.makedirs(folder_name, exist_ok=True)

# Step 2: Create dynamic filename with timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"file_{timestamp}.txt"
full_path = os.path.join(folder_name, filename)

# Step 3: Write content
with open(full_path, "w") as file:
    file.write(f"This file was created at {timestamp}\n")
    file.write("Every file will now have a unique name!\n")

# Step 4: Read content
with open(full_path, "r") as file:
    content = file.read()

# Step 5: Display
print(f"\nCreated file: {filename}")
print("\nFile Content:\n")
print(content)

import time

# Step 6: Auto-cleanup files older than 1 day (86,400 seconds)

# How many seconds old before deleting?
threshold_seconds = 86400  # 24 hours

# Get the current time
current_time = time.time()

# List all files in the folder
for file_name in os.listdir(folder_name):
    file_path = os.path.join(folder_name, file_name)
    
    # Check if it's a file (not a folder)
    if os.path.isfile(file_path):
        # Get the file's last modified time
        file_modified_time = os.path.getmtime(file_path)
        
        # If the file is older than 1 day, delete it
        if current_time - file_modified_time > threshold_seconds:
            os.remove(file_path)
            print(f"Deleted old file: {file_name}")
