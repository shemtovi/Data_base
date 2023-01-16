from persistence import *

def main():
    print("Activities")
    activitie_list = repo.activities.find_all()
    for line in activitie_list:
        print("(", end='')
        print(line, end='')
        print(")")
    print("Branches")
    branche_list = repo.branches.find_all()
    for line in branche_list:
        print("(", end='')
        print(line, end='')
        print(")")
    print("Employees")
    employees_list = repo.employees.find_all()
    for line in employees_list:
        print("(", end='')
        print(line, end='')
        print(")")
    print("Products")
    products_list = repo.products.find_all()
    for line in products_list:
        print("(", end='')
        print(line, end='')
        print(")")
    print("Suppliers")
    suppliers_list = repo.suppliers.find_all()
    for line in suppliers_list:
        print("(", end='')
        print(line, end='')
        print(")")
    print("Employees report")
    report = repo.execute_command("SELECT name, salary, location, balance FROM employees JOIN branches ON branche = branches.id ORDER BY name;")
    for line in report:
        print(f"{line[0].decode()}, {line[1]}, {line[2].decode()}, {line[3]}")
    print("Activities report")
    


if __name__ == '__main__':
    main()