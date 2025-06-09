from itertools import chain

crazy_list = [9, [10, [11, [12, [13, [14, [15]]]]]]], [16, [[17, [18, [19, [20, 21]]]]]]

result = list(chain.from_iterable(crazy_list))
print(result)

def sort_list(lst):
    for element in lst:
        if isinstance(element, list):
            yield from sort_list(element)
        else:
            yield element


ready_list = sort_list(crazy_list)

