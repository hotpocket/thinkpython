

# 2.2 Variable names
"""
42invalid_variable
invalid_variable@
# invalid, class is reserved
class

Python 3 has these keywords:
False    class  finally   is
return   None   continue  for
try      True   def       from
nonlocal while  and       del
global   not    with      as
elif     if     or        yield
assert   else   import    pass
break    except in        raise
lambda

Statements have effects and generally not values
Expressions have values but not effects generally
"""

# 2.6 String operators
# operators don't operate on strings but there are 2 exceptions, + and *

# Concatenation
join_this = 'join ' + 'this'
print('join_this = ' + join_this)

# Repetition
buffalo = 'buffalo '*8
print("Our friend the buffalo sentence: " + buffalo)

# Exercises
x = y = 1   # is valid syntax
print("x + y = " + str(x + y))
z = 5;  # semicolon has no effect

# implicit multiply like in math e.g. xy   is an error  "NameError: name 'xy' is not defined"

# 4/3 * pi * r**3    =  volume of sphere

# sphere of radius 5
print("Volume of sphere with radius 5 = " + str( (4/3) * 3.14159 * 5**3))

"""
3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
"""

hour = 6
minutes = 52
seconds = 0

seconds += 15 + (3*12) + 15
minutes += 8 + (3*7) + 15

minutes += seconds // 60
seconds = seconds % 60

hour += minutes // 60
minutes = minutes % 60

hour += (minutes // 60)
hour = hour % 24

# Yet another way to do string interpolation ... 
print('you finish your run at %02d:%02d:%02d' % (hour,minutes,seconds))




# EOF
