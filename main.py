from flask import Flask, render_template, send_from_directory
app = Flask(__name__, static_url_path='/static')

@app.route('/login')
def index():
   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0', port='80')