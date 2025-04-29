# greeting_decision.py

# prompt user for name
name = input("What's your name? ")
day_check = input(f"Hi {name}, are you having a good day? (yes/no): ")

# ask user if they are having a good day
if day_check.lower() == "yes":
    print("That's awesome to hear! Keep crushing it! 💪")
elif day_check.lower() == "no":
    print("That’s okay. You showed up, and that’s enough today. 🙌")
else:
    print("Got it — no pressure. Just keep showing up. 👊")
