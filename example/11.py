print('this is {{hello}}'.format())

def format_test():
    a = 33
    print('a = {:b}'.format(a))
    print('a = {:c}'.format(a))
    print('a = {:d}'.format(a))
    print('a = {:o}'.format(a))
    print('a = {:x}'.format(a))
    print('a = {:X}'.format(a))
    print('a = {:n}'.format(a))
    b = 0.122132
    print('a = {:e}'.format(b))
    print('a = {:E}'.format(b))
    print('a = {:f}'.format(b))
    print('a = {:F}'.format(b))
    print('a = {:g}'.format(b))
    print('a = {:G}'.format(b))
    print('a = {:%}'.format(b))

def fstring_test():
    a =123.123
    print(f'{a:e}')
    print(f'{a:#0e}')

if __name__ == '__main__':
    fstring_test()