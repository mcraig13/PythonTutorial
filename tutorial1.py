'''
	This is an extremely basic look at how Python works and how to create
	a simple function. These block comments will explain best in detail 
	between the code how it works. This may be too much explanation and
	detail but it's better than nothing.
	
	So to start off there's always three main parts to a Python program:
		- Library imports
		- Function initialisation (creating functions to be called later)
		- Calling the functions you've created
	
	This simple script will follow those 3 steps to create a simple print
	to screen program.
	The start of the script is always where the libraries are imported to
	be used later on.
'''
# import libraries
import time
import sys

'''
	Here you can also set variables that can be used anywhere in this script.
	This isn't a pretty good style to use but and it is usually better to keep
	everything localised in functions. There will be an example of that later.
'''	
anotherTest = "another test"

'''
	Here we will create a skeleton function to start off.
	This function takes no parameters. This means between the ()
	is empty.
'''
# write functions
def function():
	print "test"
	
def parameter_function_0(lastTest):
	print lastTest
	
def parameter_function_1(anotherTest):
	lastTest = "last test"		# a variable can also be declared inside a function before being used
	parameter_function_0(lastTest)		# Here the function creates the parameter before sending it into another
	multiple_parameter_function(anotherTest, lastTest)
	print anotherTest
	
def multiple_parameter_function(anotherTest, lastTest):
	print anotherTest, lastTest
	
'''
	Now that the functions are created. We can call them. Any function 
	calls must always be done at the bottom of the script as it 
	needs to initialise the functions first before it can call them
'''
# call functions
function()		# generic function call
parameter_function_1(anotherTest)		# function call with a parameter

'''
	This will call the different functions and print out to the console
'''
