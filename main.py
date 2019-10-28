from sorters import BCIS
from random import randrange


def seed_random(size, min, max):

    array = []
    for i in range(0, size):
        array.append(randrange(min, max))
    return array


bcis_sorter = BCIS()
array = seed_random(100, 0, 500)

bcis_sorter.sort(array, 0, len(array)-1)


