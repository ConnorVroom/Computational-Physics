import numpy as np

def Is_Float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def Inputs():
    while True:
        x = input("Enter the distance of the planet in lightyears: ")
        v = input("Enter the speed of the spaceship in percent of c: ")

        digit_check = Is_Float(x) and Is_Float(v)
        positive_x_check = float(x) > 0
        precedential_v_check = float(v) > 0 and float(v) < 1

        if not digit_check:
            print("x and v must be numbers")
        if digit_check and not positive_x_check:
            print("x must be a positive number")
        if digit_check and not precedential_v_check:
            print("v must be a percentage")
        if digit_check and positive_x_check and precedential_v_check:
            return float(x), float(v)

def Calculate_Stationary_Frame_Time(distance, speed):
    return distance/speed #in years

def Calculate_Moving_Frame_Time(distance, speed):
    t = Calculate_Stationary_Frame_Time(distance, speed)
    t_prime = (t - speed * distance)/(np.sqrt(1 - speed**2))
    return t_prime #in years


def main():
    print(f"The time the spaceship takes from Earths perspective is {round(Calculate_Stationary_Frame_Time(10, 0.99),2)} years. \nThe time the spaceship takes from the spaceships perspective is {round(Calculate_Moving_Frame_Time(10, 0.99),2)} years")

main()