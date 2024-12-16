from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'GOOGLE'

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="siloson",
    database="finance_tracker"
)
cursor = db.cursor()

# Routes
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    cursor.execute("SELECT id, password FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()
    if user and check_password_hash(user[1], password):
        session['user_id'] = user[0]
        return redirect(url_for('dashboard'))
    return "Invalid credentials!"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
        db.commit()
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    user_id = session['user_id']
    cursor.execute("SELECT name FROM users WHERE id=%s", (user_id,))
    user_name = cursor.fetchone()[0]
    cursor.execute("SELECT goal_amount FROM goals WHERE user_id=%s ORDER BY id DESC LIMIT 1", (user_id,))
    goal_amount_result = cursor.fetchone()
    goal_id = goal_amount_result[0] if goal_amount_result else None
    goal_amount = goal_amount_result[0] if goal_amount_result else 0

    cursor.execute("SELECT goal_name, goal_amount FROM goals WHERE user_id=%s", (user_id,))
    goals = cursor.fetchall()
    savings_progress = 100 if goals and goals[-1][1] <= 5000 else 0

    cursor.execute("SELECT SUM(amount) FROM expenses WHERE user_id=%s", (user_id,))
    total_expenses = cursor.fetchone()[0] or 0

    remaining_budget = total_expenses - goal_amount
    if goal_id is not None:
        cursor.execute("UPDATE goals SET remaining_budget=%s WHERE id=%s", (remaining_budget, goal_id))
        db.commit()

    return render_template('dashboard.html', total_expenses=total_expenses,user_name=user_name,goal_amount=goal_amount,savings_progress=savings_progress,remaining_budget = remaining_budget)

@app.route('/log_expense', methods=['GET', 'POST'])
def log_expense():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        user_id = session['user_id']
        category = request.form['category']
        amount = float(request.form['amount'])
        cursor.execute("INSERT INTO expenses (user_id, category, amount) VALUES (%s, %s, %s)", (user_id, category, amount))
        db.commit()
        return redirect(url_for('dashboard'))
    return render_template('log_expense.html')  

@app.route('/history')
def history():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    user_id = session['user_id']
    cursor.execute("SELECT category, amount, date FROM expenses WHERE user_id=%s", (user_id,))
    expenses = cursor.fetchall()
    totals = [expense[1] for expense in expenses]
    return render_template('history.html', expenses=expenses,totals=totals)

@app.route('/goals', methods=['GET', 'POST'])
def goals():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    user_id = session['user_id']
    if request.method == 'POST':
        goal_name = request.form['goal_name']
        goal_amount = float(request.form['goal_amount'])
        cursor.execute("INSERT INTO goals (user_id, goal_name, goal_amount) VALUES (%s, %s, %s)", (user_id, goal_name, goal_amount))
        db.commit()
        return redirect(url_for('goals'))
    
    cursor.execute("SELECT goal_name, goal_amount FROM goals WHERE user_id=%s", (user_id,))
    goals = cursor.fetchall()
    savings_progress = 100 if goals and goals[-1][1] <= 5000 else 0
    return render_template('goals.html', goals=goals,savings_progress=savings_progress)


@app.route('/stress_management')
def stress_management():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    return render_template('stress_management.html')

@app.route('/community')
def community():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    return render_template('community.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
