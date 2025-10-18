print('BANK SYSTEM - ENTER PIN MODULE')

pin = int(input('Please enter your 4-digit PIN: '))

while pin != 1234:
    print('Incorrect PIN. Please try again.')
    pin = int(input('Please enter your 4-digit PIN: '))

print('PIN accepted. Access granted.')