import os
from UI_AUTOMATION.utils.file_reader import YamlReader
from UI_AUTOMATION.utils.file_reader import ExcelReader
# os.path.abspath(__file__) 表示当前文件的绝对路径
# os.path.dirname(path) 表示当前文件的父级目录
# os.path.split(path) 将路径和文件名拆开
# 先获取框架根补录，再用os.path.join()拼接其他模块路径
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
# CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'soa.yml')
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yml')
DATA_PATH = os.path.join(BASE_PATH, 'data1', 'more_langrauge.xlsx')
DRIVER_PATH = os.path.join(BASE_PATH, 'driver')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')


class Config:
    def __init__(self, config=CONFIG_FILE):
        self.config = YamlReader(config).data

    def get(self, element: object, index: object = 0) -> object:
        """
        yaml是可以通过‘---’来分节的。用YamlReader读取返回的是一个list。第一项是默认的节。如果有多个节，可以用index来获取
        这样我们就可以把框架相关的配置放在默认节，其他项目配置放在其他节中，可以在框架中实现多个项目测试
        """
        return self.config[index].get(element)

class Config_E:
    def __init__(self, excel=DATA_PATH):
        self.config = ExcelReader(excel).data

    def get(self, element: object, index: object) -> object:
        return self.config[index].get(element)



if __name__ == '__main__':

    c = Config()
    c = Config().get('mysql')
    print(c)








