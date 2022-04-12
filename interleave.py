from typing import Iterator



def interleave(*args) -> Iterator[any]:
    """
      This function  get some args as of parameter and has to zip the lists
      :param args:
    """
    yield [i for list_temp in zip(*args) for i in list_temp]

