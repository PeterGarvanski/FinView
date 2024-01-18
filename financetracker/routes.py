from flask import render_template, request, redirect, url_for
from financetracker import app, db
from financetracker.models import User, Transaction, Asset


@app.route("/")
def home():
    return render_template("log-in.html")

@app.route("/log-in")
def logIn():
    if request.method == "GET":
        username = request.form.get("username")
        password = request.form.get("password")
        print(username)
        print(password)
        return redirect(url_for("dashboard"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        net_worth_goal = request.form.get("net_worth_goal")
        savings_goal = request.form.get("savings_goal")
        new_user = User(username=username,password=password, net_worth_goal=net_worth_goal, savings_goal=savings_goal)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("home"))
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