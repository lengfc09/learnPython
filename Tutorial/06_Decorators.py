# Decorators: preliminaries
def outer_fun():
    message = "hi"
    def inner_fun():
        print(message)
    return inner_fun

my_func = outer_fun()
my_func()


def outer_fun2(msg):
    message = msg
    def inner_fun():
        print(message)
    return inner_fun


hi_fun = outer_fun2('Hi')
bye_fun = outer_fun2("Bye")

hi_fun()
bye_fun()


# Examples1-----------------
def decorator_function(message):
    def wrapper_function():
        print(message)
    return wrapper_function


# Examples2------------------decorate functions!
def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function


def display():
    print("test for decoration!@!")

decorated_display = decorator_function(display)
decorated_display()
print()

# Examples3------------------add some functionality to the exisiting one


def decorated_function2(original_function):
    def wrapper_function():
        # do some thing new here!
        print("some thing happened before !{}".format(original_function.__name__))
        return original_function()
    return wrapper_function

decorated_display2 = decorated_function2(display)
decorated_display2()
print()

# Examples4------------------ a simple syntax
# which is equivalent to: display=decorated_function2(display)


@decorated_function2
def display22():
    print("display function ran")

display22()
print()

# ADD some args: (*args,**kwargs)


def decorated_function3(original_function):
    def wrapper_function(*args, **kwargs):
        # do some thing new here!
        print("some thing happened before !{}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


@decorated_function3
def display33(name, age):
    print("display33 ran with arguments ({} ,{})".format(name, age))

display33("peter", 26)
print()

# for logging, and timing!!!


def my_logger(original_function):
    import logging
    import time
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info("ran with args: {}, and kwargs: {}".format(args, kwargs))
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        logging.info("{} ran in: {} seconds".format(original_function.__name__, t2))
        return result
    return wrapper


@my_logger
def display44(name, age):
    print("display44 ran with arguments ({} ,{})".format(name, age))

display44("hank", 26)
print()

# for timing


def my_timer(original_function):
    import time
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in: {} seconds".format(original_function.__name__, t2))
        return result
    return wrapper


@my_timer
def display55(name, age):
    print("display55 ran with arguments ({} ,{})".format(name, age))

display55("hank", 26)
print()
