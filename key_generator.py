import random
import string
with open("key.dat", mode="r+") as f:
    for a in range(0, 1000000):
        f.write(random.choice(string.ascii_letters))

