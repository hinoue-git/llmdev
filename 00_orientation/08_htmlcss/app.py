from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f"Hello, {name}!"

@app.route('/about')
def about():
    return "About Page"

@app.route('/user/<username>')
def show_user_profile(username):
    return f"User: {username}"

if __name__ == "__main__":
    app.run(debug=True)
