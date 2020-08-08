import pandas as pd
from flask import Flask, render_template, abort, url_for, redirect, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route("/")
def index():
   
    #procedure = 'CALL AllBoroughCases()'
    #df = CallProcedure(keys, procedure, DQL=True)
    
    return render_template('index.html')
    #return render_template('index.html', tables=[df.to_html(classes='table table-striped table-hover', index=False)], titles=df.columns.values, borough=borough)

@app.route("/login")
def login():

    return render_template('login.html')  

app.run(host='localhost', debug=True)