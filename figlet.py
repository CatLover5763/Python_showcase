import sys
from pyfiglet import Figlet
import random
figlet = Figlet()


font = figlet.getFonts()
if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in font:
    text = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print("Output")
    print(figlet.renderText(text))
elif len(sys.argv) == 0:
    text = input("Input: ")
    font = random.choice(font)
    print("Output")
    print(figlet.renderText(text))
else:
    sys.exit("Invalid usage")

