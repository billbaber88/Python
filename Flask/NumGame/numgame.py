from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key = 'adfa'

@app.route('/', methods=['GET'])
def home():
    

    return render_template('index.html')



@app.route('/guess', methods=['GET'])
def guess():
    session['name'] = request.form['number']
    
    return redirect('/')

app.run(debug = True)
