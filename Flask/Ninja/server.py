from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/ninja')

@app.route('/ninja')
def route():
    return render_template('index.html')
        
@app.route('/ninja/blue')
def blue():
    return render_template('blue.html')

@app.route('/ninja/purple')
def purplenurp():
    return render_template('purple.html')

@app.route('/ninja/orange')
def orange():
    return render_template('orange.html')

@app.route('/ninja/red')
def red():
    return render_template('red.html')

@app.route('/notapril')
def not_april():
    return render_template('not_april.html')

@app.errorhandler(404)
def page_not_found(e):
    return redirect('/notapril')

app.run(debug = True)