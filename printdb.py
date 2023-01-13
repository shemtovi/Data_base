from persistence import *

def main():
    print("Activities")
    activitie_list = repo.execute_command("SELECT * FROM activities")
    for line in activitie_list:
        activitie = Activitie(line[0], line[1], line[2], line[3])
        print(activitie)
    print("Branches")
    branche_list = repo.execute_command("SELECT * FROM branches")
    for line in branche_list:
        branches = Branche(line[0], line[1], line[2])
        print(branches)
    print("Employees")
    employees_list = repo.execute_command("SELECT * FROM employees")
    for line in employees_list:
        employees = Employee(line[0], line[1], line[2], line[3], line[4])
        print(employees)
    print("Products")
    products_list = repo.execute_command("SELECT * FROM products")
    for line in products_list:
        products = Product(line[0], line[1], line[2], line[3])
        print(products)
    print("Suppliers")
    suppliers_list = repo.execute_command("SELECT * FROM suppliers")
    for line in suppliers_list:
        suppliers = Supplier(line[0], line[1], line[2])
        print(suppliers)



if __name__ == '__main__':
    main()