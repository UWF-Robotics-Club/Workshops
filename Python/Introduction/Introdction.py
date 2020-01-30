myChar = "A"
myFloat = 101.1
myString = "changeMe"
myInt = 5

class Introduction:
    """
    An Introductory Class
    Functions:
    __init__()
    __continue__()
    AddToCharArray(char)
    variableTypes()
    Printing()
    ForLoops()
    WhileLoops()
    ListOperations()
    Dictionaries()
    PrintCharArray

    """
    def __init__(self):
        self.charArray = ['A']

    def __continue__(self):
        print()
        input("Press Enter to Continue")
        print()

    def VariableTypes(self):
        global myString
        myString = "Hello World!"
        print(type(myString))

        myChar = 'A'
        print(type(myChar))

        print(type(self.charArray))

        myInt = 100
        print(type(myInt))

        myFloat = 100.1
        print(type(myFloat))

    def AddToCharArray(self, myInput):
        self.charArray.append(myInput)
        
    def Printing(self):
        print(myString, myChar, end = '-')
        print(myInt, myFloat, sep = '*')

    def ForLoops(self):
        for x in self.charArray:
            print(x, end = ' ')
            print()

        for i in range(0,5):
            print(i, end = ' ')
            print()

    def WhileLoops(self):
        w = 0
        while(w < 5):
            if(w == 2):
                w += 1
                continue
            elif(w == 4):
                break
            else:
                print("Everything is based on tabs " + str(w))
                w += 1
            #Cannot use ++ or --

    def ListOperations(self):
        self.charArray.append('C')
        self.charArray.insert(len(self.charArray), 'Z')
        self.charArray.extend(['H', 'E', 'L' ,'L', 'O']) #same as list1 = list1 + list2

        try:
            print("'A' is at element " + str(self.charArray.index('A')))
        except:
            print("Sorry A is no longer an element in the list")
            
        try:
            self.charArray.remove('A')
        except:
            print("Sorry A is no longer an element in the list")

        self.charArray.sort()
        self.charArray.reverse()
        print("The last element '" + self.charArray.pop(len(self.charArray)-1)+ "' was removed")
        self.PrintCharArray()
        
    def Dictionaries(self):
        Dict = {
          "Day": 30,
          "Month": "January",
          "Year": 2020
        }
        print(Dict)
        print(Dict.get("Day"))

    def PrintCharArray(self):
        print(self.charArray)
        
### END OF CLASS ###

t = Introduction()
print(t.__doc__)

while True:
    print("Variable Types")
    t.VariableTypes()
    t.__continue__()

    print("AddToCharArray")
    t.AddToCharArray('B')
    t.PrintCharArray()
    t.__continue__()

    print("Printing")
    t.Printing()
    t.__continue__()

    print("For Loops")
    t.ForLoops()
    t.__continue__()

    print("While Loops")
    t.WhileLoops()
    t.__continue__()

    print("List Operations")
    t.ListOperations()
    t.__continue__()

    print("Dictonary")
    t.Dictionaries()
    t.__continue__()

    if(input("Would you like to repeat the lesson? y or n: ") != "y"):
        exit()

# Single Line Comments

'''
Multiline
Comments
'''

"""
or
this
"""



    



