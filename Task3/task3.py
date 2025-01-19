import random
import string

def generate_password(length, complexity):
    """
    Generates a password based on length and complexity level.

    Parameters:
    length (int): Length of the password
    complexity (int): Complexity level (1, 2, or 3)

    Returns:
    str: Generated password
    """
    if complexity == 1:
        # Simple password: Lowercase letters only
        characters = string.ascii_lowercase
    elif complexity == 2:
        # Medium password: Lowercase and uppercase letters
        characters = string.ascii_letters
    elif complexity == 3:
        # Strong password: Lowercase, uppercase, digits, and special characters
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Complexity level must be 1, 2, or 3")

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length < 6:
                print("Password length should be at least 6 characters.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for length.")
    
    # Get user input for password complexity
    while True:
        try:
            complexity = int(input("Enter the complexity (1 = Simple, 2 = Medium, 3 = Strong): "))
            if complexity not in [1, 2, 3]:
                print("Please enter a complexity level of 1, 2, or 3.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for complexity.")
    
    # Generate and display password
    password = generate_password(length, complexity)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()