from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/sub')
def sub():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, port='3000')
