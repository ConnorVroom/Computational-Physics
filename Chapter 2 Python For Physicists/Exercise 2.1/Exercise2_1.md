# **Exercise 2.1: Another ball dropped from a tower**

## **Question:**
A ball is again dropped from a tower of height h with initial velocity zero. Write a program that asks the user to enter the height in meters of the tower and then calculates and prints the time the ball takes to hit the ground, ignoring air resistance. Use your program to calculate the time for a ball dropped from a 100m high tower. 

## **Physics Explication**
The easiest way to solve this problem is with an equation for constant acceleration in 1 directional motion. If you don't know what those are, or don't remember them like I did, we can derive them!
###**First Equation of Constant Acceleration**
The basic definition of acceleration is the second time derivative of position or the first time derivative of velocity: 

$$ a = \frac{\mathrm d v(t)}{\mathrm d t} $$

if we integrate both sides:
$$ \int_0^t a\text{ }\mathrm{d}t = \int_{v_{0}}^v \mathrm{d}v$$

we can compute the integrals and solve for $v$ to get: 

$$ v(t) = at + v_{0} $$

This is our first equation of constant acceleration. 

###**Second Equation of Constant Acceleration**
we  can derive our second equation with which is our definition of velocity:

$$v = \frac{\mathrm d x(t)}{\mathrm d t}$$

we can now integrate our velocity equation to find our position equation

$$ \int_0^t at+v_{0}\text{ } \mathrm{d}t = \int_{x_{0}}^x \mathrm{d}x$$

solving for $x$ 

$$ x(t) = \frac{at^2}{2} + v_{0}t + x_{0} $$

this is technically all we need for our problem but for completeness we will continue to derive the other equations. Also to note the 2 equations above describes our system in full ie we know how the acceleration, velocity and position are affected by time. The last two equation are useful because they can reduced dependencies on time or acceleration. 

###**Third Equation of Constant Acceleration**

for this equation we can solve the first equation for $t$ and eliminate $t$ from the second equation if you solve for $t$ the equation yields:

$$t = \frac{v - v_{0}}{a}$$

inserting the equation we found for $t$ into the second equation:

$$x = \frac{a(v-v_{0})^2}{2(a)^2} + v_{0} \frac{v-v_{0}}{a} + x_{0}$$

expanding

$$x - x_{0} = \frac{v^2 - 2vv_{0} + v_{0}^2}{2a} + \frac{vv_{0} - v_{0}^2}{a} $$

multiply both sides by $2a$

$$2a(x-x_{0}) = v^2 - 2vv_{0} + v_{0}^2 + 2vv_{0} - 2v_{0}^2$$

rearranging

$$2a(x-x_{0}) + v_{0}^2 = v^2$$

this is the third equation but we can write it in a more commonly seen way by setting $x-x_{0} = \Delta x$

thus:
$$v^2 = v_{0}^2 + 2a\Delta x $$

###**Forth Equation of Constant Acceleration**
for this equation we want to eliminate a from equation 2 to do this we can once again solve equation 1 for $a$.

$$a = \frac{v-v_0}{t}$$

now replacing $a$ in equation 2 of our equation grants

$$x = \frac{(v-v_{0})t^2}{2t} + v_{0}t + x_{0}$$

$$\Delta x = \frac{vt}{2} - \frac{v_{0}t}{2} + v_{0}t$$

$$\Delta x = \frac{1}{2}(v+v_{0})t$$

this is our final equation of constant acceleration these can be used for 1 dimensional motion with constant acceleration and are useful equation. 

##**Physics Solution**

for our case of a ball dropped from a tower of 100m with no initial velocity. the best equation for our problem is equation 2 because we know $x_{0} = 100m$, $x = 0m$, $v_{0} = 0 \frac{m}{s}$, and $a = -9.8 \frac{m}{s^2}$ inserting these values into equation 2 we get:

$$0 = \frac{-9.8t^2}{2} + 100$$

thus:
$$t = \sqrt\frac{200}{9.8} \approx 4.5s$$

that should be the the answer our code returns there will also be a test file with other examples for you to test your code with.