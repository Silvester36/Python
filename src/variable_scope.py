
# local variable
def my_function():
    a = 5   
    print("Inside function:", a)

# global variable
x = 100   

def display():
    print("Inside function:", x)

display()
print("Outside function:", x)

# Enclosing Scope
def outer():
    x = "outer variable"

    def inner():
        print("Accessing from inner:", x)

    inner()

outer()

# Built-in functions
print(len("Hello"))