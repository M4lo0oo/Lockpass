import random
import string
import os
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def generate_password(length, use_special_chars, use_uppercase, use_lowercase, use_digits, personal_info):
    characters = ''
    
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length - len(personal_info)))
    password += personal_info
    
    password_list = list(password)
    random.shuffle(password_list)
    
    return ''.join(password_list)

def is_password_secure(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in string.punctuation for char in password):
        return False
    return True

def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Nettoyer l'écran
    # ASCII Art d'un cadenas coloré
    cadenas_art = [
        "    ██████    ",
        "  ██      ██  ",
        "  ██      ██  ",
        "  ██      ██  ",
        "██████████████",
        "██████████████",
        "██████  ██████",
        "██████  ██████",
        "██████████████"
    ]

    for line in cadenas_art:
        print(Fore.YELLOW + line)

    print(Style.RESET_ALL)

    print("Commands:")
    print("  --password -g : Generate a password")
    print("  --password -c : Check if a password is secure")

def password_generation():
    length = int(input("What is the desired password length (minimum 8 characters)? "))
    if length < 8:
        print("Minimum length is 8 characters. Setting length to 8.")
        length = 8
    
    use_special_chars = input("Do you want to include special characters? (y/n) ").lower() == 'y'
    use_uppercase = input("Do you want to include uppercase letters? (y/n) ").lower() == 'y'
    use_lowercase = input("Do you want to include lowercase letters? (y/n) ").lower() == 'y'
    use_digits = input("Do you want to include numbers? (y/n) ").lower() == 'y'
    
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    favorite_singer = input("Who is your favorite singer? ")
    
    personal_info = (first_name[:2] + last_name[:2] + favorite_singer[:2]).lower()
    
    password = generate_password(length, use_special_chars, use_uppercase, use_lowercase, use_digits, personal_info)
    
    print(f"\nYour generated password is: {password}")

def check_password():
    password = input("Enter the password to check its security: ")
    if is_password_secure(password):
        print("The password is secure.")
    else:
        print("The password is not secure. Please make sure it meets the security criteria.")

def main():
    while True:
        display_menu()
        command = input("Enter command to start (e.g., --password -g): ")
        
        if command == '--password -g':
            password_generation()  
            input("\nPress Enter to return to the main menu...")
        elif command == '--password -c':
            check_password()
            input("\nPress Enter to return to the main menu...")
        else:
            print("Invalid command. Please enter '--password -g' or '--password -c'.")

if __name__ == "__main__":
    main()
