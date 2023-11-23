from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'database': 'mysqlInjection',
}

# Secret key for sessions (change this to a secure value in production)
app.secret_key = 'your_secret_key'

# Create a MySQL database connection
db = mysql.connector.connect(**db_config)

# Define a route for the login page
@app.route('/')
def login():
    return render_template('login.html')

# Define a route to handle the login form submission
@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

    cursor = db.cursor()
    cursor.execute("SELECT * FROM Users WHERE user = %s", (username,))
    user_data = cursor.fetchone()

    if user_data and user_data[1] == password:
        flash('Login successful', 'success')
        return redirect(url_for('dashboard'))
    else:
        flash('Login failed. Please check your credentials.', 'danger')
        return redirect(url_for('login'))

# Define a dashboard route (you can extend this for the actual dashboard)
@app.route('/dashboard')
def dashboard():
    return 'Welcome to the dashboard!'

if __name__ == '__main__':
    app.run(debug=True)
