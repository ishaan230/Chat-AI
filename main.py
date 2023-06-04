import openai
import os
from config import apikey
openai.api_key = apikey
    
def check_index(user_prompt):
    for i in range(0,len(user_prompt)):
        if(user_prompt[i]==" "):
            return i
    return i    

def callgpt(user_prompt):
    
    # # Call the api
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
    resp = (response["choices"][0]["text"])
    print('Generating...\n')
    
    print(resp)
    
    ind = check_index(user_prompt)

    with open(f"./Stored_Results/{user_prompt[0:ind]}.txt", 'w') as file:
        file.write(resp)


def main():
    user_input = input("Enter prompt: ")
    callgpt(user_input)

main()
