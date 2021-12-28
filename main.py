from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def home(): 
  return render_template('index.html')

@app.route('/lacanhome')
def lnshome():
  return render_template('lacanhome.html')

@app.route('/lacanhome2')
def lnshome2():
  return render_template('lacanhome2.html')
  
app.run(host='0.0.0.0')

