from flask import Flask, redirect, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'goldninjas'

@app.route('/')
def home():
    if not 'gold' in session:
        session['gold'] = 0
    if not 'log' in session:
        session['log'] = []

    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def money():
    if request.form['location'] == 'farm':
        collect = random.randrange(10,21)
        session['gold'] += collect
        session['log'].append("You have gained " + str(collect) + " gold.")
    elif request.form['location'] == 'cave':
        collect = random.randrange(5,11)
        session['gold'] += collect
        session['log'].append("You have gained " + str(collect) + " gold.")
    elif request.form['location'] == 'house':
        collect = random.randrange(2,6)
        session['gold'] += collect
        session['log'].append("You have gained " + str(collect) + " gold.")
    elif request.form['location'] == 'casino':
        collect = random.randrange(-50,51)
        session['gold'] += collect
        if collect >= 0:
            session['log'].append("You have gained " + str(collect) + " gold.")
        else:
            session['log'].append("You have lost " + str(collect * -1) + " gold.")
    
    return redirect("/")

app.run(debug=True)

