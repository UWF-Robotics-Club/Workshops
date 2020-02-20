my_char = "A"
my_float = 101.1
my_string = "changeMe"
my_int = 5


def printing():
    print(my_string, my_char, end='-')
    print(my_int, my_float, sep='*')


def my_continue():
    print()
    input("Press Enter to Continue")
    print()


def while_loops():
    w = 0
    while w < 5:
        if w == 2:
            w += 1
            continue
        elif w == 4:
            break
        else:
            print("Everything is based on tabs " + str(w))
            w += 1
        # Cannot use ++ or --


def dictionaries():
    my_dict = {
        "Day": 30,
        "Month": "January",
        "Year": 2020
    }
    print(my_dict)
    print(my_dict.get("Day"))


class Introduction:
    """
    An Introductory Class
    Functions:
    __init__()
    __continue__()
    add_to_char_array(char)
    variable_types()
    printing()
    ForLoops()
    while_loops()
    list_operations()
    dictionaries()
    print_char_array

    """

    def __init__(self):
        self.charArray = ['A']

    def variable_types(self):
        global my_string
        global my_char
        global my_int
        global my_float
        my_string = "Hello World!"
        print(type(my_string))

        my_char = 'A'
        print(type(my_char))

        print(type(self.charArray))

        my_int = 100
        print(type(my_int))

        my_float = 100.1
        print(type(my_float))

    def add_to_char_array(self, my_input):
        self.charArray.append(my_input)

    def for_loops(self):
        for x in self.charArray:
            print(x, end=' ')
            print()

        for i in range(0, 5):
            print(i, end=' ')
            print()

    def list_operations(self):
        self.charArray.append('C')
        self.charArray.insert(len(self.charArray), 'Z')
        self.charArray.extend(['H', 'E', 'L', 'L', 'O'])  # same as list1 = list1 + list2

        try:
            print("'A' is at element " + str(self.charArray.index('A')))
        except ValueError:
            print("Sorry A is no longer an element in the list")

        try:
            self.charArray.remove('A')
        except ValueError:
            print("Sorry A is no longer an element in the list")

        self.charArray.sort()
        self.charArray.reverse()
        print("The last element '" + self.charArray.pop(len(self.charArray) - 1) + "' was removed")
        self.print_char_array()

    def print_char_array(self):
        print(self.charArray)


# END OF CLASS #

t = Introduction()
print(t.__doc__)

while True:
    print("Variable Types")
    t.variable_types()
    my_continue()

    # Single Line Comments

    print("add_to_char_array")
    t.add_to_char_array('B')
    t.print_char_array()
    my_continue()

    print("Printing")
    printing()
    my_continue()

    print("For Loops")
    t.for_loops()
    my_continue()

    print("While Loops")
    while_loops()
    my_continue()

    print("List Operations")
    t.list_operations()
    my_continue()

    '''
    Multiline
    Comments
    '''

    print("Dictonary")
    dictionaries()
    my_continue()

    if input("Would you like to repeat the lesson? y or n: ") != "y":
        exit()
