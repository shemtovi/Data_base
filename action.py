from persistence import *

import sys

def main(args : list):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            action = Activitie(splittedline[0], splittedline[1], splittedline[2], splittedline[3])
            repo.activities.insert(action)
            product: Product = repo.products.find(id = action.product_id).pop()
            updated_quantity = product.quantity + int(action.quantity)
            if(updated_quantity >= 0):     
                repo.execute_command(f"UPDATE products SET quantity = '{updated_quantity}' WHERE id = '{action.product_id}' ")
                if(int(action.quantity) < 0):
                    employee: Employee = repo.employees.find(id = action.activator_id).pop()
                    new_balance_to_set = employee.balance + ((int(action.quantity) * product.price)* -1)
                    repo.execute_command(f"UPDATE employees SET balance = '{new_balance_to_set}' WHERE id = '{employee.id}'")


if __name__ == '__main__':
    main(sys.argv)