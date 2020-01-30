from time import sleep

myString = "Hello World!"
print(type(myString))

myChar = 'A'
print(type(myChar))

myCharArray = ['A', 'B', 'C']
print(type(myCharArray))

myInt = 100
print(type(myInt))

myFloat = 100.1
print(type(myFloat))

print(myString, myChar, end = '-')
print(myInt, myFloat, sep = '*')


for x in myCharArray:
    print(x, end = ' ')
print()


for i in range(0,5):
    print(i, end = ' ')
print()


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

#SingleLine Comments

'''
Multiline
Comments
'''

'''
Switcher / Dictionary
Functions
Headers from other file locations (adding paths)
classes
input
'''

    



