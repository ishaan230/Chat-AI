import openai
from config import apikey
openai.api_key = apikey
    

def callgpt(user_prompt):
    
    #Call the api
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=user_prompt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    
    #Response from api
    print(response["choices"][0]["text"])

def main():
    user_input = input("Enter prompt: ")
    callgpt(user_input)

main()
