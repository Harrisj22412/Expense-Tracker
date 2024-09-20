from app import db

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    amount = db.Column(db.DateTime, nullable=False)
    category = db.Column(db.String(120))

    def to_dict(self):
        return {
            'id': self.id,
            'name':self.name,
            'amount':self.amount,
            'date':self.date,
            'category':self.category
        }
    
#Create the database tables
db.create_all()