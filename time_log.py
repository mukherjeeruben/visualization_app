import timeit

start = None
stop = None


def code_init():
    global start
    start = timeit.default_timer()
    return


def execution_end():
    stop = timeit.default_timer()
    print('Total Execution Time : ', stop - start)
    return