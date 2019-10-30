'''
@Description: python
@Version: 1.0
@Autor: liuhua
@QQ: 434375025@qq.com
@Link: https://github.com/choly1985
@Date: 2019-10-30 14:56:31
@LastEditors: liuhua
'''
# coding=utf-8
import configparser


class ReadIni():
    def __init__(self):
        self.data = self.load_ini()

    def load_ini(self):
        cf = configparser.ConfigParser()
        cf.read(
            r'F:\Src\LearningPython\AutoTest_Web_meke\base_node\config\LocalElement.ini')
        return cf

    def get_value(self, key):
        return self.data.get('element', key)


read_ini = ReadIni()
