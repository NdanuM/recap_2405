name = "Joe"

def greeting():
    print(f"Hello, {name}")
greeting()

name = "Joe"

def greeting(name):
    print(f"Hello, {name}")
greeting("Sophie")

friend = 'Jane'

def quote():
    print(f"{friend} is a true friend")

quote()

# def practicing_function_scope():
#   im_trapped_in_the_function = "You can't access me outside this function!"

# print(im_trapped_in_the_function)

change_the_world = "change yourself"

def change_yourself():
    change_the_world = "world changed"

change_yourself()

change_the_world = "change yourself"

def change_yourself():
    global change_the_world
    change_the_world = "world changed"

change_yourself()

print('Hello world')

change_the_world = "change yourself"

def change_yourself():
    change_the_world = "world changed"
change_yourself()
print(change_the_world)

change_the_world = "change yourself"

def change_yourself():
    global change_the_world
    change_the_world = "world changed"
change_yourself()
print(change_the_world)
