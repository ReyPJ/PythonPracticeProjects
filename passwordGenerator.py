import string
import random

def Pass_Generator():

    while True:
        try:
            n = int(input("How many characters do you want: "))
            print(f"Your password will be have {n} characters")
        
        except ValueError:
            print("Invalid input. Please use a integer")
            break
        
        n_chars = input("Do you want special character?(Y/n): ").lower()
        to_random = string.ascii_letters + string.digits
        # Randomizer
        randomized = ''.join(random.sample(to_random, n))

        if "n" in n_chars:
            print(f"Your password without specialChars is: {randomized}")
        elif "y" in n_chars:
            randomSpecial = ''.join(random.sample(
                to_random + string.punctuation, n))
            print(f"Your special password is: {randomSpecial.capitalize()}")
            return randomSpecial

        else:
            print("You need to use 'y' or 'n'")        
        break

Pass_Generator()

