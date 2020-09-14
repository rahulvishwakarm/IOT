import telepot
import urllib.request  #This module is require for http connection
token = '1247093452:AAHAf0bXYGdztk6-LUesx8lCP86uUmERTqA'
TelegramBot = telepot.Bot(token)

def getMe():
    with urllib.request.urlopen('https://api.telegram.org/bot1247093452:AAHAf0bXYGdztk6-LUesx8lCP86uUmERTqA/getMe') as response:
        html = response.read()
    print(html)

#Getting Connection Attributes
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text':
        bot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))

#Getting Updates here
def getUpdates():
    with urllib.request.urlopen('https://api.telegram.org/bot1247093452:AAHAf0bXYGdztk6-LUesx8lCP86uUmERTqA/getUpdates') as response:
        html = response.read()
    print(html)

#Reply
def getReply():
    url1='https://api.telegram.org/bot1247093452:AAHAf0bXYGdztk6-LUesx8lCP86uUmERTqA'
    chatid='' #InputChatId
    mainURL=url1+'sendMessage?chat_id='+chatid+'&text=TestReply'
    with urllib.request.urlopen(mainURL) as response:
        html = response.read()
    print(html)

#Sending Message
def SendMessage():
    tokenId='1247093452:AAHAf0bXYGdztk6-LUesx8lCP86uUmERTqA'
    chat-id='' #InputChatId
    yourMessage='Test Reply'
    with urllib.request.urlopen('https://api.telegram.org/bot%3C'+tokenId+'%3E/sendMessage?chat_id=%3C'+chat-id+'%3E&text='+yourMessage) as response:
        html = response.read()
    print(html)

#Below we can uncomment which task is to be executed

##TelegramBot.message_loop(getMe)    
##TelegramBot.message_loop(handle)
##TelegramBot.message_loop(getUpdates)
##TelegramBot.message_loop(getReply)
##TelegramBot.message_loop(SendMessage)
