#!/usr/bin/env python3
 
ParticipantNumber = 2
participantData = []

registeredParticipants = 0

outputFile = open("ParticipantData.txt", "w")

while(registeredParticipants < ParticipantNumber):
    tempPartData = []
    name = input("Please, enter your name: ")
    tempPartData.append(name)
    country = input("Your country: ")
    tempPartData.append(country)
    age = int(input("Your age: "))
    tempPartData.append(age)

    participantData.append(tempPartData)
    registeredParticipants += 1

for participant in participantData:
    for data in participant:
        outputFile.write(str(data))
        outputFile.write(" ")
    outputFile.write("\n")

outputFile.close()
