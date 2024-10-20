from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drinks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Drink model
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

# Create the database and tables
with app.app_context():
    db.create_all()

# Function to add a new drink
def add_drink(drink_name, drink_description):
    existing_drink = db.session.query(Drink).filter_by(name=drink_name).first()
    if existing_drink:
        print(f"Drink '{drink_name}' already exists with description: {existing_drink.description}")
    else:
        new_drink = Drink(name=drink_name, description=drink_description)
        db.session.add(new_drink)
        db.session.commit()
        print(f"Added new drink: {new_drink.name} - {new_drink.description}")

@app.route('/')
def home():
    return "Welcome to the Drink Inventory!"

@app.route('/drinks')
def view_drinks():
    drinks = Drink.query.all()
    drinks_list = '<br>'.join([f"{drink.name}: {drink.description}" for drink in drinks])
    return render_template_string("<h1>Drinks List</h1><p>{}</p>".format(drinks_list))

# Main entry point
if __name__ == '__main__':
    with app.app_context():
        drinks_to_add = [
            ('Coke', 'A refreshing beverage'),
            ('Pepsi', 'A popular cola drink'),
            ('Sprite', 'A lemon-lime soda'),
        ]
        for drink in drinks_to_add:
            add_drink(drink[0], drink[1])
    
    app.run(debug=True)
