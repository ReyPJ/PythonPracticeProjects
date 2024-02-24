import string
import random


# length es para decir cuantos chars maximos queremos
def string_randomizer(lenght, use_special_chars=True):
    chars = string.ascii_letters + string.digits
    if use_special_chars:
        chars += string.punctuation

    return ''.join(random.choice(chars) for _ in range(lenght))


def passGenerator():
    try:
        n = int(input("How many characters do you want?: "))
        useChars = input("Do you want to use special characters?(Y/n)").lower()

        use_special_chars = useChars == 'y'
        password = string_randomizer(n, use_special_chars)
        print(
            f"Your {'special' if use_special_chars else ''} password is: {password}")
    except ValueError:
        print(
            "Invalid input. Please enter a positive integrer for the number of characters")


passGenerator()
