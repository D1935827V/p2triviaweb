import aboutus

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/sub')
def sub():
    return render_template('home.html')

@app.route('/hangman')
def hangman():
    return render_template('hangman.html')

@app.route('/guess_the_number')
def guess_the_number():
    return render_template('guess_the_number.html')

@app.route('/trivia')
def trivia():
    return render_template('trivia.html')

@app.route('/reaction_time')
def reaction_time():
    return render_template('reaction_time.html')

@app.route('/about')
def about():
    return render_template('about.html', aboutus=aboutus.about())

@app.route('/trivia')
def trivia():
    return render_template('trivia.html')

if __name__ == '__main__':
    app.run(debug=True, port='3000')

