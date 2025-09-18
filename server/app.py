from flask import Flask,request,Response,jsonify
from flask_cors import CORS,cross_origin
from utils.customerdata import customerdata
app=Flask(__name__)
customerdata=customerdata()
CORS(app)
@app.route("/")
@cross_origin()
def home():
    response= {
        "data": 
        {
            "message":
                    {
                        "content": f"I am the customer support server"
                    }
        }
    }
    return jsonify(response)
@app.route("/customerdata",methods=['GET'])
@cross_origin()
def getcustomerdata():
    results=customerdata.getcustomerdata()
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

@app.route("/customerprofile",methods=['POST'])
@cross_origin()
def getcustomerprofile():
    query=request.json['messages'][0]['content']
    answer=agent.invoke(query)
    response={
        "data": 
        {
            "message":
                    {
                        "content": answer 
                    }
        }
    }
    return jsonify(response)
if (__name__=="__main__"): 
    app.run(debug=True,host="0.0.0.0",port="8081")