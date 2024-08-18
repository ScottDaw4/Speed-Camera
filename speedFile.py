import random

charsetL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
charsetN = "0123456789"

def randomPlateGen():
    L1 = random.choice(charsetL)
    L2 = random.choice(charsetL)
    N1 = random.choice(charsetN)
    N2 = random.choice(charsetN)
    N3 = random.choice(charsetN)
    N4 = random.choice(charsetN)
    N5 = random.choice(charsetN)
    randomPlate = f"{L1}{L2}{N1}{N2}-{N3}{N4}{N5}"
    return randomPlate

def randomTimeGen():
    Hours = random.randint(0, 23)
    Minutes = random.randint(0, 59)
    randomTime = f"{Hours:02d}:{Minutes:02d}"
    randomTime2 = random.randint(1,6)
    randomTime2 += Minutes
    randomTime2 = f"{Hours:02d}:{randomTime2:02d}"
    return randomTime, randomTime2

def writeData(x):
    file_name = "vehicleData.txt"
    with open(file_name, "a") as file:
        for _ in range(x):
            Time = randomTimeGen()
            file.write(f"\n{randomPlateGen()} {Time[0]} {Time[1]} \n")
    print(f"Finished writing {x} random plates")

def readData():
    listOfPlates = []
    file_name = "vehicleData.txt"
    with open (file_name, "r") as file:
        newSet = False
        linenumber = 0
        for line in file:
            if newSet == True:
                listOfPlates.append(line)
                newSet = False
            linenumber += 1
            if line == "\n":
                newSet = True
    return listOfPlates