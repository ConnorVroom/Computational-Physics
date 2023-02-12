# **Exercise 2.6: Planetary Orbits**

## **Question:**
The orbits in space of one body around another, such as a planet around the Sun, need not be circular. In general it takes the from of an ellipse, with the body sometimes closer in and sometimes further out. If you are given the distance $l_{1}$ of the closest approach that a planet makes to the Sun, also called its *perihelion*, and its linear velocity $v_{1}$ at perihelion, then any other property of the orbit can be calculated from theses two as follows. 

(a) Kepler's seconded law tells us that the distance $l_{2}$ and velocity $v_{2}$ of the planet at its most distant point, or *aphelion*, satisfy $l_{2}v_{2} = l_{1}v_{1}$. At the same time the total energy, kinetic plus gravitational, of a planet with velocity $v$ and distance r from the Sun is given by 

$$E = \frac{1}{2}mv^2 - G\frac{mM}{r}$$

where $m$ is the planet's mass, $M = 1.9891 \times 10^30 kg$ is the mass of the Sun, and $G = 6.6738 \times 10^-11 \frac{m^3}{kg s^2}$ is Newtons gravitational constant. Given that energy must be conserved, show that $v_{2}$ is the smaller root of the quadratic equation  

$$v_{2}^2 - \frac{2GM}{v_{1}l_{1}}v_{2} - \left[v_{1}^2 - \frac{2GM}{l_{1}}\right] = 0$$

Once we have $v_{2}$ we can calculate $l_{2}$ using the relation $l_{2} = l_{1}v_{1}/v_{2}$.

(b) Given the values of $v_{1},l_{1}, \text{and } l_{2},$ other parameters of the orbit are given by simple formulas can that be derived from Kepler's laws and the fact that the orbit is an ellipse: 
$$\text{Semi-major axis:    } a = \frac{1}{2}\left(l_{2}+l_{1}\right),$$
$$\text{Semi-minor axis:    } b = \sqrt{l_{1}l_{2}},$$
$$\text{Orbital Period:     } T = \frac{2\pi ab}{l_{1}v_{1}},$$
$$\text{Orbital eccentricity:   } e = \frac{l_{2}-l_{1}}{l_{2}+l_{1}}.$$

Write a program that ask the user to enter the distance to the Sun and velocity at perihelion, then calculates and prints the quantities $l_{2}, v_{2}, T, \text{and } e$.

(c) Test your program by having it calculate the properties of the orbits of the Earth (for which $l_{1} = 1.4710 \times 10^11 m$ and $v_{1} = 3.0287 \times 10^4 \frac{m}{s}$) and Halley's comet (for which $l_{1} = 8.7830 \times 10^10 m$ and $v_{1} = 5.4529 \times 10^4 \frac{m}{s}$). Among other things you should find that the orbital period of the Earth is one year and that of Halley's comet is about 76 years.

## **Physics Explication**

##**Physics Solution**