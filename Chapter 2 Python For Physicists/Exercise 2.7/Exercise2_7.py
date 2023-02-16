def Catalan_Equation(Cn, n):
    return Cn * (4*n + 2) / (n + 2)

i = 0
C = 1

while Catalan_Equation(C, i) <= 10**9:
    print(f"The Catalan number at n = {i} is {int(C)}")
    C = Catalan_Equation(C, i)
    i+=1
    
