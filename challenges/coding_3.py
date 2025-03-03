def do_twice(f,s):
    f(s)
    f(s)
    
def print_twice(s):
    print(s)
    print(s)
    
do_twice(print_twice, 'spam')

def do_four(f, s):
    print_twice('spam')
    print_twice('spam')
