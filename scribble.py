import re
import random
import time
import sys
from pynput.keyboard import Key, Controller

keyboard = Controller()

q = input("How many words>")

if q == "1":
    wordlen = input("how long is the word(including spaces)>")
    wordlen = int(wordlen)
    string = open("scrribbliowords.txt", "r")
    wordslist = [word for word in string.read().split() if len(word)==wordlen]
    string.close()
    lastword = ""
    time.sleep(3)
    for word in wordslist:
        if word == lastword:
            pass
        elif "!" in word:
            skip
        elif "?" in word:
            skip
        else:
            print(word)
            keyboard.type(word)
            keyboard.press(Key.enter)
            lastword = word
            time.sleep(0.99)
if q == str(2):
    wordlen1 = input("how long is the word(including spaces)>")
    wordlen = int(wordlen1)
    string = open("scrribbliowords.txt", "r")
    wordslist = [word for word in string.read().split() if len(word)==wordlen]
    string.close()
    lastword = ""
    time.sleep(3)
    for word in wordslist:
        if word == lastword:
            pass
        elif "!" not in word:
            pass
        elif word == "procrastination":
            pass
        elif "?" in word:
            pass
        else:
            word_2 = word
            word = word_2.replace("!", " ")
            print(word)
            keyboard.type(word)
            keyboard.press(Key.enter)
            lastword = word
            time.sleep(0.99)
if q == str(3):
    wordlen1 = input("how long is the word(including spaces)>")
    wordlen = int(wordlen1)
    string = open("scrribbliowords.txt", "r")
    wordslist = [word for word in string.read().split() if len(word)==wordlen]
    string.close()
    lastword = ""
    time.sleep(3)
    for word in wordslist:
        if word == lastword:
            pass
        elif "?" not in word:
            pass
        elif word == "procrastination":
            pass
        elif "!" in word:
            pass
        else:
            word_3 = word
            word = word_3.replace("?", " ")
            print(word)
            keyboard.type(word)
            keyboard.press(Key.enter)
            lastword = word
            time.sleep(0.99)
