from persistence import *

def main():
    print("Activities")
    activitie_list = repo._conn.cursor().execute("SELECT * FROM activities ORDER BY date ASC")
    for line in activitie_list:
        print(str(line).replace('"',''))
    print("Branches")
    branche_list = repo._conn.cursor().execute("SELECT * FROM branches ORDER BY id ASC").fetchall()
    for line in branche_list:
        print(line)
    print("Employees")
    employees_list = repo._conn.cursor().execute("SELECT * FROM employees ORDER BY id ASC").fetchall()
    for line in employees_list:
        print(line)
    print("Products")
    products_list = repo._conn.cursor().execute("SELECT * FROM products ORDER BY id ASC").fetchall()
    for line in products_list:
        print(line)
    print("Suppliers")
    suppliers_list = repo._conn.cursor().execute("SELECT * FROM suppliers ORDER BY id ASC").fetchall()
    for line in suppliers_list:
        print(line)
    
    print("\nEmployees report")
    report = repo.execute_command("SELECT employees.id, name, salary, location FROM employees JOIN branches ON branche = branches.id ORDER BY name;")
    for line in report:
        balance = 0
        tempTable = repo.execute_command(f"SELECT quantity, product_id FROM activities WHERE activator_id = {line[0]}")
        for amount in tempTable:
            price = repo.execute_command(f"SELECT price FROM products WHERE products.id = {amount[1]}").pop()
            balance += -(amount[0]*price[0])
        print(f"{line[1]} {line[2]} {line[3]} {balance}")
    print("\nActivities report")
    activities_report = []
    activities_report=repo._conn.cursor().execute('''SELECT activities.date, products.description, activities.quantity, employees.name, suppliers.name
                                FROM activities JOIN products on activities.product_id = products.id
                                left JOIN employees ON activities.activator_id = employees.id
                                left JOIN suppliers ON activities.activator_id = suppliers.id
                                ORDER BY activities.date''')
    for activity in activities_report:
        print(activity)


if __name__ == '__main__':
    main()