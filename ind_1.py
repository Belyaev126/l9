#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Вариант 11. Написать программу, которая считывает текст из файла и выводит на экран только
# предложения, начинающиеся с тире, перед которым могут находиться только пробельные
# символы.

if __name__ == '__main__':
    with open('text.txt', 'r')as f:
        text = f.read()

        text = text.replace("!", ".")
        text = text.replace("?", ".")

        while ".." in text:
            text.replace("..", ".")

        sentences = text.split(".")

        for sentence in sentences:
            if sentence.startswith("-"):
                    print(sentence)

