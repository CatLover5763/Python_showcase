import sys
import os
from PIL import Image
from PIL import ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif os.path.splitext(sys.argv[1])[1] not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid input")
elif os.path.splitext(sys.argv[2])[1] not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid output")
elif os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1] :
    sys.exit("Input and output have different extensions")

try:
    shirt = Image.open("shirt.png")
    pic = Image.open(sys.argv[1])
    pic = ImageOps.fit(pic, shirt.size)
    pic.paste(shirt, shirt)
    pic.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist")
