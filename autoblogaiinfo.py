import os
from dotenv import load_dotenv
load_dotenv()

import openai

openai.api_key = os.getenv('OPEN_API')

user_command = input("Write your topics ")

def openai_article(user_command):
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt=user_command,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  
  content =  response.get("choices")[0].get('text')
  return content

content = openai_article(user_command)

print(content)
