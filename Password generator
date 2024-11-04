import random
import string

def generate_password(length, use_uppercase, use_digits, use_special):
    """Generate a random password based on the specified criteria."""
    character_pool = string.ascii_lowercase  
    if use_uppercase:
        character_pool += string.ascii_uppercase  
    if use_digits:
        character_pool += string.digits  
    if use_special:
        character_pool += string.punctuation  
    if length < 1 or len(character_pool) == 0:
        return None  
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password
def main():
    print("Welcome to the Simple Password Generator!")
    try:
        length = int(input("Enter the desired length of the password: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'
        password = generate_password(length, use_uppercase, use_digits, use_special)

        if password:
            print(f"Generated password: {password}")
        else:
            print("Invalid input. Please make sure to select at least one character type and a positive length.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the length.")

if _name_ == "_main_":
    main()
