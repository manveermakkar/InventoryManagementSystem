import mysql.connector as ms
m=ms.connect(host="localhost",user="root",password="Manveer123^",database="INVENTORY__ITEMS1")
mc=m.cursor()
mc.execute('''CREATE Database INVENTORY__ITEMS1''')
mc.execute('''USE INVENTORY__ITEMS1;''')
#CREATING TABLE FOR SPORTS INVENTORY
mc.execute('''CREATE TABLE sports_inventory(
              SID VARCHAR(5) PRIMARY KEY,
              product_name VARCHAR(255) NOT NULL,
             quantity INT NOT NULL,
              price DECIMAL(10, 2) NOT NULL);''')
mc.execute('''INSERT INTO sports_inventory (SID,product_name, quantity, price) VALUES
    ('S1','Football', 10, 20.00),
    ('S2','Basketball', 15, 25.00),
    ('S3','Tennis Racquet', 8, 50.00),
    ('S4','Baseball Glove', 12, 30.00),
    ('S5','Golf Clubs', 5, 200.00),
    ('S6','Cricket Bat', 7, 40.00),
    ('S7','Hockey Stick', 10, 35.00),
    ('S8','Volleyball', 6, 15.00),
    ('S9','Table Tennis Paddle', 20, 10.00),
    ('S10','Badminton Shuttlecock', 30, 1.50);''')

#CREATING TABLE FOR CLOTHES INVENTORY#
mc.execute('''CREATE TABLE clothing_inventory(
    SID VARCHAR(5) PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL);''')
mc.execute('''INSERT INTO clothing_inventory (SID,product_name, quantity, price) VALUES
    ('C1', 'T-Shirt', 15, 30.00),
    ('C2', 'Jeans', 20, 25.00),
    ('C3', 'Dress Shirt', 10, 50.00),
    ('C4', 'Sweater', 12, 40.00),
    ('C5', 'Jacket', 8, 60.00),
    ('C6', 'Skirt', 18, 35.00),
    ('C7', 'Hoodie', 25, 20.00),
    ('C8', 'Shorts', 30, 15.00),
    ('C9', 'Blouse', 22, 45.00),
    ('C10', 'Pants', 14, 55.00);''')
#CREATE TABLE FOR TECHDEVICES INVENTORY#
mc.execute('''CREATE TABLE techdevices_inventory (
    SID VARCHAR(5) PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL);''')
mc.execute('''
INSERT INTO techdevices_inventory (SID,product_name, quantity, price) VALUES
    ('T1', 'Laptop', 20, 800.00),
    ('T2', 'Smartphone', 30, 500.00),
    ('T3', 'Tablet', 15, 300.00),
    ('T4', 'Smartwatch', 25, 150.00),
    ('T5', 'Camera', 10, 700.00),
    ('T6', 'Headphones', 50, 50.00),
    ('T7', 'Gaming Console', 8, 400.00),
    ('T8', 'Fitness Tracker', 12, 80.00),
    ('T9', 'Desktop Computer', 18, 1000.00),
    ('T10', 'E-reader', 5, 120.00);''')

#CREATE TABLE FOR FURNITURE ITEMS#
mc.execute('''CREATE TABLE furniture_inventory (
    SID VARCHAR(5) PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);''')
mc.execute('''INSERT INTO furniture_inventory (SID,product_name, quantity, price) VALUES
    ('F1', 'Sofa', 5, 500.00),
    ('F2', 'Dining Table', 8, 300.00),
    ('F3', 'Bed', 10, 700.00),
    ('F4', 'Wardrobe', 15, 400.00),
    ('F5', 'Bookshelf', 12, 150.00),
    ('F6', 'Coffee Table', 20, 100.00),
    ('F7', 'Desk', 7, 250.00),
    ('F8', 'Chair', 30, 50.00),
    ('F9', 'Cabinet', 6, 180.00),
    ('F10', 'Nightstand', 14, 80.00);''')

#CREATE TABLE FOR GROCERY ITEMS#
mc.execute('''CREATE TABLE groceries_inventory (
    SID VARCHAR(5) PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);''')

mc.execute('''INSERT INTO groceries_inventory (SID,product_name, quantity, price) VALUES
    ('G1', 'Rice', 10, 20.00),
    ('G2', 'Pasta', 15, 10.00),
    ('G3', 'Canned Beans', 20, 2.50),
    ('G4', 'Milk', 5, 3.00),
    ('G5', 'Eggs', 30, 1.50),
    ('G6', 'Bread', 8, 2.00),
    ('G7', 'Fresh Vegetables', 12, 15.00),
    ('G8', 'Fresh Fruits', 25, 25.00),
    ('G9', 'Cereal', 18, 4.50),
    ('G10', 'Cooking Oil', 22, 6.00);''')
#CREATING A CATEGORY TABLE #
mc.execute('''CREATE TABLE CATEGORY(
     ID VARCHAR(5) PRIMARY KEY,
     TABLE_NAME VARCHAR(50))''')
mc.execute('''INSERT INTO CATEGORY VALUES
     ('ID1','sports_inventory'),
     ('ID2','clothing_inventory'),
     ('ID3','techdevices_inventory'),
     ('ID4','furniture_inventory'),
     ('ID5','groceries_inventory')''')



#if conn.is_connected():
   # print("connection is established")
