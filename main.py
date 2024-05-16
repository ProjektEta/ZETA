import ollama
import json
from os import path
import os

modelfile='''
FROM llama3
SYSTEM You are Zeta, a Virtual Discord AI; You will be helping many people sometimes at the same time! Make sure you can keep track of many convosations at once! System Messages are from the creator of the bot so make sure they take priority 
'''
ollama.create(model='zeta-llama3', modelfile=modelfile)

def main():

    saved_messages = []

    if path.isfile("chat_history.json") is False:
        raise Exception("chat_history.json not found [Error 0xA]")
    
    with open("chat_history.json") as fp:
        saved_messages = json.load(fp)

    while True:
        user_input = input("Message: ")

        if user_input.lower() == "/bye":
            break

        saved_messages.append({'role': 'user', 'content': user_input})
        response = ollama.chat(model="zeta-llama3", messages=saved_messages, stream=False)

        saved_messages.append({'role': 'assistant', 'content': response['message']['content']})

        print(response['message']['content'])

    with open("chat_history.json", 'w') as json_file:
        json.dump(saved_messages, json_file, indent=4, separators=(',', ': '))

    return 0

if __name__ == "__main__":
    main()
