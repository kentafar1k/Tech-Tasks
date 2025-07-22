"""
Условие: Банкомат инициализируется набором купюр и умеет выдавать купюры для заданной суммы либо отвечать отказом.
При выдаче купюр списываются с баланса банкомата. Допустимые номиналы 50 10 500 1000 5000.
Определить сигнатуры методов банкомата. в классе ATM.

Методы. Реализовать основной метод выдачи денег, который возвращает, сколько купюр и какое количество выдано относительно суммы введённой.

Входные данные:
atm = Atm({50: 50, 100: 20, 500: 1, 1000: 20, 2000: 0, 5000: 0})
"""


class Atm:
    def __init__(self, nominal):
        self.nominal = nominal

    def get_balance(self):
        total = 0
        for key, value in self.nominal.items():
            total += key * value
        return total

    def get_money(self, summ):
        if summ > self.get_balance():
            raise Exception

        while True:
            for key, value in self.nominal.items()[-1:]:


atm = Atm({50: 50, 100: 20, 500: 1, 1000: 20, 2000: 0, 5000: 0})
print(atm.get_balance())
atm.get_money(26000)