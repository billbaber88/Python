from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key = 'I_like_turtles'

@app.route('/')
def home():
    if not 'random' in session:
        session['random'] = random.randrange(0,101)
    if not 'counter'in session:
        session['counter'] = 0
    session['counter'] += 1   
    return render_template('num2.html')

@app.route('/submit', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    if session['random'] > guess:
        session['content'] = "Too low!! You have guessed " + str(session['counter'])+ " times."
    elif session['random'] < guess:
        session['content'] = "Too high!! You have guessed " + str(session['counter']) + " times."
    else:
        session['content'] = "WINNER after " + str(session['counter'])+ " guesses."
    
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session.clear()
    return redirect('/')

app.run(debug = True)