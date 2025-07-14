"""Задача: найти и исправить 2 ошибки в функции."""


def update_list(lst: list[int]=None, value_to_increase: int=1) -> list[int]:
    """Модифицирует список.

    Принимает на вход список и значение, на которое необходимо увеличить кадждый элемент списка.
    В конец списка добавляет сумму всех элементов списка.

    Args:
        lst (list[int]): исходный список
        value_to_increase (int): значение, на которое необходимо увеличить каждое значение списка

    Returns:
        list: итоговый список
    """
    if lst is None:
        lst = []
    for i in range(len(lst)):
        lst[i] += value_to_increase
    sum_ = sum(lst)
    lst.append(sum_)
    return lst

if __name__ == '__main__':
    print(update_list([1, 2, 3], 2))

