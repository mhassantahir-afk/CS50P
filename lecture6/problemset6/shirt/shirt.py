from PIL import Image
from PIL import ImageOps
import sys

def cond(x,y):
    if(x.endswith(".jpg") and y.endswith(".jpg")) or (x.endswith(".jpeg") and y.endswith(".jpeg")) or (x.endswith(".png") and y.endswith(".png")):
        return True
    else:
        return False


try:
    if len(sys.argv) == 3 and cond(sys.argv[1],sys.argv[2]):
        before = Image.open(sys.argv[1])
        overlay = Image.open("shirt.png")
        size = overlay.size
        before = ImageOps.fit(before ,size)
        before.paste(overlay, (0, 0), overlay)
        before.save(sys.argv[2])
        before.close()
        overlay.close()
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    else:
        print("Input and output have different extensions")
        sys.exit(1)


except(FileNotFoundError):
    print("Invalid Input!")
    sys.exit(1)

