# program prompts the user for a level, If the user does not input 1, 2, or 3, the program should prompt again
# program randomly generete two numbers x and y
# total 10 question
# user has 3 attempts for each math problem
# at the end user see score

import random
import sys


def main():
    lvl=get_level()  # take an lvl 1 or 2 or 3
    generate_integer(lvl)
    sys.exit()





def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level ==2 or level == 3:
                return level
                break
        except:
            pass



def generate_integer(level): #for eg level=1
    score=0
    count = 0
    error = 2
    while count<10:   # ONLY FOR TEST ----------------------------------------------
        if level==1:
            x = random.randrange(10)
            y = random.randrange(10)
        elif level==2:
            x = random.randrange(10,100)
            y = random.randrange(10,100)
        else:
            x = random.randrange(100,1000)
            y = random.randrange(100,1000)

        answer = x+y
        print(x,"+",y,"= ", end="")

        guess = int(input())
        if guess==answer:
            score+=1
            count+=1
        else:
            while error!=0:
                print("EEE")
                print(x,"+",y,"= ", end="")

                guess=int(input())
                if guess!= answer:
                    error-=1
                else:
                    score+=1
                    break
            print("EEE")

            print(x,"+",y,"=",answer)
            count+=1
    print("Score:", score)




if __name__ == "__main__":
    main()
