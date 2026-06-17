from flask import Flask, render_template,request,redirect,url_for,flash
from database import get_products,get_sales,get_stock,insert_products,insert_sales,insert_stock,check_available_stock,check_user_exists,create_user
from flask_bcrypt import Bcrypt


app = Flask(__name__)


bcrypt = Bcrypt(app)

app.secret_key = "c58c8203d55770ca2c45474d76bdd176"


@app.route("/")
def home():
    number = 100
    return render_template("index.html",value = number)


@app.route("/products")
def products():
    products_data = get_products()
    return render_template("products.html", products_data = products_data)


@app.route("/add_products",methods=["GET","POST"])
def add_products():
    if request.method == "POST":
        product_name = request.form["p_name"]
        buying_price = request.form["b_price"]
        selling_price = request.form["s_price"]

        new_product = (product_name,buying_price,selling_price)
        insert_products(new_product)
        flash("Product added successfully","success")
        return redirect(url_for("products"))


# sales route
@app.route("/sales")
def sales():
    sales_data = get_sales()

    products = get_products()
    return render_template("sales.html",sales_data = sales_data,products = products)


@app.route("/add_sales",methods=["GET","POST"])
def add_sales():
    if request.method == "POST":
        product_id = request.form["p_id"]
        quantity = request.form["quantity"]
        
        new_sales = (product_id,quantity)


        available_stock = check_available_stock (product_id)

        if available_stock < float(quantity):
            flash("Insufficient stock, add more","danger")
            return redirect(url_for("sales"))
        else:            
            insert_sales(new_sales)
            print("Sales added successfully")
            return redirect(url_for("sales"))

# stock route
@app.route("/stock")
def stock():
    stock_data = get_stock()
    
    products = get_products()
    return render_template("stock.html",stock_data = stock_data,products = products)

# insert stock route
@app.route("/add_stock",methods=["GET","POST"])
def add_stock():
    if request.method == "POST":
        product_id = request.form["p_id"]
        stock_quantity = request.form["s_quantity"]
        
        new_stock = (product_id,stock_quantity)
        insert_stock(new_stock)
        flash("Stock added successfully","success")
    return redirect(url_for("stock"))

# register route
@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "POST":
        full_name = request.form["full_name"]
        email = request.form["email"]
        phone_number = request.form["phone"]
        password = request.form["password"]
        
        existing_user = check_user_exists(email)
        if not existing_user:
            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
            new_user = (full_name,email,phone_number,hashed_password)
            create_user(new_user)
            flash("User created successfully","success")
            return redirect(url_for("login"))
        else:
            flash("User already exists. Please login instead","danger")
    
    return render_template("register.html")

# dashboard route
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# login route
@app.route("/login")
def login():
    return render_template("login.html")

app.run(debug=True)