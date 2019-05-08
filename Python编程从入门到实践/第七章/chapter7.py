#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-08 16:04:40
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$

import os
# i = 0
# message = []
# while i < 3:
#     message.append(
#         input("Tell me something,and I will repeat it back to you: "))
#     i += 1
# print(message)

# promt = "\nTell me something,and I will repeat it back to you:  "
# promt += "\nEnter'quit' to end the program. "
# message = ""
# while message != "quit":
#     message = input(promt)
#     print(message)

promt = "\nTell me something,and I will repeat it back to you:  "
promt += "\nEnter'quit' to end the program. "

# active = True
# while active:
#     message = input(promt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# while True:
#     city = input(promt)
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to " + city.title() + "!")

# pets = ['doge', 'cat', 'doge', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove("cat")
# print(pets)

responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond?(YES/NO)")
    if repeat == "no":
        polling_active = False
print("\n--Poll Result--")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
