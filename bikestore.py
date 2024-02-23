from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock database (you would typically use a real database like SQLite or MongoDB)
bikes = [
    {'id': 1, 'brand': 'Brand 1', 'model': 'Model 1', 'price': 500},
    {'id': 2, 'brand': 'Brand 2', 'model': 'Model 2', 'price': 700},
    # Add more bikes as needed
]

cart = []

@app.route('/')
def index():
    return render_template('index.html', bikes=bikes)

@app.route('/bike/<int:bike_id>')
def view_bike(bike_id):
    bike = next((b for b in bikes if b['id'] == bike_id), None)
    if bike:
        return render_template('bike.html', bike=bike)
    return "Bike not found"

@app.route('/add_to_cart/<int:bike_id>')
def add_to_cart(bike_id):
    bike = next((b for b in bikes if b['id'] == bike_id), None)
    if bike:
        cart.append(bike)
        return redirect(url_for('index'))
    return "Bike not found"

@app.route('/cart')
def view_cart():
    return render_template('cart.html', cart=cart)

if __name__ == '__main__':
    app.run(debug=True)
