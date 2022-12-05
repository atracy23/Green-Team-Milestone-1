import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "T%rterr@425",
    "host": "127.0.0.1",
    "port": "51502",
    "database": "winery",
    "raise_on_warnings": True
}


try:
    # Insert records into tables.
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    cursor.execute("INSERT INTO Suppliers VALUES (1, 12345, 'Bottle', 'Container Part', 1)")
    cursor.execute("INSERT INTO Suppliers VALUES (2, 23456, 'Cork', 'Container Part', 1)")
    cursor.execute("INSERT INTO Suppliers VALUES (3, 34567, 'Label', 'Transport Material', 1)")
    cursor.execute("INSERT INTO Suppliers VALUES (4, 45678, 'Box', 'Transport Material', 1)")
    cursor.execute("INSERT INTO Suppliers VALUES (5, 56789, 'Vat', 'Manufacturing Part', 1)")
    cursor.execute("INSERT INTO Suppliers VALUES (6, 67890, 'Tubing', 'Manufacturing Part', 1)")
    cursor.execute("INSERT INTO Supply VALUES (1, 'Product Packaging', 50, 12345, '02-15-2022')")
    cursor.execute("INSERT INTO Supply VALUES (2, 'Transport Packaging', 10, 23456, '02-22-2022')")
    cursor.execute("INSERT INTO Supply VALUES (3, 'Manufacturing Components', 3, 34567, '02-07-2022')")
    cursor.execute("INSERT INTO Distributor VALUES "
                   "(1, 'Michael', 'Jordan', '123 Basketball Street', 'Anytown', 12345, '850-123-4567')")
    cursor.execute("INSERT INTO Distributor VALUES "
                   "(2, 'Kiera', 'Knightly', '456 Movie Boulevard', 'Anytown', 12345, '850-321-9876')")
    cursor.execute("INSERT INTO Distributor VALUES "
                   "(3, 'Glenn', 'Beck', 'Radio Road', 'Somewhereville', 54321, '850-112-2334')")
    cursor.execute("INSERT INTO `Order` VALUES "
                   "(1, 1, 'Michael Jordan', '100 Nice Street', 'Big City', "
                   "'Missouri', 12345, '3 9 2022', 12345, 98765)")
    cursor.execute("INSERT INTO `Order` VALUES "
                   "(2, 1, 'Michael Jordan', '200 Pleasant Place', 'Little City', "
                   "'Montana', 55443, '3 25 2022', 23456, 87654)")
    cursor.execute("INSERT INTO `Order` VALUES "
                   "(3, 2, 'Kiera Knightly', '300 Pretty Park', 'Medium City', "
                   "'California', 24680, '4 08 2022', 34567, 76543)")
    cursor.execute("INSERT INTO `Order` VALUES "
                   "(4, 2, 'Kiera Knightly', '400 Cordial Circle', 'Southern City', "
                   "'Kentucky', 35791, '4 15 2022', 45678, 65432)")
    cursor.execute("INSERT INTO `Order` VALUES "
                   "(5, 3, 'Glenn Beck', '500 Politic Parkway', 'Northern City', "
                   "'New York', 24242, '3 22 2022', 56789, 54321)")
    cursor.execute("INSERT INTO `Order` VALUES "
                   "(6, 3, 'Glenn Beck', '600 Radio Wave Walk', 'Coastal City', "
                   "'Rhode Island', 12457, '3 30 2022', 67890, 43210)")
    cursor.execute("INSERT INTO Wine VALUES (1, 1, 'Merlot', 'Red')")
    cursor.execute("INSERT INTO Wine VALUES (2, 1, 'Cabernet', 'Red')")
    cursor.execute("INSERT INTO Wine VALUES (3, 1, 'Chardonnay', 'White')")
    db.commit()
    db.close()

    # Show records in tables.
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Suppliers")
    suppliers = cursor.fetchall()
    print("\n--SUPPLIERS--")
    for supplier in suppliers:
        print("\nCompany ID: {}\nProduct ID: {}\nProduct Name: {}\nProduct Type: {}\nQuantity: {}"
              .format(supplier[0], supplier[1], supplier[2], supplier[3], supplier[4]))

    cursor.execute("SELECT * FROM Supply")
    supplies = cursor.fetchall()
    print("\n--SUPPLIES--")
    for supply in supplies:
        print("\nInventory ID: {}\nSupply Name: {}\nQuantity: {}\nWarehouse ID: {}\nDate Received: {}"
              .format(supply[0], supply[1], supply[2], supply[3], supply[4]))

    cursor.execute("SELECT * FROM Distributor")
    distributors = cursor.fetchall()
    print("\n--DISTRIBUTORS--")
    for distributor in distributors:
        print("\nCustomer ID: {}\nFirst Name: {}\nLast Name: {}\nStreet: {}\nCity: {}\nZIP: {}\nPhone: {}"
              .format(distributor[0], distributor[1], distributor[2], distributor[3],
                      distributor[4], distributor[5], distributor[6]))

    cursor.execute("SELECT * FROM `Order`")
    orders = cursor.fetchall()
    print("\n--ORDERS--")
    for order in orders:
        print("\nOrder Number: {}\nCustomer ID: {}\nCustomer Name: {}\nTo Street: {}\nTo City: {}\nTo State: {}\n"
              "To ZIP: {}\nShip Date: {}\nShipping ID: {}\nTracking ID: {}"
              .format(order[0], order[1], order[2], order[3], order[4],
                      order[5], order[6], order[7], order[8], order[9]))

    cursor.execute("SELECT * FROM Wine")
    wines = cursor.fetchall()
    print("\n--WINES--")
    for wine in wines:
        print("\nProduct ID: {}\nQuantity: {}\nProduct Type: {}\nColor: {}"
              .format(wine[0], wine[1], wine[2], wine[3]))

    input("\n\n Press any key to continue...")
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist.")

    else:
        print(err)
