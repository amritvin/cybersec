from flask import Flask
app = Flask(__name__)

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return render_template('list.html')

if __name__ == '__main__':
   app.run(port=8857)
