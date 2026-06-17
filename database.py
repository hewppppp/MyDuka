import psycopg2

conn = psycopg2.connect(host = 'localhost', port = 5432, user = 'postgres', password = '1292', dbname = 'myduka')

curr = conn.cursor()

curr.execute('Select * from products')

products_data = curr.fetchall()

print(products_data)

#curr.execute("Insert into products(name, buying_price, selling_price) values('fridge',89000,102000)")
#conn.commit()
#print(products_data)

product1 = ('samsung phone', 30000, 40000)
product2 = ('LG Microwave', 50000,60000)


#insert_products(product1)
#insert_products(product2)

def insert_products(values):
    curr.execute("insert into products(name, buying_price,selling_price)values(%s,%s,%s)", values)
    conn.commit()

def insert_products2(values):
    curr.execute("insert into products(name, buying_price,selling_price)values(%s,%s,%s)", values)
    conn.commit()

product3 = ('books',1200,1300)
insert_products2(product3)

def get_stock():
    curr.execute("Select * from stock")
    stock_data = curr.fetchall()
    return stock_data

def get_products():
    curr.execute("Select * from products")
    products_data = curr.fetchall()
    return products_data

def get_sales():
    curr.execute("Select * from sales")
    sales_data = curr.fetchall()
    return sales_data


def get_data(table):
    curr.execute(f"select * from {table}")
    data = curr.fetchall()
    return data


def insert_stock(values):
    curr.execute("insert into stock(pid,stock_quantity,created_at) values(%s,%s,%s)",values)
    conn.commit()

def insert_sales(values):
    curr.execute("insert into sales(pid, quantity, created_at) values(%s,%s,%s)", values)
    conn.commit()


stock_one = (1,50,"2025-09-20")
insert_stock(stock_one)

sale_one = (1, 50,"2026-01-20")
insert_sales(sale_one)

get_stock()

get_products()

get_sales()

get_stock()

def sales_per_day():
    curr.execute("""
        select date(sales.created_at) as date, sum(sales.quantity * products.buying_price) as total_sales 
        from sales join products on products.id = sales.pid 
        group by date;
    """)
    daily_sales = curr.fetchall()
    return daily_sales


def profit_per_day():
    curr.execute("""
        select date(sales.created_at) as date, sum(sales.quantity * (products.selling_price - products.buying_price)) as profit 
        from products join sales on sales.pid = products.id 
        group by date;
    """)
    daily_profit = curr.fetchall()
    return daily_profit


def sales_per_product():
    curr.execute("""
        select products.name as p_name, sum(sales.quantity * products.buying_price) as total_sales 
        from sales join products on products.id = sales.pid 
        group by p_name;
    """)
    product_sales = curr.fetchall()
    return product_sales


def profit_per_product():
    curr.execute("""
        select products.name as p_name, sum(sales.quantity * (products.selling_price - products.buying_price)) as profit 
        from products join sales on sales.pid = products.id 
        group by p_name;
    """)
    product_profit = curr.fetchall()
    return product_profit

def check_available_stock(pid):
    curr.execute("select sum(stock.stock_quantity) from stock where pid = %s",(pid))
    total_stock = curr.fetchone()[0] or 0

    curr.execute("select sum(sales.quantity) from sales where pid = %s",(pid))
    total_sales = curr.fetchone()[0] or 0

    return total_stock - total_sales

def check_user_exists(email):
    curr.execute("select * from users where email = %s",(email,))
    user = curr.fetchone()
    return user


def create_user(user_details):
    curr.execute("Insert into users(full_name,email,phone_number,password)values(%s,%s,%s,%s)",user_details)
    conn.commit()

