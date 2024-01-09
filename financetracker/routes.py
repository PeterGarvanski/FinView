from flask import render_template, request, redirect, url_for
from financetracker import app, db
from financetracker.models import User


@app.route("/")
def home():
    return render_template("log-in.html")


@app.route("/register")
def register():
    return render_template("register.html")