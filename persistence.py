import sqlite3
import atexit
from dbtools import Dao
 
# Data Transfer Objects:
class Employee(object):
    id = object[0]
    name = object[1]
    salary = object[2]
    branche = object[3]

    def __str__(self):
        return f"{self.id}, {self.name}, {self.salary}, {self.branche}"

 
class Supplier(object):
    id = object[0]
    name = object[1]
    contact_information = object[2]

    def __str__(self):
        return f"{self.id}, {self.name}, {self.contact_information}"


class Product(object):
    id = object[0]
    description = object[1]
    price = object[2]
    quantity =object[3]

    def __str__(self):
        return f"{self.id}, {self.description}, {self.price}, {self.quantity}"


class Branche(object):
    id = object[0]
    location = object[1]
    number_of_employees = object[2]

    def __str__(self):
        return f"{self.id}, {self.location}, {self.number_of_employees}"



class Activitie(object):
    product_id = object[0]
    description = object[1]
    activator_id = object[2]
    date =object[3]

    def __str__(self):
        return f"{self.product_id}, {self.description}, {self.activator_id}, {self.date}"

 
#Repository
class Repository(object):
    def __init__(self):
        self._conn = sqlite3.connect('bgumart.db')
        self._conn.text_factory = bytes
        #TODO: complete
 
    def _close(self):
        self._conn.commit()
        self._conn.close()
 
    def create_tables(self):
        self._conn.executescript("""
            CREATE TABLE employees (
                id              INT         PRIMARY KEY,
                name            TEXT        NOT NULL,
                salary          REAL        NOT NULL,
                branche    INT REFERENCES branches(id)
            );
    
            CREATE TABLE suppliers (
                id                   INTEGER    PRIMARY KEY,
                name                 TEXT       NOT NULL,
                contact_information  TEXT
            );

            CREATE TABLE products (
                id          INTEGER PRIMARY KEY,
                description TEXT    NOT NULL,
                price       REAL NOT NULL,
                quantity    INTEGER NOT NULL
            );

            CREATE TABLE branches (
                id                  INTEGER     PRIMARY KEY,
                location            TEXT        NOT NULL,
                number_of_employees INTEGER
            );
    
            CREATE TABLE activities (
                product_id      INTEGER REFERENCES products(id),
                quantity        INTEGER NOT NULL,
                activator_id    INTEGER NOT NULL,
                date            TEXT    NOT NULL
            );
        """)

    def execute_command(self, script: str) -> list:
        return self._conn.cursor().execute(script).fetchall()
 
# singleton
repo = Repository()
atexit.register(repo._close)