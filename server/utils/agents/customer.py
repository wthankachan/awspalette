from strands import Agent
from strands import tool
from utils.database.cdp import CustomerData
import json

class Customer:
    customeragent=None
    agentPrompt="""
        You are an agent specialized in creating customer profiles as a text that can be used as a prompt to generate personalized content.
        Focus on the interests, past purchase behavior, demagraphic and gender information that is provided. Customer id is provided to you. 
        Use the tool to retrieve customer profile data that is returned and use that information to create the prompt.
        """
    def __init__(self):
        self.customeragent=Agent(tools=[self.getcustomerdata],system_prompt=self.agentPrompt)
    #tool for getting customer data from cdp.py
    @tool
    def getcustomerdata(self,customerid: str)->tuple:
        cdp=CustomerData()
        try:
            results=cdp.getcustomerdata(customerid)
            print(f"here are the results: {results}")
            return results
        except Exception as e:
            print(f"error: {e}")
            return json.loads("{}")
        results=cdp.getcustomerdata(customerid)
        print(f"here are the results: {results}")
        return results
    def generateprofile(self,customerid: str)->str:
        response=self.customeragent(f"Generate a customer profile for {customerid}")
        return response
    
  