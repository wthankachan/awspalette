from strands import Agent
from strands import tool
from utils.database.cdp import CustomerData
import json

class Customer:
    customeragent=None
    models=(
        'anthropic.claude-3-7-sonnet-20250219-v1:0',
        'anthropic.claude-3-haiku-20240307-v1:0',
        'anthropic.claude-sonnet-4-5-20250929-v1:0'
    )
    agentPrompt="""
        You are an agent specialized in creating customer profiles as a text that can be used as a prompt to generate personalized content.
        Focus on the interests, past purchase behavior, demagraphic and gender information that is provided. Customer id is provided to you. 
        Use the tool to retrieve customer profile data that is returned and use that information to create the prompt.
        """
    def __init__(self):
        self.customeragent=Agent(tools=[self.getcustomerdata],system_prompt=self.agentPrompt,model=self.models[1])
    #tool for getting customer data from cdp.py
    @tool
    def getcustomerdata(self,customerid: str)->tuple:
        cdp=CustomerData('config.ini')
        try:
            results=cdp.getcustomerdata(customerid)
            return results
        except Exception as e:
            print(f"error: {e}")
            return json.loads("{}")
    
    def generateprofile(self,customerid: str)->str:
        response=self.customeragent(f"Generate a customer profile for {customerid}. Format the response as an HTML file without the html and body tags")
        return response
    
  