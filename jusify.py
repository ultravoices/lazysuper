def right_justify(s):
    s_var = len(s)
    print(' ' * (70 - s_var) + s)


def do_twice(f, x):
    f(x)
    f(x)

def print_twice(bruce):
    print(bruce)
    print(bruce)

def print_spam():
    print('spam')

def do_four(f, x):
    do_twice(f, x)
    do_twice(f, x)

do_four(print_twice, 'spam')