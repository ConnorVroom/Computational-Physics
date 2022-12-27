# **Exercise 2.2: Altitude of a satellite**

## **Question:**
A satellite is to be launched into a circular orbit around Earth so that it orbits the planet once every T seconds.

a) Show that the altitude h above the Earth's surface that the satellite must have is 
$$h = \left(\frac{GMT^2}{4\pi^2}\right)^\frac{1}{3} - R$$

where $G = 6.67\times10^{-11} \frac{m^3}{kgs^2}$ is Newton's gravitational constant, $M = 5.97\times10^{24} kg$ is the mass of the Earth, and $R = 6371 km$ is its radius.  

b) Write a program that asks the user to enter the desired value of T and then calculates and prints out the correct altitude in meters.  
 
  
c) Use your program to calculate the altitudes of satellites that orbit the Earth once a day(so-called "geosynchronous" orbits), once every 90 minutes, and once every 45 minutes. What do you conclude from the last of these calculations?


d)Technically a geosynchronous satellite is one that orbits the Earth once per *sidereal day*, which is 23.93 hours, not 24 hours. Why is this? And how much difference will it make the the altitude of the satellite?
## **Useful Resources:**
https://en.wikipedia.org/wiki/Kepler%27s_laws_of_planetary_motion

The wikipedia has a good introduction on what Kepler's laws are and some derivation of them. It also has nice figures for Kepler's second law. 

## **Physics Solution:**

Since the physics behind this question is a question this will just be the  solution to the problems a), c), and d).

###**a)**###
The equation in part A might look a bit complicated but it is Kepler's third law in terms of a circular orbit around earth. The third law states that the square of the orbital period is proportional to the cube of the semi-major axis ie $P^2 = Ka^3$. 

we can rewrite our equation from a) to look like Kepler's third law by first combining the altitude and the earth's radius.
$$T^2\left(\frac{GM}{4\pi^2}\right) = \left(h+R\right)^3$$

we can now move our constant factors over to result in an equation that looks like Kepler's third law.
$$T^2 = \left(\frac{4\pi^2}{GM}\right)(h+R)^3$$
which looks like $P^2 = Ka^3$ where $a = h + R$ and $K = \frac{4\pi^2}{GM}$

But where does $K = \frac{4\pi^2}{GM}$ really come from? 

We can derive it from Kepler's second law which states that a satellite orbiting around a planet in a ellipse generates a line running from a planet to a satellite at time $t_{0}$ sweeps out an area when the satellite moves to a new time $t$ at any point on the elliptical path the area sweeps out by moving the same time $t_{0}$ to $t$  is equal. 

in mathematical terms Kepler's second law is 

$$\frac{dA}{dt} = \frac{L}{2m}$$

where L is the angular momentum of the satellite.

now to sweep out the total area A our time must be equal to the total time to go around the ellipse or the period
$$\frac{\pi ab}{T} = \frac{L}{2m}$$

since the general solution to kepler's third law is elliptical we will continue with our elliptical model

the semi-minor axis is equal to $b^2 = a^2(1-e^2)$
lets square our second law 

$$\frac{\pi^2 a^2b^2}{T^2} = \frac{L^2}{4m^2}$$

and plug in our semi-minor axis identity

$$\frac{\pi^2 a^4(1-e^2)}{T^2} = \frac{L^2}{4m^2}$$

The angular momentum square over the mass of our satellite squared is equal to $\frac{L^2}{m^2} = G(M+m)a(1-e^2)$

since $M >> m$ usually we can write $M + m = M$
thus our second law equation becomes

$$\frac{\pi^2 a^4(1-e^2)}{T^2} = \frac{GMa(1-e^2)}{4}$$

we can now write our second law equation in terms of the third law
$$T^2 = \frac{4\pi^2a^3}{GM}$$

where a is the semi-major axis length from the center of mass of the planet to the satellite. 

we can see from here the equation from part a) falls out nicely. 

###**c)**### 
for the geosynchronous orbits our period is 24 hours so changing that to seconds we get 86400 s. now we can use that period in the equation from part a) to get 35136 km

for the 90 minutes its the same so our period is 5400 s and the altitude is 166 km 

for 45 minutes or 2700 s the altitude is -2252km wait what we have a negative altitude that can not be right? 

it is not the correct altitude for Earth because kepler's laws are applied to point masses when near earths surface the altitude for a given period will be wrong but it does work well for large orbits like a geosynchronous orbit. 

###**d)**###
we can do the same thing as in problem c) as in this problem except our period is now 23.93 hours or 86148s the altitude then is 35055km the difference between the sidereal day and our 24 hour day is 81km or about 0.2% of the total altitude.