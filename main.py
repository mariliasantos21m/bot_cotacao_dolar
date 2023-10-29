import telebot
import os
import data
from telebot import *
from telebot.ext import *
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv

load_dotenv()

API_TELEGRAM= os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(API_TELEGRAM)

buttons = {'Cotação Dólar':'/cotacao_dolar', 'Calcular Cotação':'/calcular_cotacao_dolar', 'Sobre':'/sobre'}
def add_buttons(keyboard):
    for key, value in buttons.items():
        keyboard.add(types.InlineKeyboardButton(text=key, callback_data=value))


def check_message_response_default(message):
    if((message.text != "") and (message.text not in buttons.values()) and not(message.text).isnumeric()):
        return True
    else:
        return False    

def check_valor_calcular_cotacao(message):
    if((message.text).isnumeric()):
        return True
    else:
        return False
    
@bot.message_handler(func=check_message_response_default)
def response_default(message):    
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    add_buttons(keyboard)
    bot.send_message(message.chat.id, f'Olá, {message.chat.first_name}. Esse é o cotacao_dolar US$! ', reply_markup=keyboard)

@bot.message_handler(commands=['/sobre'])
def message_sobre(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    add_buttons(keyboard)
    bot.send_message(message.chat.id, 'Created by mary :D', reply_markup=keyboard)
    
@bot.message_handler(commands=['/cotacao_dolar'])
def message_cotacao(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    add_buttons(keyboard)
    bot.send_message(message.chat.id, f'Cotação: {data.buscar_cotacao()}', reply_markup=keyboard)

@bot.message_handler(commands=['/calcular_cotacao_dolar'])
def message_calcular_cotacao(message):
    bot.send_message(message.chat.id, "Insira o valor em R$:")

@bot.message_handler(func= check_valor_calcular_cotacao)
def response_calcular_cotacao(message): 
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    add_buttons(keyboard)   
    bot.send_message(message.chat.id, f'Valor em dólar: US$ {data.calcular_cotacao(message.text)}', reply_markup=keyboard)
        
@bot.callback_query_handler(func=lambda call:True)
def response_buttons(callback):
    if (callback.message):
        if (callback.data == '/sobre'):
            message_sobre(callback.message)
        elif(callback.data == '/cotacao_dolar'):
            message_cotacao(callback.message)
        elif(callback.data == '/calcular_cotacao_dolar'):
            message_calcular_cotacao(callback.message)


bot.polling()