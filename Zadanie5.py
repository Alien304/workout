from random import random, randrange
from unittest import skip


def overlap():
    mya = [randrange(0, 100, 10) for i in range(20)]
    myb = [randrange(0, 100, 10) for i in range(10)]
    result = []
    for x in mya:
        for y in myb:
            if x is y not in result:
                result.append(x)
    print(f"Lista A: {mya} ")
    print(f"Lista A: {myb} ")
    print(result)

overlap()