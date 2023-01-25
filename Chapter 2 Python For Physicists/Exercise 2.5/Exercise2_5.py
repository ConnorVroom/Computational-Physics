import numpy as np
from scipy.constants import hbar
from scipy.constants import electron_mass
def EigenValues(m,E,V):
    k1 = np.sqrt(2*m*E)/hbar
    k2 = np.sqrt(2*m*(E-V))/hbar
    return k1, k2

def DirectionProbability(m,E,V):
    k1, k2 = EigenValues(m, E, V)
    T = (4 * k1 * k2) / (k1 + k2) ** 2
    R = ((k1 - k2) / (k1 + k2)) ** 2
    return T, R

def main():
    m = electron_mass #kg
    E = 10 #ev
    V = 9 #ev

    T, R = DirectionProbability(m, E, V)

    print(f"The probability for the electron to transmit is {round(T,2)}\n")
    print(f"The probability for the electron to reflect is {round(R,2)}\n")

main()