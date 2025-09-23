from strands import Agent
import json
class Customer:
    customeragent=None
    def __init__(self):
        self.customeragent=Agent()
    def generateprofile(self,customerdata: json)->str:
        response=self.customeragent("Tell me about agentic AI")
        return response
    def getcustomers()->json:
        results=json.loads("{}")
        return results
    def getcustomerdata(customerid:str)->json:
        results=json.loads("{}")
        return results