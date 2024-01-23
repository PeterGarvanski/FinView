from flask import render_template, request, redirect, url_for, session
from financetracker import app, db
from financetracker.models import User, Transaction, Asset
from sqlalchemy import desc
from datetime import datetime


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
                session["USER_ID"] = user.id
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

            if int(net_worth_goal) < 0:
                message = "Net Worth Goal can't be negative!"
                return render_template("register.html", register_message=message)
            elif int(savings_goal) < 0:
                message = "Savings Goal can't be negative!"
                return render_template("register.html", register_message=message)
            else:
                new_user = User(username=username,password=password, net_worth_goal=net_worth_goal, savings_goal=savings_goal, salary=0)
                
                # Commits data
                db.session.add(new_user)
                db.session.commit()

                # Redirects to Log-In Page
                return redirect(url_for("logIn"))
    
    # If Username already taken
    except:
        print("Username Already Taken")
        message = "Username Already Taken"
        return render_template("register.html", register_message=message)

    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    # Retrieves users credentials
    USER_ID = session.get('USER_ID')
    user = User.query.get(USER_ID)
    net_worth_goal = user.net_worth_goal
    savings_goal = user.savings_goal

    # Fetches all the users assets
    net_worth = user.salary
    assets = Asset.query.filter_by(user_id=USER_ID).all()

    # Loops through each asset incrementing the net worth value
    for asset in assets:
        net_worth += int(asset.asset_value)

    # Fetches all the users transactions that fit the query
    savings = 0
    transactions = Transaction.query.filter_by(user_id=USER_ID, transaction_type="earning", category="income").all()
    latest_transactions = Transaction.query.filter_by(user_id=USER_ID).order_by(desc(Transaction.transaction_id)).limit(5).all()

    # Loops through each transaction incrementing the savings value
    for transaction in transactions:
        savings += int(transaction.amount)

    # Adds net worth and savings to the database
    user.net_worth = net_worth
    user.savings = savings
    db.session.commit()

    return render_template("dashboard.html", active_page="dashboard", latest_transactions=latest_transactions, net_worth_goal=net_worth_goal, net_worth=net_worth, savings_goal=savings_goal, savings=savings, user=user)


@app.route("/income&expenses")
def income_expenses():
    # Retrieves users credentials
    USER_ID = session.get('USER_ID')
    user = User.query.get(USER_ID)

    # Formats user salary
    salary = "{:,}".format(user.salary)

    return render_template("income-expenses.html", active_page="income_expenses", salary=salary)


@app.route("/all-transactions")
def allTransactions():
    # Retrieves users credentials
    USER_ID = session.get('USER_ID')
    all_transactions = Transaction.query.filter_by(user_id=USER_ID).all()

    return render_template("all-transactions.html", all_transactions=all_transactions)


@app.route("/add-transaction", methods=["GET", "POST"])
def addTransaction():
    USER_ID = session.get('USER_ID')
    user = User.query.get(USER_ID)

    if request.method == "POST":

        # Adds data to the database
        date = datetime.today()
        transaction_type = request.form.get("transaction_type")
        category = request.form.get("category")
        amount = request.form.get("amount")
        new_transaction = Transaction(user_id=USER_ID, date=date, transaction_type=transaction_type, category=category, amount=amount)

        # Commits data
        db.session.add(new_transaction)
        db.session.commit()

        # Redirects to income and expenses page
        return redirect(url_for("income_expenses"))
    
    salary = "{:,}".format(user.salary)
    return render_template("add-transaction.html", active_page="income_expenses", salary=salary)


@app.route("/edit-salary", methods=["GET", "POST"])
def editSalary():
    USER_ID = session.get('USER_ID')
    user = User.query.get(USER_ID)

    if request.method == "POST":
        # Retrieves the salary from the form and the credentials of the logged in user
        salary = int(request.form.get("salary"))

        # Changes the users salary to the new salary
        user.salary = salary
        db.session.commit()

        return redirect(url_for("income_expenses"))

    salary = "{:,}".format(user.salary)
    return render_template("edit-salary.html", active_page="income_expenses", salary=salary)


@app.route("/delete-transaction", methods=["GET", "POST"])
def deleteTransaction():
    USER_ID = session.get('USER_ID')
    user = User.query.get(USER_ID)

    if request.method == "POST":
        # Retrieves the id from the form and the credentials of the logged in user
        transaction_id = request.form.get("transaction_id")
        transaction = Transaction.query.filter_by(user_id=USER_ID, transaction_id=transaction_id).first()
        delete = request.form.get("delete_transaction")

        # Commit the changes to the database if the transaction exists
        if transaction and delete == "yes":
            db.session.delete(transaction)
            db.session.commit()

        # Redirect to asset page whether or not the transaction was found
        return redirect(url_for("income_expenses"))
    
    salary = "{:,}".format(user.salary)
    return render_template("delete-transaction.html", active_page="income_expenses", salary=salary)



@app.route("/assets")
def assets():
    USER_ID = session.get('USER_ID')
    assets = Asset.query.filter_by(user_id=USER_ID).all()

    total_asset_value = 0
    asset_names = []
    asset_values = []

    for asset in assets:
        total_asset_value += int(asset.asset_value)
        asset_names.append(asset.asset_name)
        asset_values.append(asset.asset_value)

    total_asset_value = "{:,}".format(total_asset_value)

    return render_template("assets.html", active_page="assets", total_asset_value=total_asset_value, asset_names=asset_names, asset_values=asset_values)


@app.route("/add-assets", methods=["GET", "POST"])
def addAssets():
    USER_ID = session.get('USER_ID')
    if request.method == "POST":

        # Adds data to the database
        asset_name = str(request.form.get("asset-name")).capitalize()
        asset_value = request.form.get("asset-value")
        new_asset = Asset(user_id=USER_ID, asset_name=asset_name, asset_value=asset_value)

        # Commits data
        db.session.add(new_asset)
        db.session.commit()

        # Redirects to asset page
        return redirect(url_for("assets"))
    
    assets = Asset.query.filter_by(user_id=USER_ID).all()

    total_asset_value = 0
    asset_names = []
    asset_values = []

    for asset in assets:
        total_asset_value += int(asset.asset_value)
        asset_names.append(asset.asset_name)
        asset_values.append(asset.asset_value)

    total_asset_value = "{:,}".format(total_asset_value)

    return render_template("add-asset.html", active_page="assets", total_asset_value=total_asset_value, asset_names=asset_names, asset_values=asset_values)


@app.route("/delete-assets", methods=["GET", "POST"])
def deleteAssets():
    USER_ID = session.get('USER_ID')

    if request.method == "POST":
        assets = Asset.query.filter_by(user_id=USER_ID).all()
        asset_name = str(request.form.get("asset-name")).capitalize()
        delete = request.form.get("delete_asset")

        # Iterate through the assets and delete the one with the specified name
        if delete == "yes":
            for asset in assets:
                if asset.asset_name == asset_name:
                    db.session.delete(asset)

        # Commit the changes to the database
        db.session.commit()

        # Redirects to asset page
        return redirect(url_for("assets"))
    
    assets = Asset.query.filter_by(user_id=USER_ID).all()

    total_asset_value = 0
    asset_names = []
    asset_values = []

    for asset in assets:
        total_asset_value += int(asset.asset_value)
        asset_names.append(asset.asset_name)
        asset_values.append(asset.asset_value)

    total_asset_value = "{:,}".format(total_asset_value)

    return render_template("delete-asset.html", active_page="assets", total_asset_value=total_asset_value, asset_names=asset_names, asset_values=asset_values)