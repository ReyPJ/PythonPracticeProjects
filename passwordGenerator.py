import string
import random


def passGenerator():
    n = int(input("How many characters do you want: "), base=20)
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
    else:
        print("ERROR")


passGenerator()
