from appium import webdriver
from time import sleep


desired_caps = {
'platformName': 'Android',
'deviceName': '127.0.0.1:62001',
'platformVersion': '6.0.0',
# apk包名
'appPackage': 'com.globalegrow.app.gearbest',
# apk的launcherActivity
'appActivity': 'com.globalegrow.app.gearbest.SplashActivity',
'unicodeKeyboard':True,    #使用Unicode编码发送字符串
'resetKeyboard':True     #隐藏键盘
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

sleep(12)

driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[5]/android.widget.ImageView").click()
# driver.get("www.baidu.com")
sleep(2)
driver.find_element_by_id("com.globalegrow.app.gearbest:id/tv_sign_in").click()
sleep(1)
driver.find_element_by_id("com.globalegrow.app.gearbest:id/et_login_username").send_keys("583241254@qq.com")
sleep(1)
# driver.find_element_by_xpath("//*[@NAF='true']").click()
# sleep(1)
driver.find_element_by_id("com.globalegrow.app.gearbest:id/et_login_password").send_keys("abc456456")
driver.find_element_by_id("com.globalegrow.app.gearbest:id/btn_login").click()
sleep(2)
# driver.close_app()


driver.find_element_by_id("com.globalegrow.app.gearbest:id/my_favorites").click()   #点击收藏商品
sleep(1)
# Floureon 2S 7.4V 5200mAh 30C Li-po RC Battery with T Plug for RC Evader BX Car Truck Truggy RC Hobby

driver.find_element_by_xpath("//*[@text='Floureon 2S 7.4V 5200mAh 30C Li-po RC Battery with T Plug for RC Evader BX Car Truck Truggy RC Hobby']").click()
sleep(2)
driver.find_element_by_xpath("//*[@text='Buy Now']").click()
sleep(1)
driver.find_element_by_xpath("//*[@text='Buy Now']").click()

# driver.find_element_by_id("one_key_buy_text")   #点击购买
# driver.find_element_by_id("one_key_buy_text")   #点击购买
# com.globalegrow.app.gearbest:id/one_key_buy_text
# driver.find_element_by_id("popup_one_step_buy_text")   #点击购买
# com.globalegrow.app.gearbest:id/popup_one_step_buy_text
sleep(3)
# driver.find_element_by_id("place_order_button")   # place_order_button
driver.find_element_by_xpath("//*[@text='Place Order']").click()




# com.globalegrow.app.gearbest:id/goods_img_imageview




print("成功ok")





 # e9dede22       8733c6d4




