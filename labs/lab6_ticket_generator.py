import json
import uuid
from datetime import datetime

file_name = "tickets.json"

# Step 1: Menu
print("What would you like to do?")
print("1. Submit a new ticket")
print("2. View all tickets")

choice = input("Enter your choice (1 or 2): ").strip()

# Step 2: View tickets logic
if choice == "2":
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            if not data:
                print("\n📂 No tickets found.")
            else:
                print("\n📋 All Tickets:\n")
                for ticket in data:
                    print(f"🆔 {ticket['ticket_id']}")
                    print(f"👤 Submitted by: {ticket['submitted_by']}")
                    print(f"📂 Category: {ticket['category']}")
                    print(f"⚠️ Urgency: {ticket['urgency']}")
                    print(f"📝 Description: {ticket['description']}")
                    print(f"📅 Timestamp: {ticket['timestamp']}")
                    print("-" * 40)
    except FileNotFoundError:
        print("\n📂 No tickets found.")
    exit()

# Step 3: Submit ticket flow
# Define categories
categories = [
    "Network",
    "Hardware",
    "Software",
    "Printer",
    "Application Install Request",
    "Access Request",
    "Other"
]

# Get user name
user_name = input("Enter your name: ")

# Display and select category
print("\nSelect a ticket category:")
for i, category in enumerate(categories, start=1):
    print(f"{i}. {category}")

try:
    category_choice = int(input("Enter the number for your category: "))
    ticket_category = categories[category_choice - 1]
except (ValueError, IndexError):
    ticket_category = "Other"
    print("Invalid selection. Defaulting to 'Other'.")

# IAM logic: Stop here if category is 'Access Request'
if ticket_category.lower() == "access request":
    print("\n🔐 Access requests must go through Identity Management.")
    print("❌ This ticket will not be submitted.")
    exit()


# Input urgency with validation
valid_urgency = ["low", "medium", "high"]

while True:
    urgency_level = input("Urgency (Low, Medium, High): ").strip().lower()
    if urgency_level in valid_urgency:
        urgency_level = urgency_level.capitalize()
        break
    else:
        print("Please enter a valid urgency level (Low, Medium, High).")

# Input issue description
issue_description = input("Describe your issue: ")

# Generate ticket ID and timestamp
ticket_id = str(uuid.uuid4())
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create ticket
ticket = {
    "ticket_id": ticket_id,
    "timestamp": timestamp,
    "submitted_by": user_name,
    "category": ticket_category,
    "urgency": urgency_level,
    "description": issue_description
}

# Save ticket
try:
    with open(file_name, "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = []

data.append(ticket)

with open(file_name, "w") as file:
    json.dump(data, file, indent=4)

# Confirmation
print(f"\n✅ Ticket submitted successfully!")
print(f"🆔 Ticket ID: {ticket_id}")
print(f"📂 Category: {ticket_category}")
print(f"📅 Submitted on: {timestamp}")
