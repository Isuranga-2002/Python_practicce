kilometers = float(input("Enter the distance in kilometers: "))

def kilometers_to_miles(kilometers):
    miles = kilometers / 1.609
    print("Distance in miles: ",round(miles,2))

kilometers_to_miles(kilometers)
