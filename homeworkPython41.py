import pymysql


class Database:
    """
    Класс для работы с MySQL базой данных.

    Отвечает за:
    - создание подключения
    - выполнение SQL-запросов
    - закрытие подключения
    """

    def __init__(self, env):
        """
        Создаёт подключение к БД.

        Args:
            env (dict): параметры подключения:
                - host
                - user
                - password
                - database
                - cursorclass
        """

        self.connection = pymysql.connect(**env)

    def execute(self, query, params=None):
        """
        Выполняет SQL-запрос и возвращает результат.

        Args:
            query (str): SQL-запрос
            params (dict | None): параметры запроса

        Returns:
            list[dict]: результат fetchall()
        """

        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()

    def close(self):
        """
        Закрывает подключение к базе данных.
        """

        self.connection.close()


class City:
    """
    Класс для работы с таблицей city.

    Позволяет:
    - получать города по названию страны
    - получать города по индексу страны
    """

    def __init__(self, db):
        """
        Args:
            db (Database): объект подключения к БД
        """

        self.db = db

    def cities_in_country_by_name(self, country):
        """
        Возвращает список городов выбранной страны.

        Args:
            country (str): название страны

        Returns:
            list[dict]: список городов и населения
        """

        return self.db.execute("""
        SELECT c.Name, c.Population 
        FROM city AS c 
        JOIN country AS co 
        ON c.CountryCode = co.Code 
        WHERE co.Name = %(country_name)s
        """, {"country_name": country})

    def cities_in_country_by_index(self, ind):
        """
        Возвращает список городов страны по её индексу.

        Индекс соответствует позиции страны
        в текущем порядке строк таблицы country.

        Args:
            ind (str | int): номер страны

        Returns:
            list[dict]: список городов и населения
        """

        return self.db.execute("""
            SELECT c.Name, c.Population
            FROM city AS c
            JOIN country AS co
            ON c.CountryCode = co.Code
            WHERE co.Name = (
                            SELECT Name
                            FROM country
                            LIMIT 1 OFFSET %(country_id)s
                            )
        """, {"country_id": int(ind) - 1})


class Country:
    """
    Класс для работы с таблицей country.
    """

    def __init__(self, db):
        """
        Args:
            db (Database): объект подключения к БД
        """

        self.db = db

    def get_all_countries(self):
        """
        Возвращает список всех стран.

        Returns:
            list[dict]: список стран
        """

        return self.db.execute("""
            SELECT Name
            FROM country
        """)


env = {
    "host": "ich-db.edu.itcareerhub.de",
    "user": "ich1",
    "password": "password",
    "database": "world",
    "cursorclass": pymysql.cursors.DictCursor
}


db = Database(env)
co = Country(db)
c = City(db)


for index, row in enumerate(co.get_all_countries(), start=1):
    print(f"{index}. {row['Name']}")


user_country = input('\nEnter country: ').strip()


if user_country.isdigit():

    for index, row in enumerate(
            c.cities_in_country_by_index(user_country),
            start=1):

        print(index, row["Name"], "-", row["Population"])


else:

    for index, row in enumerate(
            c.cities_in_country_by_name(user_country),
            start=1):

        print(index, row["Name"], "-", row["Population"])


db.close()