from flask import Flask,request,Response,jsonify
from flask_cors import CORS,cross_origin
from utils.customerdata import customerprofile
customer=customerprofile()
app=Flask(__name__)
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
@app.route("/initialize",methods=['POST','GET'])
@cross_origin()
def initialize():
    if not (agent.agentsInitialized):
        print("Initializing Agents...")
        agent.create_associate_agents()
    print("Initialized Agents...")
    response={
        "data": 
        {
            "message":
                    {
                        "content":"Agents initialized"
                    }
        }
    }
    return jsonify(response)

@app.route("/invoke",methods=['POST'])
@cross_origin()
def invoke():
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