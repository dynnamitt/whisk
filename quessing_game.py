import random
import pretty_errors


y = random.randint(1, 13)

while True:
    x = int(input("qeussss number!!"))

    if x == y:
        print("you won")
    elif x <= y:
        print("higher")
    elif x >= y:
        print("lowwwwer!")
    else:
        print("big noob")