from strands import Agent
import json

def summarizeprofile(profile:str)->str:
    models=(
        'anthropic.claude-3-7-sonnet-20250219-v1:0',
        'anthropic.claude-3-haiku-20240307-v1:0',
        'anthropic.claude-sonnet-4-5-20250929-v1:0'
    )
    agentPrompt="""
        You are an agent specialized in creating summarized profiles as a text that can be used as a prompt to generate background personalized content for product images.
         Remove all section headings. Use demographics, geneder, and interests to create the profile summary. Do not be verbose.
        """
    summaryagent=Agent(system_prompt=agentPrompt,model=models[1])
    response=summaryagent(f"Summarize this profile: {profile}. Do not be verbose. Limit the summary to 3 sentences.")
    return response
    
  