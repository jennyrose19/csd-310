

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "bacchuswinery",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press confirm key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

cursor = db.cursor()


def show_employee(cursor, title):
    cursor.execute("SELECT Employee_id as 'Employee', Employee_first_name as 'First Name', "
                   "Employee_last_name as 'Last Name', Employee_dept_id as 'Dept. id', Employee_time as 'Hours',"
                   "Start_date as 'Start Date', Term_date as 'Fired Date', Quarter as 'Quarter', Quarterly_time as 'Quarterly Hours' FROM employee")

    employeetb = cursor.fetchall()

    print("\n  -- {} --".format(title))

    for row in employeetb:
        print(f"Employee: {row[0]}")
        print(f"First Name: {row[1]}")
        print(f"Last Name: {row[2]}")
        print(f"Dept. id': {row[3]}")
        print(f"Hours: {row[4]}")
        print(f"Quarter: {row[7]}")
        print(f"Quarterly Hours: {row[8]}")
        print(f"Start Date: {row[5]}")
        print(f"Fired Date: {row[6]}")
        print(" ")


def show_Dept(cursor, title):
    cursor.execute("SELECT Department_id as 'Dept ID', Dept_name as 'Name',"
                   "Dept_head as 'Head' FROM department")

    Depttb = cursor.fetchall()

    print("\n  -- {} --".format(title))

    for row in Depttb:
        print(f"Dept ID: {row[0]}")
        print(f"Name: {row[1]}")
        print(f"Head: {row[2]}")

        print(" ")


def show_Dist(cursor, title):
    cursor.execute("SELECT Distribution_id as 'Distribution ID', Distribution_name as 'Distribution Name', "
                   "Online_order_number as 'Online Order #'"
                   ", Tracking_number as 'Tracking Number',"
                   "Distribution_delivery_date as 'Delivery Date', Order_date as 'Order Date' From distribution")

    Disttb = cursor.fetchall()

    print("\n  -- {} --".format(title))

    for row in Disttb:
        print(f"Distribution ID: {row[0]}")
        print(f"Distribution Name: {row[1]}")
        print(f"Online Order #: {row[2]}")
        print(f"Tracking Number: {row[3]}")
        print(f"Delivery Date: {row[4]}")
        print(f"Order Date: {row[5]}")
        print(" ")


def show_Supp(cursor, title):
    cursor.execute("SELECT Supplier_id as 'Supplier ID', Supplier_name as 'Supplier Name', "
                   "Supplier_inventory as 'Supplier Inventory' ,Component_name as 'Components',"
                   "Supply_order_date as 'Order Date', Supply_delivery_date as 'Delivery Date',"
                   "Expected_delivery_date as 'Expected Delivery Date' FROM supplier")

    Supptb = cursor.fetchall()

    print("\n  -- {} --".format(title))

    for row in Supptb:
        print(f"Supplier ID: {row[0]}")
        print(f"Supplier Name: {row[1]}")
        print(f"Supplier Inventory: {row[2]}")
        print(f"Components: {row[3]}")
        print(f"Order Date: {row[4]}")
        print(f"Delivery Date: {row[5]}")
        print(f"Expected Delivery Date: {row[6]}")
        print(" ")


def show_Win(cursor, title):
    cursor.execute("SELECT Wine_id as 'Wine ID', Wine_name as 'Wine Name',"
                   "Wine_type as 'Type', Distribution_id as 'Dist. ID',"
                   "Supplier_id as 'Supplier ID', Employee_id as 'Employee ID',"
                   "Total_sold as 'Total Sold' FROM winery")

    Wintb = cursor.fetchall()

    print("\n  -- {} --".format(title))

    for row in Wintb:
        print(f"Wine ID: {row[0]}")
        print(f"Wine Name: {row[1]}")
        print(f"Type: {row[2]}")
        print(f"Dist. ID: {row[3]}")
        print(f"Supplier ID: {row[4]}")
        print(f"Employee ID: {row[5]}")
        print(f"Total Sold: {row[6]}")
        print(" ")



show_employee(cursor, "Displaying Employee Table")
show_Dept(cursor, "Displaying Department Table")
show_Dist(cursor, "Displaying Distribution Table")
show_Supp(cursor, "Displaying Supplier Table")
show_Win(cursor, "Displaying Winery Table")

cursor = db.cursor()

# Report 1: Employee Hours by Department
cursor.execute("SELECT employee.Employee_last_name as 'Last Name', "
               "employee.Employee_first_name as 'First Name', "
               "employee.Quarter as Quarter, "
               "employee.Quarterly_time as 'Quarterly Hours', "
               "SUM(employee.Employee_time) as 'Total Hours', "
               "employee.Employee_id as ID "
               "FROM employee "
               "GROUP BY employee.Employee_id "
               "ORDER BY employee.Employee_last_name")
               #"JOIN department ON employee.Employee_dept_id = department.Department_id "
               #"GROUP BY department.Department_id")

result = cursor.fetchall()

print("\nReport 1: Employee Hours by Employee\n")
print("ID\tEmployee Name\t       Quarter\tQuarterly Hours")
print("--\t-------------\t       -------\t---------------")

for row in result:
    print("{}\t{}, {}       \t{}\t{}".format(row[5], row[0], row[1], row[2], row[3]))

# Report 2: Sales by Wine Type
cursor.execute("SELECT winery.Wine_type as 'Wine Type', "
               "SUM(winery.Total_sold) as 'Total Sales', "
               "distribution.Distribution_name as 'Distributor' "
               "FROM winery "
               "JOIN distribution ON winery.Distribution_id = distribution.Distribution_id "
               "GROUP BY winery.Wine_type, distribution.Distribution_name")

result = cursor.fetchall()

print("\nReport 2: Sales by Wine Type\n")
print("Wine Type\tTotal Sales\tDistributor")
print("---------\t-----------\t-----------")

for row in result:
    print("{}  \t{}   \t{}".format(row[0], row[1], row[2]))

# Report 3: Inventory by Supplier
cursor.execute("SELECT supplier.Supplier_name as 'Supplier', "
               "SUM(supplier.Supplier_inventory) as 'Total Inventory', "
               "supplier.Supply_order_date as 'Delivered', "
               "supplier.Expected_delivery_date as 'Expecting' "
               "FROM supplier "
               "GROUP BY supplier.Supplier_id "
               "ORDER BY supplier.Supply_delivery_date")

result = cursor.fetchall()

print("\nReport 3: Inventory by Supplier\n")
print("Supplier\tTotal Inventory\tDelivered\tExpected")
print("-------   \t---------------\t---------\t---------")

for row in result:
    print("{}\t{}   \t{}\t{}".format(row[0], row[1], row[2], row[3]))
