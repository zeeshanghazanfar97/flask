from flask import Flask, render_template, send_from_directory, redirect, request
app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return redirect('/login')


@app.route('/login', methods = ['POST', 'GET'])
def login():
   return render_template('index.html')
   
@app.route('/auth', methods = ['POST'])
def auth():
    uname = request.form['auth-username']
    password = request.form['auth-password']
    #print(username + ", " + password)
    if uname == 'checkpoint85' and password == 'checkpoint85_pass':
        return redirect('/payment_provider_choice')
    else:
        return redirect('/login')
        
@app.route('/addpaymentmethod')
def apppay():
    return render_template('subs.html')

@app.route('/payment_provider_choice')
def payment_provider_choice():
    return render_template('selectMethos.html')

@app.route('/getCard', methods= ["POST"])
def getCard():
    name = request.form['name']
    add1 = request.form['add1']
    add2 = request.form['add2']
    city = request.form['postal']
    postal = request.form['postal']
    country = request.form['country']
    cardNo = request.form['number']
    expiry = request.form['DOE']
    csv = request.form['csv']

    print ('\n\n\n\n\n')
    print(name)
    print(add1)
    print(add2)
    print(city)
    print(postal)
    print(country)
    print(cardNo)
    print(expiry)
    print(csv)

if __name__ == '__main__':
   app.run(debug = False, host='0.0.0.0', port='80')