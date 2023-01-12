from persistence import *

import sys

def main(args : list[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            action = Activitie(splittedline)
            product_quantity = repo.execute_command(f"SELECT quantity FROM products WHERE id = '{action.product_id}'")
            if(action.description > 0):
                repo.execute_command(f"UPDATE products SET quantity = '{product_quantity + action.description }' WHERE id = '{action.product_id}' ")
            else:
                updated_quantity = product_quantity - action.description
                if(updated_quantity >= 0):     
                    repo.execute_command(f"UPDATE products SET quantity = '{updated_quantity}' WHERE id = '{action.product_id}' ")


if __name__ == '__main__':
    main(sys.argv)