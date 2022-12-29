import numpy as np

def Cartesian_Input():
    x = input("Enter the x component of your point: ")
    y = input("Enter the y component of your point: ")
    if (x.isdigit() and y.isdigit()):
        return float(x), float(y)
    print("x and y must be numbers")
    
def Cartesian_To_Polar(x, y):
    r = np.sqrt(x ** 2 + y ** 2)
    if y > 0:
        theta = np.arccos(x/r)
        theta = theta * 180 / np.pi
        print(f"r = {round(r,2)}, \u03B8 = {int(theta)}")
    if y < 0:
        theta = np.arccos(-x/r) + np.pi
        theta = theta * 180 / np.pi
        print(f"r = {round(r,2)}, \u03B8 = {int(theta)}")

def main():
    Cartesian_To_Polar(4, -4)

main()