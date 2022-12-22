import numpy as np

def Height_Input(): #This function checks if the import is a positive number otherwise will ask for a different import
    while True:
        h = input("Enter the height of the building: ")
        if not h.isdigit():
            print("height must be a number \n")
        if h.isdigit() and float(h) < 0:
            print("height must be positive \n")
        if h.isdigit() and float(h) > 0:
            break
    return float(h)

def Object_Fall_Time(height): #Calculates the balls fall time with a constant acceleration equation
    g = 9.8 #m/s^2
    t = np.sqrt(2*height/g)
    return t

def main(): #Main functionality of program
    height = Height_Input()

    time = Object_Fall_Time(height)

    print(f"The time for the object to fall from {height}m is {round(time,3)}s")

main() #Calling the main function