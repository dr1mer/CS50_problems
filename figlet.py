from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
figlet.getFonts()

if len(sys.argv)==3:
    first=sys.argv[1]
    second=sys.argv[2]
    if (first=="-f" or first=="--font") and (second in figlet.getFonts()):
        s=input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(s))
    else:
        sys.exit("Invalid usage")

# if no arguments -> random font
elif len(sys.argv)==1:
    s=input("Input: ")
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(figlet.renderText(s))
else:
    sys.exit("Invalid usage")
