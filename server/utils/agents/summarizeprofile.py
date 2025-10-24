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
        use key information like demographics, geneder, interests to create the profile summary. Limit the summary to 800 words
        """
    summaryagent=Agent(system_prompt=agentPrompt,model=models[1])
    response=summaryagent(f"Generate a summarized profile using this profile: {profile}. Limit the summary to 800 words.")
    print("Profile Summary:",response)
    return response
    
  