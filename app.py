from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/Estimate', methods=['GET'])
def Estimate():
    return render_template('Estimate.html')

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        num1 = int(request.form['radius'])
        num2 = int(request.form['height'])
        
if __name__ == '__main__':
    app.run(debug=True)