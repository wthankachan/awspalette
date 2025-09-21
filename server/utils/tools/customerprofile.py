from strands import Agent
import json
class customerprofile:
    customeragent=None
    def __init__(self):
        self.customeragent=Agent()
    def generateprofile(self,customerdata: tuple)->str:
        response=self.customeragent("Tell me about agentic AI")
        return response