import time
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
class TestDemo:
    def setup(self):
        url = "http://127.0.0.1:5001/wd/hub"
        url1 = "http://193.112.47.128:5001/wd/hub"
        chrome_options = webdriver.ChromeOptions()
        # 解决DevToolsActivePort文件不存在的报错
        # chrome_options.add_argument('--no-sandbox')
        # 指定浏览器分辨率
        # chrome_options.add_argument('window-size=1920x3000')
        # 谷歌文档提到需要加上这个属性来规避bug
        # chrome_options.add_argument('--disable-gpu')
        # 隐藏滚动条, 应对一些特殊页面
        # chrome_options.add_argument('--hide-scrollbars')
        # 不加载图片, 提升速度
        # chrome_options.add_argument('blink-settings=imagesEnabled=false')
        # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Remote(command_executor=url1,
                                  desired_capabilities=DesiredCapabilities.CHROME,
                                  options=chrome_options)
    def test_0(self):

        self.driver.get("http://www.baidu.com")
        time.sleep(1)
        a=self.driver.page_source
        print("\n","-"*20)
        print(a)
        print("-"*30)
    def teardown(self):
        self.driver.quit()