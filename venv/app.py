import os 
from flask import Flask, request, jsonify, abort;
from flask_sqlalchemy import SQLAlchemy;
from Model import Expense;

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

app.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.all()
    return jsonify([expense.to_dict() for expense in expenses])

@app.route('/expenses/<int:id>', methods=['Delte'])
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return jsonify({'message': 'Expense deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)