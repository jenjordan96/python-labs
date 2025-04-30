import random
import string

def generate_password(length, use_uppercase, use_numbers, use_specials):
    char_pool = list(string.ascii_lowercase)

    if use_uppercase:
        char_pool += list(string.ascii_uppercase)
    if use_numbers:
        char_pool += list(string.digits)
    if use_specials:
        char_pool += list("!@#$%^&*()_+-=[]{}|;:,.<>?")

    if not char_pool:
        return None

    return ''.join(random.choice(char_pool) for _ in range(length))

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        score += 1

    if score == 1:
        return "Very Weak ⚠️"
    elif score == 2:
        return "Weak ❌"
    elif score == 3:
        return "Moderate ⚠️"
    else:
        return "Strong ✅"

while True:
    print("\n🔧 Password Generator")
    
    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == "y"
    use_specials = input("Include special characters? (y/n): ").strip().lower() == "y"

    password = generate_password(length, use_uppercase, use_numbers, use_specials)

    if password is None:
        print("❌ No character types selected. Please try again.")
        continue

    strength = check_strength(password)
    print(f"\n🔐 Your new password: {password}")
    print(f"🧠 Strength: {strength}")

    copy_choice = input("📋 Would you like to copy this password manually? (y/n): ").strip().lower()
    if copy_choice == "y":
        print("👉 Tip: Highlight and copy the password using your mouse or keyboard shortcut (Ctrl+C or Cmd+C)")

    again = input("\n🔁 Generate another password? (y/n): ").strip().lower()
    if again != "y":
        print("👋 Exiting Password Generator. Stay secure!")
        break
