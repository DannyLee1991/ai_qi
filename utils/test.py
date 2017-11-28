import sys

def foo(func):
    print('decorator foo')
    return func


@foo
def bar():
    print('bar')

    print(sys._getframe().f_code.co_name)


bar()

# foo(bar())
