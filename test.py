import requests

api_url = 'https://api.telegram.org/bot'
token = '5642731099:AAGRdddqBD79r0K3a1ogprX9lXvHIb7CYFI'
url = api_url + token + '/'

#msgJson = {"text": "hihi", "chat_id": 659584153, "parse_mode": "Markdown", "reply_markup": {"inline_keyboard": [[{"text": "123", "callback_data": "reg"}]]}}
#sendMsg_response = requests.post(url + 'sendMessage', json=msgJson)

msgJson = {"text": "hihi", "chat_id": 659584153, "message_id": 6587, "parse_mode": "Markdown", "reply_markup": {"inline_keyboard": [[{"text": "1234", "callback_data": "reg"}]]}}
sendMsg_response = requests.post(url + 'editMessageText', json=msgJson)
print(sendMsg_response.content)