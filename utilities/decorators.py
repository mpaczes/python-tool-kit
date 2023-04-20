#  Python Tutorial: Decorators - Dynamically Alter The Functionality Of Your Functions 

# domkniecie - funkcja wewnetrzna widzi dane z funkcji zewnetrznej
def outer_function():
    message = 'hi'

    def inner_function():
        print(message)

    return inner_function()

outer_function()

# domkniecie inaczej
def outer_function_other(msg):
    # message = msg

    def inner_function():
        # print(message)
        print(msg)

    return inner_function

my_func = outer_function_other('hi')
my_func()

my_func = outer_function_other('bye')
my_func()

# decorator - to jest funkcja ktora przyjmuje inna funcje jako argument

# dekarator bez adnotacji
def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

def display():
    print('display function ran')

decorated_display = decorator_function(display)
decorated_display()

# dekarator z adnotacja
def decorator_function_adn(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

# bez parametrow
@decorator_function_adn
def display_other():
    print('display other function ran')

display_other()

# z parametrami
@decorator_function_adn
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Jack', 24)
