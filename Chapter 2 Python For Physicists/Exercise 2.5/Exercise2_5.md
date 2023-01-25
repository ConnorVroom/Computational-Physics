# **Exercise 2.5: Quantum Potential Step**

##**Question:**
A well-known Quantum mechanics problem involves a particle of mass m that encounters a one-dimensional potential step. The particle with initial kinetic energy $E$ and wavevector $k_{1} = \frac{\sqrt{2mE}}{\hbar}$ enters from the left and encounters a sudden jump in potential energy of height V at position $x=0$. By solving the Schrodinger equation, one can show that when $E > V$ the particle may either (a) pass the step, in which case it has a lower kinetic energy of $E-V$ on the other side and a correspondingly smaller wavevector of $k_{2}=\frac{\sqrt{2m(E-V)}}{\hbar}$, or (b) it may be reflected, keeping all of its kinetic energy and an unchanged wavevector but moving in the opposite direction. The probabilities T and R for transmission and reflection are given by

$$T = \frac{4k_{1}k_{2}}{(k_{1}+k_{2})^2}, R = (\frac{k_{1}-k_{2}}{k_{1} + k_{2}})^2$$ 

Suppose we have a particle with mass equal to the electron mass $m = 9.11\times10^-31 kg$ and energy $10eV$ encountering a potential step of height $9eV$. Write a Python program to compute and print out the transmission and reflection probabilities using the formulas above. 

##**Physics Explication:**

To solve this problem 