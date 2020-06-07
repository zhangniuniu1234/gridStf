from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import  os



class Testsearch:
    def setup(self):
        desired_caps = {
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.common.MainActivity',
            'platformName': 'Android',
            'platformVersion': '6.0.1',
            'deviceName': '127.0.0.1:5555',
            'noReset' : 'True',
            'udid': os.getenv("udid", None)
        }
        self.driver = webdriver.Remote("http://192.168.199.235:4444/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def test_search(self):
        # self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").send_keys("alibaba")
        self.driver.find_element(MobileBy.XPATH, '//*[@text="BABA"]').click()

    def teardown(self):
        self.driver.quit()



