import requests
import pandas as pd
import config

from bottle import (
    run, post, response, request as bottle_request
)

def get_chat_id(data):
    chat_id = data['message']['chat']['id']
    return chat_id

def get_message(data):
    message_text = data['message']['text']
    return message_text

def get_author_name(data):
    author_name = data['message']['from']['first_name']
    return author_name

def send_message(prepared_data):
    """
    prepared_data should be json which includes at least 'chat_id' and 'text'
    """
    message_url = config.BOT_URL + 'sendMessage'
    requests.post(message_url, json=prepared_data)

def change_text_message(text):
    """
    To turn the message backwards.
    """
    return text[::-1]

def define_answer(data):
    text = get_message(data)
    if 'barcos' in text:
       return boats_and_hoes()
    if 'putas' in text:
        return text.replace('putas', 'campamentos')   
    if 'campamentos' in text:
        return "{author} se va de putas".format(author=get_author_name(data))

def boats_and_hoes():
    return 'y putas'    

def prepare_data_for_answer(data):
    answer = define_answer(data)

    if pd.notnull(answer):
        json_data = {
            "chat_id": get_chat_id(data),
            "text": answer
        }

        return json_data    

@post('/')
def main():
    data = bottle_request.json
    answer_data = prepare_data_for_answer(data)
    if pd.notnull(answer_data):
        send_message(answer_data)

    return response


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)    