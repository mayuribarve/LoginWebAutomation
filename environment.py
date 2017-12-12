from selenium import webdriver

# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Firefox()
browser.maximize_window()
browser.implicitly_wait(60)
# def before_all(context):
#     context.browser = webdriver.Firefox()
#     # context.browser = webdriver.Chrome() if you have set chromedriver in your PATH
#     context.browser.set_page_load_timeout(30)
#     context.browser.implicitly_wait(60)
#     context.browser.maximize_window()


# def after_all(context):
#     context.browser.quit()
