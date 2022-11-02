from time import time

def timerPrint(func):
    # This function prints formatted string showing execution time of the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.10f}s') # displays execution time to 10 d.p
        return result
    return wrap_func

