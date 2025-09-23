from flask import Flask
from flask import render_template
from flask import url_for
import requests
import configparser
import json
import ast

#initialize the global values
app = Flask(__name__)
config=configparser.ConfigParser()
config.read('config.ini')

#read the config values
#default is running in development mode
#TODO: use the mode argument to determine if dev or prod
mode='Development'
APIURL=config[mode]["protocol"]+"://"+config[mode]["apibaseurl"]+":"+config[mode]["port"]+"/"


# route mapping
# default route to list the customers
@app.route("/")
def customerdata():
    global APIURL
    global mode
    APIURL=APIURL+config[mode]["customers"]
    response=requests.get(APIURL)
    customer=ast.literal_eval(response.json()["data"]["message"]["content"])
    return render_template('customerdata.html',data=customer)


@app.route("/generate")
def customerprofile():
    return render_template('customerprofile.html')


@app.route("/social")
def socialmedia():
    return render_template('socialmedia.html')
if (__name__== '__main__'): app.run(host='0.0.0.0',port='8080',debug=True)

