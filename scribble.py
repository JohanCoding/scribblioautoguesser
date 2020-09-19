import re
import random
import decimal
import time
import sys
import pyautogui
from pynput.keyboard import Key, Controller


keyboard = Controller()
try:

    def sr():
        q = input("How many words (type Y if it has hyphen)>")

        if q == "1":
            wordlen = input("how long is the word>")
            wordlen = int(wordlen)
            string = open("scrribbliowords.txt", "r")
            wordslist = [word for word in string.read().split() if len(word)==wordlen]
            string.close()
            lastword = ""
            time.sleep(3)
            pyautogui.click(1071, 673)
            for word in wordslist:
                if word == lastword:
                    pass
                elif "-" in word:
                    pass
                elif "!" in word:
                    pass
                elif "?" in word:
                    pass
                else:
                    print(word)
                    keyboard.type(word)
                    keyboard.press(Key.enter)
                    lastword = word
                    time.sleep(1.23124)
        elif q == str(2):
            wordlen1 = input("how long is the word>")
            wordlen = int(wordlen1)
            string = open("scrribbliowords.txt", "r")
            wordslist = [word for word in string.read().split() if len(word)==wordlen]
            string.close()
            lastword = ""
            time.sleep(3)
            pyautogui.click(1071, 673)
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
                    time.sleep(1.23124)
        elif q == str(3):
            wordlen1 = input("how long is the word>")
            wordlen = int(wordlen1)
            string = open("scrribbliowords.txt", "r")
            wordslist = [word for word in string.read().split() if len(word)==wordlen]
            string.close()
            lastword = ""
            time.sleep(3)
            pyautogui.click(1071, 673)
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
                    time.sleep(1.23124)
        elif q == "y" or q== "Y":
            wordlen1 = input("how long is the word>")
            wordlen = int(wordlen1)
            string = open("scrribbliowords.txt", "r")
            wordslist = [word for word in string.read().split() if len(word)==wordlen]
            string.close()
            lastword = ""
            time.sleep(3)
            pyautogui.click(1071, 673)
            for word in wordslist:
                if word == lastword:
                    pass
                elif "-" not in word:
                    pass
                elif word == "procrastination":
                    pass
                elif "!" in word:
                    pass
                elif "?" in word:
                    pass
                else:
                    word_hyphen = word
                    print(word_hyphen)
                    keyboard.type(word_hyphen)
                    keyboard.press(Key.enter)
                    lastword = word_hyphen
                    time.sleep(1.23124)
        else:
            print("I am not programmed to handle that function yet or there is no need too have that function")
    sr()
except KeyboardInterrupt:
    time.sleep(3)
    again = input("do you want to go again?")
    if again == "y":
        sr()
    else:
        print("[Program Ended]")
