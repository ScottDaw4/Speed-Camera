import textChecker  # Import the 'textChecker' module.
import speedFile 
generatePlates = input("Would you like to generate any more plates? (y/n)\n")
if generatePlates == "y":
    x = int(input("How many more? "))
    speedFile.writeData(x)
listOfPlates = speedFile.readData()
#Camera one gets the time that the car went past the first camera
def cameraOne():
    TotalTime1 = []
    with open("vehicleData.txt", "r") as file:
        for x in range(len(listOfPlates)):
            Time1 = int(listOfPlates[x].split()[1].split(":")[0])  # Data from file: current time in hours.
            Time1M = int(listOfPlates[x].split()[1].split(":")[1])  # Data from file: current time in minutes.
#            print(f"{Time1}:{Time1M}")  # Display the time entered by the user.
            Time1 *= 60  # Convert hours to minutes.
            TotalTime1.append(int(Time1M + Time1))  # Calculate the total time in minutes.
    return TotalTime1  # Return the total times as a list

# Camera two gets the time that the car went past the second camera
def cameraTwo():
    TotalTime2 = []
    with open("vehicleData.txt", "r") as file:
        for x in range(len(listOfPlates)):
            Time2 = int(listOfPlates[x].split()[2].split(":")[0])  # Data from file: current time in hours.
            Time2M = int(listOfPlates[x].split()[2].split(":")[1])  # Data from file: current time in minutes.
#            print(f"{Time2}:{Time2M}")  # Display the time entered by the user.
            Time2 *= 60  # Convert hours to minutes.
            TotalTime2.append(int(Time2M + Time2))  # Calculate the total time in minutes.
    return TotalTime2  # Return the total times as a list

plate = textChecker.registrationPlate()  # Get the car's registration plate using 'textChecker'.

# Distance between two cameras (miles)
distance = 1

first = cameraOne()  # Get the time the car passed the first camera.
second = cameraTwo()  # Get the time the car passed the second camera.
timeTaken = []
for x in range(len(second)):
    timeTaken.append((second[x] - first[x]) / 60)  # Calculate the time taken between the two cameras in hours.

MPH = []
for x in range(len(listOfPlates)):
    if timeTaken[x] != 0:
        MPH.append(int((distance / timeTaken[x])))  # Calculate the speed in miles per hour.

# Display the speed and car's registration plate.

for x in range(len(MPH)):
    if MPH[x] > 30:
        print(f"{MPH[x]}mph - number plate: {plate[x]} - BREAKING SPEED LIMIT OF 30MPH")
    else:
        print(f"{MPH[x]}mph - number plate: {plate[x]}")
          
input()  # Wait for user input to keep the console window open.