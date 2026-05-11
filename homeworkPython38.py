
class MoneyError(ValueError):
    """
    Исключение для ошибок, связанных с денежными операциями.

    Используется при:
    - попытке внести некорректную сумму
    - попытке снять больше денег, чем есть на счёте
    """
    pass



class BankAccount:
    """
    Класс банковского счёта.

    Хранит:
    - имя владельца счёта
    - текущий баланс
    - историю операций

    Поддерживает:
    - пополнение счёта
    - снятие средств
    - просмотр баланса
    - получение истории операций
    """

    def __init__(self, name:str, money:float):
        """
        Создаёт банковский счёт.

        :param name: имя владельца счёта
        :param money: начальный баланс
        """
        self.__name = name
        self.__balance = money
        self.__history = []


    @property
    def history(self):
        """
        Возвращает историю операций по счёту.

        :return: список операций
        """
        return self.__history.copy()


    def deposit(self, money:float):
        """
        Пополняет баланс счёта.

        :param money: сумма пополнения
        :raises MoneyError:
            если сумма меньше или равна 0
        """
        if money <= 0:
            raise MoneyError("Must be bigger then 0")

        self.__balance += money
        self.__history.append(f"Deposit: {money}")


    def withdraw(self, money:float):
        """
        Снимает деньги со счёта.

        :param money: сумма снятия
        :raises MoneyError:
            если средств недостаточно
        """
        if money > self.__balance:
            raise MoneyError("Not enough money")

        self.__balance -= money
        self.__history.append(f"Withdraw: {money}")


    def balance(self):
        """
         Возвращает текущий баланс счёта.

         :return: текущий баланс
         """
        return self.__balance


#-----------------------------------------------------------------------------------------------------------------------

a = BankAccount("Ivan", 1200)


print(a.balance())
a.deposit(200)
print(a.balance())
a.withdraw(400)
print(a.balance())

try:
    a.withdraw(100000000000)
except MoneyError as e:
    print(e)

try:
    a.deposit(-3)
except MoneyError as e:
    print(e)

print(a.balance())
print(a.history)