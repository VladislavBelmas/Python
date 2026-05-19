from datetime import datetime
from functools import total_ordering



@total_ordering
class Email:
    """
    Класс электронного письма.

    Поддерживает:
    - сравнение писем по дате
    - получение длины текста письма
    - проверку наличия текста
    - строковое представление письма
    """

    def __init__(self, sender, recipient, subject, body, date):
        """
        Создаёт объект письма.

        :param sender: отправитель письма
        :param recipient: получатель письма
        :param subject: тема письма
        :param body: текст письма
        :param date: дата отправки письма
        """
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = date

    def __eq__(self, other):
        """
        Сравнивает письма по дате отправки.

        :param other: объект Email
        :return: True если даты равны
        """
        if not isinstance(other, Email):
            return NotImplemented

        return self.date == other.date

    def __lt__(self, other):
        """
        Проверяет, было ли письмо отправлено раньше другого.

        :param other: объект Email
        :return: результат сравнения дат
        """
        if not isinstance(other, Email):
            return NotImplemented

        return self.date < other.date

    def __len__(self):
        """
        Возвращает длину текста письма.

        :return: количество символов в body
        """
        return len(self.body)

    def __bool__(self):
        """
        Проверяет, содержит ли письмо текст.

        :return: True если body не пустой
        """
        return len(self.body.strip()) > 0

    def __str__(self):
        """
        Возвращает строковое представление письма.

        :return: строка с данными письма
        """
        return (
            f"From: {self.sender}\n"
            f"To: {self.recipient}\n"
            f"Subject: {self.subject}\n"
            f"- {self.body} -"
        )



e1 = Email("alice@example.com", "bob@example.com", "Meeting",
           "Let's meet at 10am", datetime(2024, 6, 10))

e2 = Email("bob@example.com", "alice@example.com", "Report",
           "", datetime(2024, 6, 11))

print(e1)
print(e1)
print(e2)
print("Length:", len(e1))
print("Has text:", bool(e1))
print("Is newer:", e2 > e1)


#-----------------------------------------------------------------------------------------------------------------------

@total_ordering
class Money:
    """
    Класс денежной суммы.

    Поддерживает:
    - сравнение денежных объектов
    - сложение
    - вычитание
    - строковое представление
    """

    def __init__(self, amount):
        """
        Создаёт денежный объект.

        :param amount: сумма денег
        """
        self.amount = amount

    def __eq__(self, other):
        """
        Проверяет равенство денежных сумм.

        :param other: объект Money
        :return: результат сравнения
        """
        if not isinstance(other, Money):
            return NotImplemented

        return self.amount == other.amount

    def __lt__(self, other):
        """
        Сравнивает денежные суммы.

        :param other: объект Money
        :return: результат сравнения
        """
        if not isinstance(other, Money):
            return NotImplemented

        return self.amount < other.amount

    def __add__(self, other):
        """
        Складывает денежные суммы.

        :param other: объект Money
        :return: новый объект Money
        """
        if not isinstance(other, Money):
            return NotImplemented

        return Money(self.amount + other.amount)

    def __sub__(self, other):
        """
        Вычитает денежные суммы.

        Отрицательный результат заменяется на 0.

        :param other: объект Money
        :return: новый объект Money
        """
        if not isinstance(other, Money):
            return NotImplemented

        result = self.amount - other.amount

        if result < 0:
            result = 0

        return Money(result)

    def __str__(self):
        """
        Возвращает строковое представление суммы.

        :return: строка с денежной суммой
        """
        return f"${self.amount}"



money1 = Money(100)
money2 = Money(50)
print(money1 + money2)
print(money1 - money2)
print(money2 - money1)