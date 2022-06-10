import telebot
from telebot import types # for types
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Say hello to the bot/Привет боту")
    btn2 = types.KeyboardButton("❓ Ask a question/Задай вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Hello, {0.first_name}! I am test bot for github.com from PassLass".format(message.from_user), reply_markup=markup) # это приветствие
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 Say hello to the bot/Привет боту"):
        bot.send_message(message.chat.id, text="Hello! Thanks for using this bot!/Привеет.. Спасибо что читаешь статью!)")
    elif(message.text == "❓ Ask a question/Задай вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("What is my name?/Как меня звать?")
        btn2 = types.KeyboardButton("What i may to do?/Что я могу?")
        back = types.KeyboardButton("Go to menu/В меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Ask me for a question", reply_markup=markup)
    
    elif(message.text == "What is my name?/Как меня звать?"):
        bot.send_message(message.chat.id, "I havent name...")
    
    elif message.text == "What i may to do?/Что я могу?":
        bot.send_message(message.chat.id, text="All, what you may")
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Say hello to the bot/Привет боту")
        button2 = types.KeyboardButton("❓ Ask a question/Задай вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="You are in the menu/Ты в меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="I dont know this command.../Даже не знаю что сказать")

bot.polling(none_stop=True)
