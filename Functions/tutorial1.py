'''
    This is an extremely basic look at how Python works and how to create
    a simple function. This may be too much explanation and
    detail but it's better than nothing.

    Throughout these tutorials you will find lots of these coloured "block
    comments" and # comments. This may look messy but it's better to have 
    things explained around actual code than to go through loads of theory.

    The biggest feature of Python that you need to be aware of is that it
    is a tab sensitive language. Meaning that unlike C you can't just write
    all of your code out on one line. It makes it for a much more nicely
    structured read. But one of the most common errors you will come across
    will be "indentation errors", meaning that your tabs are wrong.

    So to start off there's always three main parts to a Python program:
        - Library imports
        - Function initialisation (creating functions to be called later)
        - Calling the functions you've created

    This simple script will follow those 3 steps to create a simple print
    to screen program.
    The start of the script is always where the libraries are imported to
    be used later on. But imports and libraries can be explained later on.
'''
# import libraries
import time     # example import

'''
    Here we will create a skeleton function to start off.
    This function takes no parameters. This means between the ()
    is empty.
'''
# write functions
def function():
    print "test"
	
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

    Expected output: test
'''
