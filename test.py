from selenium.webdriver import Chrome
#executable_path:指定浏览器驱动的路劲
web = Chrome(executable_path = "C:/Users/13817/AppData/Local/Programs/Python/Python38-32/chromedriver")
url="http://www.baidu.com"
web.get(url)
