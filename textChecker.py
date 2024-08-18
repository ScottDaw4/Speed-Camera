import speedFile
def registrationPlate():
    listOfPlates = speedFile.readData()
    charsetL = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    charsetN = ["0","1","2","3","4","5","6","7","8","9"]
    letterCheck = False
    numberCheck = False
    x = 0
    plates = []
    for x in range(len(listOfPlates)):
        plate = []
        rawPlate = listOfPlates[x].split()[0]
        while len(rawPlate) != 8:
            print("You need to have the format XX00 000")
            rawPlate = input("Number plate? (XX00 000) \n") 
        for letter in rawPlate:
            plate.append(letter)
        for reg in range(0,2):
            for char in range(len(charsetL)):
                if plate[reg] == charsetL[char]:
                    x += 1
                if x == 2:
                    letterCheck = True
        for reg in range(2,8):
            for char in range(len(charsetN)):
                if plate[reg] == charsetN[char]:
                    x += 1
                if x == 7:
                    numberCheck = True
        if letterCheck and numberCheck:
            plates.append(plate)
    return plates
