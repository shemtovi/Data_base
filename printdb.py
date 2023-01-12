from persistence import *

def main():
    print("Activities")
    activitie_list = repo.execute_command("SELECT * FROM activities")
    for line in activitie_list:
        activitie = Activitie(line)
        print(activitie.__str__)
    print("Branches")
    branche_list = repo.execute_command("SELECT * FROM branches")
    for line in branche_list:
        branches = Branche(line)
        print(branches.__str__)
    print("Employees")
    employees_list = repo.execute_command("SELECT * FROM employees")
    for line in employees_list:
        employees = Employee(line)
        print(employees.__str__)
    print("Products")
    products_list = repo.execute_command("SELECT * FROM products")
    for line in products_list:
        products = Product(line)
        print(products.__str__)
    print("Supplier")
    suppliers_list = repo.execute_command("SELECT * FROM suppliers")
    for line in suppliers_list:
        suppliers = Supplier(line)
        print(suppliers.__str__)



if __name__ == '__main__':
    main()