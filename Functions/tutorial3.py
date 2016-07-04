'''
    This final example will show how multiple parameters can be used with functions
    and also show functions calling each other.
'''
# import libraries
import time     # example import

# variables
anotherTest = "another test"

# write functions

'''
    It might look like a lot is going on in this function but I wanted to look at a
    few things at once here. So we've looked at a simple function call and then a
    function call with a parameter. This one will do a little more.
    
    This function will take a parameter, create it's own local variable and then pass
    that variable into a second function that will be printed out on the screen.
    The main key here is that instead of printing it's own result it will return it
    instead. This means that where it is being called from can decide what to do with
    what's being returned.
    
    In this case we're returning anotherTest to the point of call and we will just 
    simply print it out.
'''
def parameter_function(anotherTest):
    # local function variables
    lastTest = "last test"		# a variable can also be declared inside a function before being used

    # function working
    multiple_parameter_function(anotherTest, lastTest)      # this time passing two parameters - more can be added

    return anotherTest      # return will send the thing it returns to the point at which the function was called from
	
def multiple_parameter_function(anotherTest, lastTest):
    print anotherTest, lastTest
    
print parameter_function(anotherTest)       # notice we are printing this function as it is returning a value to us
