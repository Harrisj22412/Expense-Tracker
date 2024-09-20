import os 
from flask import Flask, request, jsonify, abort;
from flask_sqlalchemy import SQLAlchemy;

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)

@app.route('/expenses', methods=['POST'])
def create_expense():
    data = request.get_json()
    if not data or not 'name' in data or not 'amount' in data or not 'category' in data or not 'date' in data:
        abort(400, description="Missing fields in request")

        expense = Expense(
            name=data['name'],
            amount=data['amount'],
            date=data['data'],
            category=data['category']
        )
    db.session.add(expense)
    db.session.commit()

    return jsonify(expense.to_dict()), 201