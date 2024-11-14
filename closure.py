# give me example of closure
def outer_function(msg):
    def inner_function():
        print(msg , "hello")
        return inner_function
name = outer_function('Hello')
print(name)
# so even if the value of inner_function is already executed, it still can be applied to outer function.