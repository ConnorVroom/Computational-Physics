import numpy as np

def Period_Input():
    while True:
        T = input("Enter the period of your orbit: ")
        Units = input ("Enter the units of your period (h for hours, m for minutes, and s for seconds): ")
        if not T.isdigit():
            print("T must be a number")
        if T.isdigit() and float(T) < 0:
            print("T must be a positive number")
        if T.isdigit() and float(T) > 0:
            if Units == 'h':
                return float(T)*3600
            if Units == 'm':
                return float(T)*60
            if Units == 's':
                return float(T)

def Calculate_Altitude(T):
    G = 6.67 * 10 ** -11
    M = 5.97 * 10 ** 24
    R = 6371000 
    h = (((G * M * T**2)/(4 * np.pi ** 2)) ** (1/3)) - R
    print(f"The altitude for a satellite with a period of {T}s is {int(h / 1000)} km")

def main():
    T = Period_Input()
    Calculate_Altitude(T)

main()

        
