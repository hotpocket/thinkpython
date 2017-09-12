import turtle

bob = turtle.Turtle()
print(bob)

"""   Go Bob, it's your birthday!
                       ____,------------------,______
                   ___/    \            /            \_____
                __/         \__________/              \___ \___
  ,^------.____/\           /          \              /   `----\_
  | (O))      /  \_________/            \____________/         \ \
  \_____,--' /   /         \            /            \          \ \
    \___,---|___/_______,---`----------'----,_________\__________\_\
              /  :__________________________/  :___________________/
             /   :          /   :          /   :          /   :
            /    :         /    :         /    :         /    :
        (~~~     )     (~~~     )     (~~~     )     (~~~     )
         ~~~~~~~~       ~~~~~~~~       ~~~~~~~~       ~~~~~~~~
"""

# draw a square
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)

for i in range(4):
    print("Hello!")

# another way to draw the square drawn above
# consequently draws a connected square :)
for i in range(4):
    bob.fd(100)
    bob.lt(90)

# Exercises
"""
Write a function called square that takes a parameter named t , which is a turtle. It
should use the turtle to draw a square.
Write a function call that passes bob as an argument to square , and then run the
program again.
"""

# clears all work done by bob :'(
bob.reset()
"""  Sad Bob :(
  _  .----.
 (_\/      \_,
   'uu----uu~'
"""

def square(t,len):
    t.fd(len)
    for i in range(3):
        bob.lt(90)
        bob.fd(len)

# sponge bob?
square(bob,111)
bob.reset()  # sad panda

"""
Make a copy of square and change the name to polygon . Add another parameter
named n and modify the body so it draws an n-sided regular polygon. Hint: The
exterior angles of an n-sided regular polygon are 360/n degrees.
"""

def polygon(turtle,len,sides):
    turn_angle = 360/sides
    for i in range(sides):
        turtle.fd(len)
        turtle.lt(turn_angle)

polygon(bob,30,15)  # increase arg2 to make more circle like
bob.reset()

import turtle
sue = turtle.Turtle()

import math
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

circle(sue,10)
#  Turtle power !
turtle.mainloop()
