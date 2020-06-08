


def CalcAge():
    name = str(input("Kindly enter your name here: "))
    age = int(input("how old are you now ? "))
    result = 100 - age
    print(f" your name is {name}, you are {age} years old, and you will be 100 years old in {result} years ")


CalcAge()


# iterates the list and returns numbers les than 5
MyList = [23,2,3,45,6,2.843,4,100,5,23,67,55,0,0.4,3.7]

for items in MyList:
    while items <= 5:
        print([items])
        break

print([items for items in MyList if items < 5])

#convert json data to object
import json
myJson = '{"Name":"Mickey","Twitter Handle":"@phiiphi13","Dialect":"python"}'
pyJson = json.loads(myJson)

print(myJson)