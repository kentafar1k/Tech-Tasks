l =[[1, 2, 3], [4, 5], 6]  # -> [1, 2, 3, 4, 5, 6]


def flutten(lst) -> list:
    for elem in lst:
        if isinstance(elem, list):
            yield from flutten(elem)
        else:
            yield elem


print(list(flutten(l)))