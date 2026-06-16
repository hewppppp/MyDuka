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

