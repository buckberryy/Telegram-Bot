# -*- coding: utf-8 -*-
"""
Created on Sat May 23 05:09:23 2020

@author: Olcay Esir
"""
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
import requests
import re
import logging
from random import randint
from selenium import webdriver
from datetime import date


musicList = ["https://www.youtube.com/watch?v=BOn3Tu2vfS0", "https://www.youtube.com/watch?v=LqvHXFwG-H8",
             "https://www.youtube.com/watch?v=tmrQXhwF0To"
    , "https://www.youtube.com/watch?v=cITUab_6sVs", "https://www.youtube.com/watch?v=CZjdL6bC3wg",
             "https://www.youtube.com/watch?v=coESiTABB-k"
    , "https://www.youtube.com/watch?v=ZtKf-NNGpZY", "https://www.youtube.com/watch?v=Sn9pzF9rZxI",
             "https://www.youtube.com/watch?v=GJ46u26hhM4"
    , "https://www.youtube.com/watch?v=9oScKV-81H4", "https://www.youtube.com/watch?v=LJCjt2qdxVs",
             "https://www.youtube.com/watch?v=-x5LnDSctk0"
             ]


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def get_image_url():
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$", url).group(1).lower()
    return url


def bop(update, context):
    url = get_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)


def olcay(update, context):
    question = str(context.args[0])
    if(question == "nasılsın"):
        update.message.reply_text("İyiyim, sen nasılsın ?")
    else:
        update.message.reply_text("Merhaba..")
"""

def echo(update, context):
    update.message.reply_text(update.message.text)
"""


def musicCreate(update, context):
    x = randint(0, 11)
    update.message.reply_text(musicList[x])


def getYoutubeandCorona():
    browser = webdriver.Chrome()
    browser.get(
        "https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNHJsZhIiUExGZ3F1TG5MNTlhbFZMenoyc2FKcEtVR0JrMXFxMW95MA%3D%3D")
    user_data = browser.find_elements_by_xpath('//*[@id="video-title"]')

    for i in user_data:
        links.append(i.get_attribute('href'))

    browser.get("https://covid19.saglik.gov.tr")
    user_data = browser.find_element_by_xpath('//*[@id="bg-logo"]')
    a = user_data.screenshot(corona)

    browser.close()


def youtube(update, context):
    index = randint(0, len(links))
    update.message.reply_text(links[index])


links = []
corona = str(date.today()) + ".png"


def covid(update, context):
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=open(corona, 'rb'))
    update.message.reply_text("Türkiye Günlük Korona Virüsü Tablosu")

def doviz(update,context):
    browser = webdriver.Chrome()

    browser.get(
        "https://www.doviz.com")

    user_data = browser.find_element_by_xpath('/html/body/header/div[2]/div/div/div[1]/a/span[2]')
    altin = user_data.text
    user_data = browser.find_element_by_xpath('/html/body/header/div[2]/div/div/div[2]/a/span[2]')
    dolar = user_data.text
    user_data = browser.find_element_by_xpath('/html/body/header/div[2]/div/div/div[3]/a/span[2]')
    euro = user_data.text

    update.message.reply_text("Altın   :"+ altin +"\n"+
                              "Dolar  :"+ dolar + "\n"+
                              "Euro   :"+ euro)
    browser.close()


def start(update, context):
    update.message.reply_text("Kanalıma hoşgeldiniz. Kullanabileceğiniz komutlar ; \n"
                              "1- /kopek Rastgele köpek resmi oluşturur \n"
                              "2- /youtube Rastgele Trend müziklerden bir tane seçer \n"
                              "3- /oneri Seçilen müziklerden rastgele bir tane getirir \n"
                              "4- /olcay OLCAY ESIR \n"
                              "5- /covid Güncel Korona Vaka Sayıları \n"
                              "6- /doviz Güncel Döviz Kurları")


def main():
    updater = Updater('BOT_TOKEN', use_context=True)
    dp = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    getYoutubeandCorona()
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('kopek', bop))
    dp.add_handler(CommandHandler('youtube', youtube))
    dp.add_handler(CommandHandler('oneri', musicCreate))
    dp.add_handler(CommandHandler('covid', covid))
    dp.add_handler(CommandHandler('doviz', doviz))
    dp.add_handler(CommandHandler('olcay', olcay,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True
                                  ))

    """dp.add_handler(MessageHandler(Filters.text, echo)) eğer yazılan mesaja cevap olarak yazdığı stringin dönmesini istiyorsak"""
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
