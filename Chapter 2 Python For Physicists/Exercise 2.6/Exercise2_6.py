import numpy as np

def Determine_v2_l2(v1, l1):
    G = 6.6738 * 10 ** -11 #Newtons Gravitational Constant in m^3 / kg s^2
    M = 1.9891 * 10 ** 30 # Mass of the Sun in kg
    
    a = 1
    b = -(2 * G * M) / (v1 * l1)
    c = (-v1 ** 2 + (2 * G * M) / l1)

    v2_root1 = (-b + np.sqrt(b ** 2 - 4 * a * c))/(2 * a)
    v2_root2 = (-b - np.sqrt(b ** 2 - 4 * a * c))/(2 * a)

    l2_root1 = l1 * v1 / v2_root1
    l2_root2 = l1 * v1 / v2_root2

    if v2_root1 < v2_root2:
        return (v2_root1, l2_root1)
    return (v2_root2, l2_root2)

def Determine_Period(l1, l2, v1):
    a = (1/2) * (l1 + l2)
    b = np.sqrt(l1 * l2)
    T = (2 * np.pi * a * b) / (l1 * v1)
    return T

def Determine_Eccentricity(l1, l2):
    e = (l2 - l1) / (l2 + l1)
    return e



perihelion_distance_earth = 1.4710*10**11 #m
perihelion_velocity_earth =  3.0286*10**4 #m/s

aphelion_velocity_earth, aphelion_distance_earth = Determine_v2_l2(perihelion_velocity_earth, perihelion_distance_earth)

period_earth = Determine_Period(perihelion_distance_earth, aphelion_distance_earth, perihelion_velocity_earth)

eccentricity_earth = Determine_Eccentricity(aphelion_distance_earth, perihelion_distance_earth)

print(f"The earths aphelion is at a distance of {aphelion_distance_earth/10**9} Gkm from the sun. Its speed at the aphelion is {aphelion_velocity_earth/1000} km/s")
print(f"The earths period is {period_earth / (3600 * 24)} in days and the eccentricity_earth is {eccentricity_earth}")




