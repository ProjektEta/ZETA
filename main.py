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

def ChatMessage(user_message, user_mode, user_id):
    saved_messages = []

    if path.isfile("CHAT_HISTORY/" + str(user_id)) is False:
        return "Sorry! But you do not have previous chat history please use the createhistory command first!"
    
    with open("CHAT_HISTORY/" + str(user_id)) as fp:
        saved_messages = json.load(fp)

    saved_messages.append({'role': user_mode, 'content': user_message})
    response = ollama.chat(model="zeta-llama3", messages=saved_messages, stream=False)
    saved_messages.append({'role': 'assistant', 'content': response['message']['content']})

    with open("CHAT_HISTORY/" + str(user_id), 'w') as json_file:
        json.dump(saved_messages, json_file, indent=4, separators=(',', ': '))

    return response['message']['content']

def CreateHistory(user_id):

    if path.isfile("CHAT_HISTORY/" + str(user_id)) is True:
        return "Sorry! But you do have previous chat history please use the clearhistory command if you want to start a new chat!" 

    default = []
    f = open("CHAT_HISTORY/" + str(user_id), 'w')

    with open("CHAT_HISTORY/" + str(user_id), 'w') as json_file:
        json.dump(default, json_file, indent=4, separators=(",", ": "))

    return
    
def ClearHistory(user_id):

    if path.exists("CHAT_HISTORY/" + str(user_id)):
        os.remove("CHAT_HISTORY/" + str(user_id))

    return

async def DownloadHistory(user_id):
    
    if path.isfile("CHAT_HISTORY/" + str(user_id)) is False:
        return None

    return open("CHAT_HISTORY/" + str(user_id), 'w')


if __name__ == "__main__":
    main()
