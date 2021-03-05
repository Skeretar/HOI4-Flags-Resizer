from pathlib import Path
import os
import PIL
from PIL import Image


pwd = Path('.')
images = pwd/"flags"
GoodImages = []

print("==----------==")
input("Welcome to HOI4 Flag Folder Generator. Press ENTER to continue.\n==----------==")

hoi4 = input("Please insert your HOI4 mod directory.\n> ")
conf = input("Are you sure it's that one? [Y/N]\n> ")
while conf != "Y":
    hoi4 = input("Please insert your HOI4 mod directory.\n> ")
    conf = input("Are you sure it's that one? [Y/N]\n> ")

output = Path(hoi4)
if not((output/"small").exists() or (output/"medium").exists()):
    print("Inserted folder not found or not recognized as a proper flag folder (It misses either small or medium folder)")
    input("...")
    exit()

# all flags must be:
    # - .tga
    # - 32 bit
    #Big - 82x52
    #Medium - 41x26
    #Small - 10x7
    # in bicubic

    # IMAGE COLLECTION AND ERROR CHECKING  
for image in images.iterdir():
    with Image.open(image) as I:
        
        imagesize = I.size
        filetitle = I.filename.split("\\")[::-1][0]

            # ERROR CHECKING
        print("Wrong size detected. Expect for unpredictable behavior [MIGHT CAUSE PROGRAM CRASHES]." * (imagesize != (82, 52)))

        try:
            filetitle.split("_")[0]
            filetitle.split("_")[1]

        except:
            print(f"Wrong title detected. Expect for this file be discarded. [FILE: {filetitle}]")
            continue

            # PASSED CHECKING
        GoodImages.append(I.filename)
        
input("All images have been collected. Press ENTER to continue.")


    #TO-DO: ASK WHAT HOI4 FOLDER IS

    # PROCESS IMAGES
for Im in GoodImages:
    I = Image.open(Im)
    # to save as TGA just do "I.save("title.TGA")
    
    title = (I.filename.split("\\")[::-1][0]).split(".")[0]+".tga"
    small = I.resize((10, 7), PIL.Image.BICUBIC)
    medium = I.resize((41, 26), PIL.Image.BICUBIC)
    big = I.resize((82, 52), PIL.Image.BICUBIC)

    small.save((output/"small")/title, "TGA")
    medium.save((output/"medium")/title, "TGA")
    big.save(output/title, "TGA")
    
    pass

input("Everything done. Press ENTER to exit.")
