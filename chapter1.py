
# http://greenteapress.com/thinkpython2/thinkpython2.pdf

# 1.3
print("Hello World!")

# 1.4 Arithmetic
# ** is exponent in python, ^ is bitwise XOR
print("8**2 = " + str(8**2))

# 1.5 Types
print(type(2))
print(type(40.0))
print(type('40.0'))
x = 1,000,000  # tuple, not a a number
print(type(x))

# 1.6 formal vs natural languages
# formal languages have strict syntax pertaining to tokens and structure
# formal = no ambiguity, less verbose, mean exactly what they say
# natural/informal = contextual ambiguity, more verbose, idiom and metaphor ... not necessarly means exactly what is said.

# Exercise 1.1
"""
1) This is ok in python2, not ok in python3 where print is a function
print "Hello World!"

    SyntaxError: Missing parentheses in call to 'print'

2) leaving out quotation marks when printing a string
print(Hello World)

    SyntaxError: invalid syntax

3) sign before number
print(2++2)

    Prints 4 , seemingly w/o error

4) leading zeros are ok in math but not python
print(02)
    SyntaxError: invalid token

5) two values w/o operator between them
print(2 2)
    SyntaxError: invalid syntax
"""

# Exercise 1.2
"""
1. How many seconds are there in 42 minutes 42 seconds?
2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per
mile in minutes and seconds)? What is your average speed in miles per hour?
"""
# default seperator is space, so we can use commas and treat each string as an arg and omit leading & trailing spaces
print("There are" , str(42*60+42) , "seconds in 42m 42s")
# with str concat we create each string in memory & then output once final string is constructed (not memory friendly)
print("There are " + str(10*1.61) + " miles in 10 kilometers")

# variable naming detour ...  https://google.github.io/styleguide/pyguide.html#Naming
# module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name
miles = 10*1.61
seconds = 42*60+42
seconds_per_mile = int(seconds/miles)
seconds_part_per_mile = seconds_per_mile % 60
minutes_part_per_mile = seconds_per_mile // 60

# I aparently don't have python 3.6 yet ... i'm on 3.5 ...
# print(f'seconds in race are: {seconds_in_race}')

# another way to do string interpolation
print('Average speed in 42m 42s 10k race in min_sec/mi is {}m {}s per mile'.format(minutes_part_per_mile, seconds_part_per_mile))
mph = miles / (seconds / (60*60))
print('Average mph is {} ... yes, you are hauling ass'.format(mph))






""""""
