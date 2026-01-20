import os
from droidrun import DroidRunAgent
from prompts import SYSTEM_PROMPT

# Load API Key (Ensure this is set in your environment)
api_key = os.getenv("DROIDRUN_API_KEY")

def main():
    print("🚀 Starting DomainScout Agent...")
    
    # Initialize the Agent
    agent = DroidRunAgent(api_key=api_key)
    
    # Define the user task
    user_task = "Check if 'DroidRunPizza.com' is available on GoDaddy."
    
    # Run the workflow
    result = agent.run(
        task=user_task,
        system_prompt=SYSTEM_PROMPT,
        device="emulator" # or "device"
    )
    
    print("✅ Task Complete!")
    print(f"Agent Report: {result}")

if __name__ == "__main__":
    main()