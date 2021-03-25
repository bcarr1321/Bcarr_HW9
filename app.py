from flask import Flask
from flask import render_template, request, url_for
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
        num1 = float(request.form['radius'])
        num2 = float(request.form['height'])
        top = float(3.14*(num1**2))
        side = float(2*(3.14*(num1*num2)))
        total = float(top+side)
        sqft= float((total/144))
        MaterialCost = float(25*sqft)
        LaborCost = float(sqft*15)
        totalCost = float(MaterialCost+LaborCost)
        print(totalCost)
    return render_template('Estimate.html', myValue=totalCost)
        
if __name__ == '__main__':
    app.run(debug=True)