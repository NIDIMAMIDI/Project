# Inventory Control Management

# Learning Objective - Understanding the problem statement and implementing the same using Python and SQL.
# Problem Statement - Inventory Control Management helps to identify which and how much stock to order at what time. It tracks inventory from purchase to the sale of goods. 
# Create this project with the help of  the following specifications:

# 1.Create a database called “Inventory_Management” with different tables like “manufacture”, “goods”, “purchase”, “sale” etc.
# 2.Insert multiple entries to these different tables - “manufacture”, “goods”, “purchase” and “sale”.

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Sharu@7981350465')
cur=mydb.cursor()
cur.execute("create database Inventory_Management")
cur.execute("use Inventory_Management")

# 3.In the “manufacture” table, one should be able to see all the products that need to be manufactured, and defective items during the manufacture with different entries like manufacture id, number of items required, etc. 
# Creating and Insereting Data Into Manufacture Table

Manufacture_Table='create table manufacture(manufacture_id integer(5) primary key not null,manufacture_date date not null,item_name varchar(30) not null,no_of_items integer(5),defective_items integer(5) not null,item_color varchar(20) not null,company varchar(30) not null)'
cur.execute(Manufacture_Table)
t1='insert into manufacture(manufacture_id,manufacture_date,item_name,no_of_items,defective_items,item_color,company) values(%s,%s,%s,%s,%s,%s,%s)'
a=[ (1, '2023-04-01', 'Shirt', 1000, 30,'Red','ALLEN SOLLY'),
    (2, '2023-04-02', 'Toy Car', 600, 20,'Red','IBM'),
    (3, '2023-04-01', 'Toy Car',  850, 35,'Yellow','SONY'),
    (4, '2023-04-02', 'EARPODS', 200, 15,'Orange','DELL'),
    (5, '2023-04-03', 'MOBILE PHONE', 150, 27,'White','LENOVO'),
    (6,'2023-04-04','LAPTOP',1500,40,'Black','ACER')]
cur.executemany(t1,a)
print("Manufacture Table Details are Inserted Successfully")
mydb.commit()

# 4.In the “goods” table, it should include different items that are manufactured by the company along with the goods id, manufactured date, etc.
# Creating and Insereting Data Into Goods Table

Goods_Table="create table goods(goods_id integer(5) primary key not null,manufacture_id integer(5) not null,item_name varchar(30) not null,item_color varchar(20) not null,item_price integer(5) not null,manufactured_date date not null)"
cur.execute(Goods_Table)
t2='insert into goods(goods_id,manufacture_id,item_name,item_color,item_price,manufactured_date) values(%s,%s,%s,%s,%s,%s)'
b=[ (1, 1, 'Shirt', 'Red', 150, '2023-04-01'),
    (2, 2, 'Toy Car', 'Red', 200, '2023-04-02'),
    (3, 3, 'Toy Car', 'Yellow', 200, '2023-04-01'),
    (4, 4, 'EARPODS', 'Orange', 300, '2023-04-02'),  
    (5, 5, 'MOBILE PHONE', 'White', 300, '2023-04-03'),
    (6,6,'LAPTOP','Black',100,'2023-04-04')]
cur.executemany(t2,b)
print("Goods Table Details are Inserted Successfully")
mydb.commit()

# 5.In the “purchase” table, it should include all the purchase details that are purchased in different online and offline stores, along with the purchase id, purchase amount, etc.
# Creating and Insereting Data Into Purchase Table

Purchase_Table='create table purchase (purchase_id integer(5) primary key not null,goods_id integer(5) not null,purchase_date date not null,purchase_amount integer(5) not null,purchase_store varchar(50) not null)'
cur.execute(Purchase_Table)
t3='insert into purchase(purchase_id,goods_id,purchase_date,purchase_amount,purchase_store) values(%s,%s,%s,%s,%s)'
c=[ (1, 1, '2023-04-06', 26500, 'ORay'),
    (2, 2, '2023-04-07', 5600, 'Myntra'),
    (3, 3, '2023-04-08', 13050, 'Allen Solly'),
    (4, 4, '2023-04-09', 6500, 'V-Mart'),
   (5, 5, '2023-04-10', 4750, 'Super Bazar')]
cur.executemany(t3,c)
print("Purchase Table Details are Inserted Successfully")
mydb.commit()

# 6.In the “sale” table, it should include all the items got sold in different stores with the sale date, profit margin, etc
# Creating and Insereting Data Into Sales Table

Sales_Table='create table sales(sale_id integer(5) primary key not null,goods_id integer(5) not null,sale_date date not null,sale_amount integer(5) not null,sale_store varchar(50) not null,profit_margin integer(5) not null)'
cur.execute(Sales_Table)
t4='insert into sales(sale_id,goods_id,sale_date,sale_amount,sale_store,profit_margin) values(%s,%s,%s,%s,%s,%s)'
d=[(1, 1, '2023-04-16', 30000, 'PrashantiNilayam', 5000),
    (2, 2, '2023-04-17', 9000, 'MyKids', 1500),
    (3, 3, '2023-04-18', 13500, 'Myntra', 2250),
    (4, 4, '2023-04-19', 6000, 'V-mart', 1000),
    (5, 5, '2023-04-20', 4500, 'More',750)]
cur.executemany(t4,d)
print("Sales Table Details are Inserted Successfully")
mydb.commit()

# 7.Delete the defective item, e.g., the shirt which was accidentally purchased by the “ORay” store, manufactured on the date ‘01-04-23’.

dele='DELETE FROM goods WHERE goods.goods_id in(SELECT goods_id from(SELECT goods.goods_id FROM goods JOIN manufacture ON goods.manufacture_id = manufacture.manufacture_id JOIN purchase ON goods.goods_id = purchase.goods_id WHERE goods.item_name = "Shirt" AND purchase.purchase_store = "ORay" AND manufacture.manufacture_date = "2023-04-01" AND manufacture.defective_items >0 limit 1)as c)'
cur.execute(dele)
print("Deleted successfully")
mydb.commit()

# 8.Update the manufacture details of all the red-colored toys which are purchased by the “MyKids” store.
upd="UPDATE manufacture m JOIN goods g ON m.manufacture_id = g.manufacture_id JOIN purchase p ON g.goods_id = p.goods_id SET m.no_of_items = m.no_of_items + p.purchase_amount, m.defective_items = m.defective_items + (p.purchase_amount * 0.05) WHERE g.item_name = 'Toy Car' AND g.item_color = 'Red' AND p.purchase_store='MyKids'"
cur.execute(upd)
print("Updated successfully")
mydb.commit()

# 9.Display all the “wooden chair” items that were manufactured before the 1st May 2023. 
display="SELECT * FROM goods WHERE item_name = 'Wooden Chair' AND manufactured_date < '2023-05-01'"
cur.execute(display)
print("Displayed Successfully")
my_result2=cur.fetchall()
for x in my_result2:
    print(x)
mydb.commit()

# 10.Display the profit margin amount of the “wooden table” that was sold by the “MyCare” store, manufactured by the “SS Export” company."""
cur.execute("SELECT profit_margin FROM sales,goods, manufacture WHERE goods.goods_id = sales.goods_id AND goods.item_name = 'wooden table' AND manufacture.company = 'SS Export' AND sales.sale_store = 'MyCare'")
my_result2=cur.fetchall()
for i in my_result2:
    print(i)
mydb.commit()

"""
                    OUTPUT
Manufacture Table Details are Inserted Successfully
Goods Table Details are Inserted Successfully
Purchase Table Details are Inserted Successfully
Sales Table Details are Inserted Successfully
Deleted successfully
Updated successfully
Displayed Successfully
(4, 4, 'Wooden Chair', 'Orange', 300, datetime.date(2023, 4, 2))

"""