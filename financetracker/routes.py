from flask import render_template, request, redirect, url_for
from financetracker import app, db
from financetracker.models import User


@app.route("/")
def home():
    return render_template("log-in.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", active_page="dashboard")


@app.route("/income&expenses")
def income_expenses():
    return render_template("income-expenses.html", active_page="income_expenses")


@app.route("/assets")
def assets():
    return render_template("assets.html", active_page="assets")

@app.route("/add-assets", methods=["GET", "POST"])
def addAssets():
    return render_template("add-asset.html", active_page="assets")


@app.route("/delete-assets")
def deleteAssets():
    return render_template("delete-asset.html", active_page="assets")