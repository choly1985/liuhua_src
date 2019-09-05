'''
@Description: python
@Version: 1.0
@Autor: liuhua
@QQ: 434375025@qq.com
@Link: https://github.com/choly1985
@Date: 2019-05-11 15:36:28
@LastEditors: liuhua
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-11 15:36:20
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$

import os


class AnonymousSurvey():
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_reponse(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results:")
        for response in self.responses:
            print("_" + response)


question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)
my_survey.show_question()
while True:
    response = input("language: ")
    if response == 'q':
        break
    my_survey.store_reponse(response)
my_survey.show_results()
