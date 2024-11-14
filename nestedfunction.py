# nested function
def outer_function(name):
    def inner_function():
        print('Hello', name)
    inner_function()

outer_function('John') # Hello John