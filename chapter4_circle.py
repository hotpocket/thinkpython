import turtle
import math

sue = turtle.Turtle()

def polygon(turtle,len,sides):
    turn_angle = 360/sides
    for i in range(sides):
        turtle.fd(len)
        turtle.lt(turn_angle)

def circle(turtle,radius):
    len = 0
    nsides = 0
    # len * nsides = 2*math.pi*radius
    # so divide both sides by len & get nsides
    # ... so len decreases w/ #sides
    # ... as radius increased #turns increases and len decreases
    # ... so #sides is denominator because as it approaches infinity len approaches 0
    # ... because we have 2 unknowns and 1 equation let's assume len = 1 then we can eliminate it & solve for nsides
    len = 1
    nsides = int(2*math.pi*radius)
    polygon(turtle,len,nsides)

# this gets slow as radius gets large ... we can do better
#circle(sue,100)

def circle2(turtle,radius):
    # draw a graph contrasting sides vs len to determine best
    nsides = int((radius * 4) / (radius % 40))
    print(nsides, radius)
    # we need to define nsides as a function of radius.
    len = int((2*math.pi*radius) / nsides)
    # whatever we * len by we need to / nsides by
    # now that nsides is fixed, we must compute len
    polygon(turtle,len,nsides)  # turtle , len, sides


##   this is far from perfect ,    eval later once ideas have been digested
# sue.reset()
circle2(sue,100)

#  Turtle power !
turtle.mainloop()
