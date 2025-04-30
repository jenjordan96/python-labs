import os
from datetime import datetime

# Step 1: Ask the user for a message
user_message = input("What would you like to save to a file? ")

# Step 2: Create the folder
folder_name = "user_input_files"
os.makedirs(folder_name, exist_ok=True)

# Step 3: Timestamp the file name
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"user_message_{timestamp}.txt"
full_path = os.path.join(folder_name, filename)

# Step 4: Write the user message into the file
with open(full_path, "w") as file:
    file.write(user_message + "\n")

# Step 5: Confirm to the user
print(f"\n✅ Your message has been saved to: {filename}")

# Step 6: Read the file back to the user
with open(full_path, "r") as file:
    content = file.read()
    print("\n📜 Here is the content of your file:")
    print(content)
