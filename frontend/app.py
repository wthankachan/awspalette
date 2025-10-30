from flask import Flask, request
from flask import render_template
from flask import url_for
import configparser
import json
import ast
import requests
import html
import sys

#initialize the global values
app = Flask(__name__)
config=configparser.ConfigParser()
config.read('config.ini')

#read the config values
#default is running in development mode
#TODO: use the mode argument to determine if dev or prod
mode=sys.argv[1:][1] if len(sys.argv) > 1 else "development"
BASEAPIURL=config[mode]["protocol"]+"://"+config[mode]["apibaseurl"]+":"+config[mode]["port"]+"/"


# route mapping
# default route to list the customers
@app.route("/")
def customerdata():
    global BASEAPIURL
    global mode
    APIURL=BASEAPIURL+config[mode]["customers"]
    response=requests.get(APIURL)
    customer=ast.literal_eval(response.json()["data"]["message"]["content"])
    return render_template('customerdata.html',data=customer)


@app.route("/generate",methods=['GET','POST'])
def customerprofile():
    global BASEAPIURL
    global mode
    customerid = request.args.get('customerid', default='0')
    APIURL=BASEAPIURL+config[mode]["customerprofile"]+"/"+customerid
    response=requests.get(APIURL)
    customerprofile=response.json()["data"]["message"]["content"]
    return render_template('customerprofile.html',data=customerprofile)

@app.route("/addimages")
def addimages():
    return render_template('addimages.html')

@app.route("/social")
def socialmedia():
    return render_template('socialmedia.html')

@app.route("/personalizedimages", methods=['POST'])
def personalizedimages():
    global BASEAPIURL
    global mode
    APIURL=BASEAPIURL+config[mode]["personalize"]
    profile=request.form['profile']
    response=requests.post(APIURL,data=profile)
    image64content=response.json()["data"]["message"]["content"]
    return render_template('personalizedimages.html',data=image64content)
  

if (__name__== '__main__'): app.run(host='0.0.0.0',port='8080',debug=True)

