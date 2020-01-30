myChar = "A"
myFloat = 101.1

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
    

    """
    def __init__(self):
        self.charArray = ['A']

    def __continue__(self):
        print()
        input("Press Enter to Continue")

    def AddToCharArray(self, input):
        self.charArray.append(input)
        
    def variableTypes(self):
        myString = "Hello World!"
        print(type(myString))

        myChar = 'A'
        print(type(myChar))

        print(type(self.charArray))

        myInt = 100
        print(type(myInt))

        myFloat = 100.1
        print(type(myFloat))

    def Printing():
        global myChar
        global myFloat 
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
        self.charArray.insert('A', 3)
        self.charArray.extend(['H', 'E', 'L' ,'L', 'O']) #same as list1 = list1 + list2
        print("'A' is at element " + str(this.charArray.index('A')))
        self.charArray.remove('A')
        self.charArray.sort()
        self.charArray.reverse()
        print("The last element '" + this.charArray.pop(index)+ "' was removed")
        print(self.charArray)
        
    def Dictionaries():
        print("TODO")
### END OF CLASS ###

t = Introduction()
print(
    t.__doc__)

while True:
    t.variableTypes()
    t.__continue__()
    t.ForLoops()
    t.__continue__()
    t.AddToCharArray('B')
    t.ForLoops()

# Single Line Comments

'''
Multiline
Comments
'''

'''
Switcher / Dictionary
Catching errors/exeptions
Headers from other file locations (adding paths)
Splitting Files
Type Conversions
'''

    



