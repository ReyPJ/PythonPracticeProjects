import random
import string
import sqlite3


def password_gen(n):
    to_random = string.ascii_letters + string.digits + string.punctuation
    randomized = ''.join(random.sample(to_random, n))
    print(randomized)
    return randomized


number = int(input("How many chars you need?: "))
password = password_gen(number)

with sqlite3.connect("passwords.db") as con:
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO passwords (passw) VALUES (?)",
        (password, )
    )
