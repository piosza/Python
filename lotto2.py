import random

myNumbers = []
Lista = [10, 11, 22, 33, 44, 55, 66, 77, 88, 89, 999, 1000]

while len(myNumbers) < 10:
    newNumber = random.choice(Lista)

    if newNumber in myNumbers:
        print("bloked: ", newNumber)
        continue
    myNumbers.append(newNumber)
print("numbers:", sorted(myNumbers))
