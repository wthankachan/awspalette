from flask import Flask
from flask import render_template
from flask import url_for
import requests
import configparser

app = Flask(__name__)
config=configparser.ConfigParser()
config.read('config.ini')
@app.route("/")
def customerdata():
    customer=[('a','b','c','d','e','f','g'),('1','2','3','4','5','6','7')]
    return render_template('customerdata.html',data=customer)


@app.route("/generate")
def customerprofile():
    return render_template('customerprofile.html')


@app.route("/social")
def socialmedia():
    return render_template('socialmedia.html')
if (__name__== '__main__'): app.run(host='0.0.0.0',port='8080',debug=True)

