'''
@Description: python
@Version: 1.0
@Autor: liuhua
@QQ: 434375025@qq.com
@Link: https://github.com/choly1985
@Date: 2019-08-02 15:20:06
@LastEditors: liuhua
'''


import smtplib
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def send_email(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    msg['from'] = 'choly1985@163.com'
    msg['to'] = '958905266@qq.com'

    msg.Root = MIMEMultipart('related')
    ms.Root['Subject'] = msg['Subject']

    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com", port=25)
    smtp.login("choly1985@163.com", 'xb8573097')
    smtp.sendmail("choly1985@163.com", '958905266@qq.com', msg.as_string())
    smtp.quit()
    print('email has send out!')


def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + r"\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new


if __name__ == '__main__':
    test_report = r'C:\Users\liuhua2\Desktop\result'
    new_report1 = new_report(test_report)
    # send_email(r'C:\Users\liuhua2\Desktop\result.html')
