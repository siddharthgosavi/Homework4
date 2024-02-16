"""
CSC 4110
HOMEWORK4:QUESTION 3
START DATE: 02/ 10 / 2024
BEGIN ROHITH SURESH (02/10/24)
"""

import random
import string

class PasswordSimulator:
    def __init__(self):
        self.accepted_passwords = []
        self.unaccepted_passwords = []
        self.archived_passwords = []
        self.dictionary_words = set(['password', '123456', 'qwerty', 'letmein', 'monkey'])  # Sample dictionary words

    def generate_password(self, length=8):
        """
        Generates a random password of specified length.
        
        Args:
        - length: Length of the password (default is 8)
        
        Returns:
        - A randomly generated password
        """
        password_characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(password_characters) for _ in range(length))

    def is_acceptable_password(self, password):
        """
        Checks if the given password is acceptable.
        
        Acceptance criteria:
        - Contains at least one special symbol
        - Not a word in a dictionary list
        
        Args:
        - password: Password to check
        
        Returns:
        - True if the password is acceptable, False otherwise
        """
        if any(char in string.punctuation for char in password) and password not in self.dictionary_words:
            return True
        return False

    def simulate_password_generation(self):
        """
        Simulates password generation until at least 40 accepted passwords are archived.
        """
        while len(self.archived_passwords) < 40:
            password = self.generate_password()
            if self.is_acceptable_password(password):
                self.accepted_passwords.append(password)
                self.archived_passwords.append(password)
            else:
                self.unaccepted_passwords.append(password)
                self.archived_passwords.append(password)

# Usage example
if __name__ == "__main__":
    password_simulator = PasswordSimulator()
    password_simulator.simulate_password_generation()

    print("Accepted Passwords:")
    for password in password_simulator.accepted_passwords:
        print(password)

    print("\nUnaccepted Passwords:")
    for password in password_simulator.unaccepted_passwords:
        print(password)

    print("\nArchived Passwords (Accepted and Unaccepted):")
    for password in password_simulator.archived_passwords:
        if password in password_simulator.accepted_passwords:
            print(password + " (Accepted)")
        else:
            print(password + " (Unaccepted)")


"""
FINAL DATE: 15/ 02/ 2024
END ROHITH SURESH
"""