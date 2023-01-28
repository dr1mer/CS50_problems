import random

while True:
    try:
        level = int(input("Level: "))  # level should be only int and level >=1 if not program asks level again
        if level>=1:
            answer = random.randint(1,level)
            while True:  # to play until you guess right
                try:
                    guess = int(input("Guess: "))  # if guess is not int -> Value Erorr -> ask user again for a guess
                    if guess<0: # if not -> Value Error -> ask again
                        pass
                    elif guess>answer:
                        print("Too large!")
                    elif guess<answer:
                        print("Too small!")
                    else:
                        print("Just right!")
                        break
                except ValueError: # ask guess again
                    pass
        else:
            raise ValueError # ask level again
        break

    except: # ask level again
        pass
