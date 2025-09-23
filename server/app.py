from flask import Flask,request,Response,jsonify
from flask_cors import CORS,cross_origin
from utils.agents.customer import Customer
from utils.agents.tools.customerdata import CustomerData
import json
app=Flask(__name__)
customer=Customer()
customerdata=CustomerData()
CORS(app)
@app.route("/")
@cross_origin()
def home():
    response= {
        "data": 
        {
            "message":
                    {
                        "content": "I am the customer support server"
                    }
        }
    }
    return jsonify(response)
@app.route("/customers",methods=['GET'])
@cross_origin()
def getcustomers():
    results=customerdata.getcustomers()
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
@app.route("/customerprofile",methods=['GET','POST'])
@cross_origin()
def generateprofile():
    inputdata=json.loads("""{
        "age": 23,
        "gender": "male"
    }
    """
    )
    results=customer.generateprofile(inputdata)
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