from flask import Flask, render_template,request,redirect,url_for,flash,session

from database import get_products,get_sales,get_stock,insert_products,insert_sales,insert_stock,check_available_stock,check_user_exists,create_user

from flask_bcrypt import Bcrypt

from functools import wraps 

app = Flask(__name__)

bcrypt = Bcrypt(app)

app.secret_key = "c58c8203d55770ca2c45474d76bdd176"




@app.route("/")
def home():
    number = 100
    return render_template("index.html", value=number)



def login_required(f):
    @wraps(f)
    def protected(*args,**kwargs):
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args,**kwargs)
    return protected


@app.route("/products")
@login_required
def products():
    products_data = get_products()
    return render_template('products.html',products_data=products_data)



@app.route("/add_products", methods=["GET", "POST"])
def add_products():
    if request.method == "POST":
        product_name = request.form["p_name"]
        buying_price = request.form["b_price"]
        selling_price = request.form["s_price"]

        new_product = (product_name, buying_price, selling_price)
        insert_products(new_product)
        flash("Product added successfully!", "success")
        return redirect(url_for("products"))

@app.route("/sales")
@login_required
def sales():
    sales_data = get_sales()
    products = get_products()
    return render_template("sales.html", sales_data=sales_data, products=products)

@app.route("/add_sales", methods=["GET", "POST"])
def add_sales():
    if request.method == "POST":
        product_id = request.form["p_id"]
        quantity = request.form["quantity"]
       
        new_sales = (product_id, quantity)
        available_stock = check_available_stock(product_id)

        if available_stock < float(quantity):
            flash("Insufficient stock. Add more!", "danger")
            return redirect(url_for("sales"))
        else:            
            insert_sales(new_sales)
            flash("Sales added successfully!", "success")
            return redirect(url_for("sales"))

@app.route("/stock")
@login_required
def stock():
    stock_data = get_stock()
    products = get_products()
    return render_template("stock.html", stock_data=stock_data, products=products)

@app.route("/add_stock", methods=["GET", "POST"])
def add_stock():
    if request.method == "POST":
        product_id = request.form["pid"]
        stock_quantity = request.form["quantity"]
       
        new_stock = (product_id, stock_quantity)
        insert_stock(new_stock)
        flash("Stock added successfully!", "success")
    return redirect(url_for("stock"))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        full_name = request.form["full_name"]
        email = request.form["email"]
        phone_number = request.form["phone"]
        password = request.form["password"]
       
        existing_user = check_user_exists(email)
        if not existing_user:
            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
            new_user = (full_name, email, phone_number, hashed_password)
            create_user(new_user)
            flash("User created successfully!", "success")
            return redirect(url_for("login"))
        else:
            flash("User already exists! Please login instead", "danger")
   
    return render_template("register.html")


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        registered_user = check_user_exists(email)
        if not registered_user:
            flash("User doesn't exist! Please register.",'danger')
        else:
            if bcrypt.check_password_hash(registered_user[-1],password):
                session['email'] = email
                flash("Login successful!",'success')
                return redirect(url_for('dashboard'))
            else:
                flash("Incorrect password! Try again.",'danger')
    
    return render_template('login.html')



app.run(debug=True)


