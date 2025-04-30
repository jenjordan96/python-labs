# lab3_file_read_write.py

# Step 1: Define the file name
filename = "sample_text.txt"

# Step 2: Write to the file
with open(filename, "w") as file:
    file.write("Hello, Jennai! Welcome to your first Python file write.\n")
    file.write("This is line 2 of your sample file.\n")

# Step 3: Read from the file
with open(filename, "r") as file:
    content = file.read()

# Step 4: Print the content
print("\nFile Content:\n")
print(content)

