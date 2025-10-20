import math

inCorrectInput = True

while inCorrectInput:

    print('\n What is the shape?')

    print('  1) Square')
    print('  2) Rectangle')
    print('  3) Triangle')
    print('  4) Circle')

    shape = int(input('Enter a number(1-4): '))

    if shape == 1:
        a = int(input('\n What is the lengthe of a side of the square: '))
        print('The area is: ', a * a)
        inCorrectInput = False
    elif shape == 2:
        b = int(input('\n What is the length of the rectangle: '))
        c = int(input('\n What is the width of the rectangle: '))
        print('The area is: ', b * c)
        inCorrectInput = False
    elif shape == 3:
        d = int(input('\n 1st side length: '))
        e = int(input('\n 2nd side length: '))
        f = int(input('\n 3rd side length: '))
        s = ((d+e+f)/2)
        area = (s*(s-d)*(s-e)*(s-f))**(1/2)
        print("The area is: ",area)
        inCorrectInput = False
    elif shape == 4:
        r = int(input('\n What is the radius: '))
        ar = math.pi * r * r
        print("The area is: ",ar)
        inCorrectInput = False
    else:
        print("Invalid input. Try again!")

 