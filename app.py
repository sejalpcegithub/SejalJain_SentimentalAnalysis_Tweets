
import numpy as np
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
@app.route('/')
def home():
  
    return render_template("index1.html")

@app.route('/index2')
def index2():
    return render_template('index2.html')


@app.route('/index3')
def index3():
    return render_template('index3.html')


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')
@app.route('/MiniProjects')
def MiniProjects():
    return render_template('MiniProjects.html')

@app.route('/index4',methods=['GET'])
def index4():
    prediction="Neutral"
    return render_template('index4.html', prediction_text='predicted sentimental analysis for given dataset is : {}'.format(prediction))

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
