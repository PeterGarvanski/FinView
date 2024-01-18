from financetracker import db


class User(db.Model):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
    net_worth_goal = db.Column(db.Integer, nullable=False)
    savings_goal = db.Column(db.Integer, nullable=False)
    net_worth = db.Column(db.Integer, nullable=True)
    savings = db.Column(db.Integer, nullable=True)
    salary = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.username


class Transaction(db.Model):
    # schema for the Transaction model
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    transaction_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    transaction_type = db.Column(db.String(15), nullable=False)
    category = db.Column(db.String(30), nullable=False)
    amount = db.Column(db.String(10), nullable=False)


class Asset(db.Model):
    # schema for the Asset model
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    asset_id = db.Column(db.Integer, primary_key=True)
    asset_name = db.Column(db.String(30), nullable=False)
    asset_value = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.asset_name