from flask import Flask,request,Response,jsonify
from flask_cors import CORS,cross_origin
from utils.agents.customer import Customer
from utils.database.cdp import CustomerData
import json
import configparser
import utils.agents.personalizecontent as pc

#create the global objects
app=Flask(__name__)

config=configparser.ConfigParser()
CORS(app)

#initialize the config
#default mode is development
mode="Development"
config.read('config.ini')
rowlimit=config[mode]['rowlimit']
customer=Customer()
customerdata=CustomerData(config,mode)

#create the routes
#default route just displays a message
@app.route("/")
@cross_origin()
def home():
    response= {
        "data": 
        {
            "message":
                    {
                        "content": "I am the customer server"
                    }
        }
    }
    return jsonify(response)

#get the customers
@app.route("/customers",methods=['GET'])
@cross_origin()
def getcustomers():
    global rowlimit
    results=customerdata.getcustomers(rowlimit=rowlimit)
    response={
        "data": 
        {
            "message":
                    {
                        "content":f"{results}"
                    }
        }
    }
    return response
@app.route("/customerprofile/<customerid>",methods=['GET','POST'])
@cross_origin()
def generateprofile(customerid='0'):
    results=customer.generateprofile(customerid)
    response={
        "data": 
        {
            "message":
                    {
                        "content":f"{results}"
                    }
        }
    }
    return jsonify(response)

@app.route("/personalize/<prompt>",methods=['GET','POST'])
@cross_origin()
def personalise(prompt:str):
    results=pc.customize_background(prompt)
    response={
        "data": 
        {
            "message":
                    {
                        "content":f"{results}"
                    }
        }
    }
    return jsonify(response)



if (__name__=="__main__"): 
    app.run(debug=True,host="0.0.0.0",port="8081")