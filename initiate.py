from persistence import *

import sys
import os

def add_branche(splittedline : list[str]):
    id = splittedline[0]
    location = splittedline[1]
    number_of_employees = splittedline[2]
    repo.execute_command(f"INSERT INTO branches (id, location, number_of_employees) VALUES ('{id}','{location}', {number_of_employees})")

    
def add_supplier(splittedline : list[str]):
    id = splittedline[0]
    name = splittedline[1]
    contact_information = splittedline[2]
    repo.execute_command(f"INSERT INTO suppliers (id, name, contact_information) VALUES ('{id}','{name}', '{contact_information}')")

def add_product(splittedline : list[str]):
    id = splittedline[0]
    description = splittedline[1]
    price = splittedline[2]
    quantity =splittedline[3]
    repo.execute_command(f"INSERT INTO products (id, description, price, quantity) VALUES ('{id}','{description}', '{price}','{quantity}')")
    

def add_employee(splittedline : list[str]):
    id = splittedline[0]
    name = splittedline[1]
    salary = splittedline[2]
    branche = splittedline[3]
    repo.execute_command(f"INSERT INTO employees (id, name, salary, branche) VALUES ('{id}','{name}', '{salary}','{branche}')")


adders = {  "B": add_branche,
            "S": add_supplier,
            "P": add_product,
            "E": add_employee}

def main(args : list[str]):
    inputfilename = args[1]
    # delete the database file if it exists
    repo._close()
    # uncomment if needed
    # if os.path.isfile("bgumart.db"):
    #     os.remove("bgumart.db")
    repo.__init__()
    repo.create_tables()
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(",")
            adders.get(splittedline[0])(splittedline[1:])

if __name__ == '__main__':
    main(sys.argv)