# Functions
import math
print(math)

# playing w/ some math functions
signal_power = 2.5
noise_power = 1.5
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
print("ratio: {}   decibels: {}".format(ratio,decibels))

radians = 0.7
height = math.sin(radians)
print("rads = %s height = %s" % (radians, height))  # messin w/ string formatting

degrees = 45
radians = degrees / 180.0 * math.pi
print("radians = 45/180 * math.pi\n\tmath.sin(radians) = %s" % (math.sin(radians)))

print("math.sqrt(2) / 2 = %s" % (math.sqrt(2)/2))

# composition ... basic stuff ...
x = math.sin(degrees / 360.0 * 2 * math.pi)
print("x = %s" % (x))
x = math.exp(math.log(x+1))
print("x = %s" % (x))

def refrain():
    print("I'm a lumberjack and I'm ok")
    print("I work all night and I sleep all day")
    # ...

refrain()
print(refrain)

def lumberjack_song():
    refrain();
    print("I go to work, I eat my lunch, I go to the lavetory.")
    # ...
    refrain()

print()
lumberjack_song()

# <tangent_city>
import json
print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
print(json.dumps("\"foo\bar"))
print(json.dumps(u'\u1234'))
print(json.dumps('\\'))
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
# </tangent_city>

# "Tracebacks" or stack diagrams or stack traces ...
def call2(z):
    print(call1_var)

def call1(x):
    call1_var = str(x) + " more"
    call2(call1_var)

# generates a stack trace
## call1('something')


# Exercises

# Exercise 3.2.
# Solution: http://thinkpython2.com/code/do_four.py

def do_twice(f, value):
    f(value)
    f(value)

def print_twice(s):
    print(s)
    print(s)

def do_four(f,a):
    do_twice(f,a)
    do_twice(f,a)

do_twice(print_twice, 'do_twice print_twice')  # prints 4 times
print('')
do_four(print,'do_four print')   # using print_twice as in the solution would print 8 times, while not wrong per instructions it seems wrong so i used print here


# Exercise 3.3
# Solution: http://greenteapress.com/thinkpython2/code/grid.py

def draw_grid(rows,cols):
    col_width = 4
    row_height = 4
    row_split = "+" + (" -"*col_width + " +")*cols + "\n"
    row = ("|" + (" "*col_width*2 + " |")*cols + "\n")*row_height
    all_rows = row_split + (row + row_split)*rows
    print(all_rows)

draw_grid(4,4)




# EOF
