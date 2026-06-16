from flask import Flask, render_template,request,redirect,url_for,flash
from database import get_products, get_sales,get_stock,insert_products


app = Flask(__name__)

app.secret_key = 'hope1234'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/products')
def products():
    products_data = get_products()
    return render_template('products.html',products_data=products_data)


@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method == 'POST':
        product_name = request.form['p_name']
        buying_price = request.form['b_price']
        selling_price = request.form['s_price']

        new_product = (product_name,buying_price,selling_price)
        insert_products(new_product)
        print("product added successfully") 

    return redirect(url_for('products'))


@app.route('/sales')
def sales():
    sales_data = get_sales()
    return render_template('sales.html')


@app.route('/stock')
def stock():
    return render_template('stock.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


app.run()