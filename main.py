from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def home(): 
  return render_template('index.html')

@app.route('/commands')
def commands():
  return render_template('commands.html')
  
app.run(host='0.0.0.0')

