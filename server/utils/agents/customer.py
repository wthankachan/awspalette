from strands import Agent
from strands import tool
from utils.database.cdp import CustomerData
import json
import configparser
customeragent=None
models=(
    'anthropic.claude-3-7-sonnet-20250219-v1:0',
    'anthropic.claude-3-haiku-20240307-v1:0',
    'anthropic.claude-sonnet-4-5-20250929-v1:0'
)
agentPrompt="""
    You are an agent specialized in creating summarized customer profiles as a n HTML that can be used to generate an HTML page.
    Focus on the interests, past purchase behavior, demagraphic and gender information that is provided. Customer id is provided to you. 
    Use the tool to retrieve customer profile data that is returned. Do not include the customer id in the profile.
    Format the response as an HTML with appropriate tags but eclude the HTML and Body tags.
    """
@tool
def getcustomerdata(customerid: str,mode:str="Development")->tuple:
    """Tool to get customer data from the CDP database using customer id
    Args:
        customerid (str): customer id
    Returns:
        tuple: customer data""" 
    config=configparser.ConfigParser()
    config.read('config.ini')
    cdp=CustomerData(config,mode)
    try:
        results=cdp.getcustomerdata(customerid)
        return results
    except Exception as e:
        print(f"error: {e}")
        return json.loads("{}")
    
 
    
def generateprofile(customerid: str,mode:str="Development")->str:
    customeragent=Agent(tools=[getcustomerdata],system_prompt=agentPrompt,model=models[1])
    userPrompt=f"Generate a customer profile for {customerid}"
    response=customeragent(userPrompt)
    return response
    
  