from flask import render_template, request, redirect, url_for
from financetracker import app, db
from financetracker.models import User, Transaction, Asset


@app.route("/")
def home():
    return render_template("log-in.html")


# View for Log-In Page
@app.route("/log-in", methods=["GET", "POST"])
def logIn():
    try:
        if request.method == "POST":
            username = request.form.get("username").lower()
            password = request.form.get("password")
            user = User.query.filter_by(username=username).first()

            # Checks if users password is the same as in the database
            if password == user.password:
                # Grants Log-In
                return redirect(url_for("dashboard"))
            else:
                # Redirects to Log-in
                print("Incorrect Password")
                message = "Incorrect Password"
                return render_template("log-in.html", log_in_message=message)
    
    # If User has the Wrong Username
    except AttributeError:
        print("No Account with that username")
        message = "No Account Found With That Username"
        return render_template("log-in.html", log_in_message=message)

    return render_template("log-in.html")


# View for Register Page
@app.route("/register", methods=["GET", "POST"])
def register():
    try:
        if request.method == "POST":
            # Adds data to the database
            username = request.form.get("username").lower()
            password = request.form.get("password")
            net_worth_goal = request.form.get("net_worth_goal")
            savings_goal = request.form.get("savings_goal")
            new_user = User(username=username,password=password, net_worth_goal=net_worth_goal, savings_goal=savings_goal)
            
            # Commits data
            db.session.add(new_user)
            db.session.commit()

            # Redirects to Log-In Page
            return redirect(url_for("logIn"))
    
    # If Credentials already taken
    except:
        print("Credentials Already Taken")
        message = "Credentials Already Taken"
        return render_template("register.html", register_message=message)

    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", active_page="dashboard")


@app.route("/income&expenses")
def income_expenses():
    return render_template("income-expenses.html", active_page="income_expenses")


@app.route("/add-transaction", methods=["GET", "POST"])
def addTransaction():
    return render_template("add-transaction.html", active_page="income_expenses")


@app.route("/edit-salary", methods=["GET", "POST"])
def editSalary():
    if request.method == "POST":
        salary = User(salary=request.form.get("salary"))
        db.session.add(salary)
        db.session.commit()
        return redirect(url_for("income_expenses"))
    return render_template("edit-salary.html", active_page="income_expenses")


@app.route("/delete-transaction")
def deleteTransaction():
    return render_template("delete-transaction.html", active_page="income_expenses")


@app.route("/assets")
def assets():
    return render_template("assets.html", active_page="assets")


@app.route("/add-assets", methods=["GET", "POST"])
def addAssets():
    if request.method == "POST":
        asset_name = request.form.get("asset-name")
        asset_value = request.form.get("asset-value")
        new_asset = Asset(asset_name=asset_name, asset_value=asset_value)
        db.session.add(new_asset)
        db.session.commit()
        return redirect(url_for("assets"))
    return render_template("add-asset.html", active_page="assets")


@app.route("/delete-assets")
def deleteAssets():
    return render_template("delete-asset.html", active_page="assets")