from flask import Flask, render_template

app = Flask(__name__)

# Basic routes for each page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/market')
def market():
    return render_template('market.html')

@app.route('/trade/<ticker>')
def trade(ticker):
    return render_template('trade.html', ticker=ticker)

@app.route('/transaction_history')
def transaction_history():
    return render_template('transaction_history.html')

@app.route('/cash_management')
def cash_management():
    return render_template('cash_management.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)