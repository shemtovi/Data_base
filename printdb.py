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
    report = repo.execute_command("SELECT employees.id, name, salary, location FROM employees JOIN branches ON branche = branches.id ORDER BY name;")
    for line in report:
        balance = 0
        tempTable = repo.execute_command(f"SELECT quantity, product_id FROM activities WHERE activator_id = {line[0]}")
        for amount in tempTable:
            price = repo.execute_command(f"SELECT price FROM products WHERE products.id = {amount[1]}").pop()
            balance += -(amount[0]*price[0])
        print(f"{line[1].decode()}, {line[2]}, {line[3].decode()}, {balance}")
    print("Activities report")
    activities_report = []
    employees_report=repo.execute_command("SELECT activities.date, products.description, activities.quantity, employees.name\
                                FROM activities JOIN products JOIN employees\
                                ON activities.product_id = products.id AND activities.activator_id = employees.id\
                                ORDER BY activities.date")
    suppliers_report=repo.execute_command("SELECT activities.date, products.description, activities.quantity, suppliers.name\
                                FROM activities JOIN products JOIN suppliers\
                                ON activities.product_id = products.id AND activities.activator_id = suppliers.id\
                                ORDER BY activities.date")
    for activity in employees_report:
        toList = list(activity)
        toList.append("None")
        activities_report.append(toList)
    for activity in suppliers_report:
        toList = list(activity)
        toList.insert(3, "None")
        activities_report.append(toList)
    activities_report.sort(key=lambda x: x[0])
    for activity in activities_report:
        print("(", end='')
        if(activity[4] == "None"):
            print(f"{activity[0].decode()}, '{activity[1].decode()}', {activity[2]}, '{activity[3].decode()}', {activity[4]}", end='')
        else:
            print(f"{activity[0].decode()}, '{activity[1].decode()}', {activity[2]}, {activity[3]}, '{activity[4].decode()}'", end='')
        print(")")


if __name__ == '__main__':
    main()