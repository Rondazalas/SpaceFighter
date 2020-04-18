import os

#Grab width in pixels
def getWidth(filename):
    file = open("sprites\\" + filename, "rb")
    byte = file.read(18)
    width = file.read(1)
    file.close()
    return int.from_bytes(width, byteorder='big')

#Grab height in pixels
def getHeight(filename):
    file = open("sprites\\" + filename, "rb")
    byte = file.read(22)
    height = file.read(1)
    file.close()
    return int.from_bytes(height, byteorder='big')

#Returns boolean on whether or not the given file is of the correct format
def isProperBMP(filename):
    file = open("sprites\\" + filename, "rb")
    byteB = file.read(1)
    byteM = file.read(1)
    filler = file.read(8)
    byteStart = file.read(1)

    if (byteB != b"\x42") or (byteM != b"\x4D") or (byteStart != b"\x76"):
        print("ERROR: " + filename + " is NOT a correct file format.\n")
        return False
    else:
        return True

    file.close()

'''def createSpriteTableFile():
    file = open("spriteTable", "w")
    file.close()

    file = open("spriteTable", "ab")

    for root, dirs, files in os.walk(".\\sprites"):
        for filename in files:
            if isProperBMP(filename) == True:
                pixels = getPixels(filename)
                noDirectory = filename.split('.')[0]
                file.write(bytes(noDirectory, 'utf-8'))
                file.write(bytes("|", 'utf-8'))
                file.write(bytes([getWidth(filename)]))
                file.write(bytes("|", 'utf-8'))
                file.write(bytes([getHeight(filename)]))
                file.write(bytes("|", 'utf-8'))
                for byte in pixels:
                    file.write(byte)

    file.close()'''

#Create the C code
def createCCode():
    for root, dirs, files in os.walk(".\\sprites"):
        for filename in files:
            if isProperBMP(filename) == True:
                pixels = getPixels(filename)
                width = getWidth(filename)
                height = getHeight(filename)
                
                print("struct sprite " + filename.split('.')[0] + " = {", end="")
                print(str(width), end="")
                print(", ", end="")
                print(str(height), end="")
                print(", \"", end="")
                for byte in pixels:
                    print("\\x" + byte.hex(), end="")
                print("\"};\n")
    

#Retrieve byte data for pixels from the bmp file given.
def getPixels(filename):
    file = open("sprites\\" + filename, "rb")
    width = getWidth(filename)
    height = getHeight(filename)
    byte = file.read(118)
    pixels = []
    i = 0
    while i < height:
        alignLen = 4
        j = 0
        while j < round(width/2):
            byte = file.read(1)
            pixels.append(byte)
            if j%4 == 0:
                alignLen = 4
            j += 1
            alignLen -= 1
        file.read(alignLen)
        i += 1

    return pixels
    
    file.close()

createCCode()
