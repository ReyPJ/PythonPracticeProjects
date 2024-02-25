import random
import string

def password_gen(n=int(input("How many chars you need?: "):
    while True:
        try:
            to_random = string.ascii_letters + string.digits + string.punctuation
            randomized = ''.join(random.sample(to_random, n)

            print(randomized)

        except ValueError:
                 print("Only can use integers")

        break
                 
password_gen()





                
