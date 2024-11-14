#using the decorator function
def my_decorator(func):
    def wrapper(name):
        print("Something is happening before the function is called.")
        func(name) #notice in the decorator function, the outer function parameter is used as the function itself
        print("Something is happening after the function is called.")
    return wrapper
@my_decorator
def say_hello(name):
    print("Hello", name)
say_hello("John")
# this is how you can decorate the function using the decorator function. this is useful in django framework