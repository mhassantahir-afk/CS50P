import sys
import random
import pyfiglet
from pyfiglet import Figlet

figlet = Figlet()

try:
    if len(sys.argv) == 1:
        fonts = figlet.getFonts()
        f = random.choice(fonts)
        figlet.setFont(font = f)
        text = (input("input:"))
        print("output: ", figlet.renderText(text))
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        figlet.setFont(font = sys.argv[2])
        text = (input("input:"))
        print("output: ", figlet.renderText(text))
    else:
        print("Invalid usage")
        sys.exit(1)
except(pyfiglet.FontNotFound, IndexError):
    print("Invalid usage")
    sys.exit(1)

sys.exit()
