 # creating the global varaible with the global keyword. this is to be done if you want to create the global variable inside a function
def function():
    global x
    x = "fantastic"
function()
print("Python is " + x)