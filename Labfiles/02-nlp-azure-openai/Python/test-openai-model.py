## pre-requirements:
## pip install python-dotenv
## pip install openai

import os
from dotenv import load_dotenv

# Add OpenAI import
import openai

def main(): 
        
    try: 
    
        # Get configuration settings 
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_model = os.getenv("AZURE_OAI_MODEL")
        
        # Read text from file
        # text = open(file="../text-files/sample-text.txt", encoding="utf8").read()
        text = open(file="./Labfiles/02-nlp-azure-openai/text-files/sample-text.txt", encoding="utf8").read()
        
        # Set OpenAI configuration settings
        # Set OpenAI configuration settings
        openai.api_type = "azure"
        openai.api_base = azure_oai_endpoint
        openai.api_version = "2022-12-01"
        openai.api_key = azure_oai_key

        # Send request to Azure OpenAI model
        print("Sending request for summary to Azure OpenAI endpoint...\n\n")
        response = openai.Completion.create(
            engine=azure_oai_model,
            prompt=text,
            temperature=0.7,
            max_tokens=60
        )
        
        print(response)
        print("Summary of text: " + response.choices[0].text + "\n")

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()