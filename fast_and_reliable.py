import time


def data_structure(structure):
    """
    The function returns the time that it takes to search the word 'zwitterion'
    in that file given.
    :param structure:The structure where we are searching
    :return:The average of time that it took to search the word 'zwitterion' 1000 times
    """
    start = time.time()

    for i in range(1000):
        while True:

            if 'zwitterion' in structure:
                break

    return (time.time() - start) / 1000
