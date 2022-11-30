from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from constants import *
from PIL import Image
import requests
import ssl
import urllib3

class CustomHttpAdapter (requests.adapters.HTTPAdapter):
    # "Transport adapter" that allows us to use custom ssl_context.

    def __init__(self, ssl_context=None, **kwargs):
        self.ssl_context = ssl_context
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = urllib3.poolmanager.PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, ssl_context=self.ssl_context)


def get_legacy_session():
    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.options |= 0x4  # OP_LEGACY_SERVER_CONNECT
    session = requests.session()
    session.mount('https://', CustomHttpAdapter(ctx))
    return session

def load_home_page(base_url,browser):
    browser.get(base_url)
    time.sleep(2)

def navigate_to_form(browser):
    content = browser.find_element(By.CSS_SELECTOR, selector_form)
    content.click()
    time.sleep(2)
    option = browser.find_element(By.CSS_SELECTOR,selector_option)
    option.click()
    time.sleep(2)
    print("You are on the correct form page, make appropriate selections")
    
def fill_form(browser,sro_office,doc_number, year,doc_type):
    sro_dropdown = browser.find_element(By.CSS_SELECTOR,selector_sro)
    sro_dropdown.send_keys(sro_office)
    doc_no_text_box = browser.find_element(By.CSS_SELECTOR,selector_docno)
    doc_no_text_box.send_keys(doc_number)
    year_dropdown = browser.find_element(By.CSS_SELECTOR,selector_year)
    year_dropdown.send_keys(year)
    doc_type_dropdown=browser.find_element(By.CSS_SELECTOR,selector_doctype)
    doc_type_dropdown.send_keys(doc_type)
    print("Form filled, provide the captcha")

def fill_captcha(browser,captcha):
    captcha_text = browser.find_element(By.CSS_SELECTOR,selector_captcha_text)
    captcha_text.send_keys(captcha)

def get_captcha_img(browser):
    captcha_img = browser.find_element(By.CSS_SELECTOR,selector_captcha_img)
    src = captcha_img.get_attribute('src')
    img_content= get_legacy_session().get(src,stream=True).raw
    return Image.open(img_content).show()

def submit_form(browser):
    form_btn = browser.find_element(By.CSS_SELECTOR,selector_formsubmit)
    form_btn.click()
    time.sleep(2)
    print("Form submitted")

def download_certificate(browser):
    download_btn = browser.find_element(By.CSS_SELECTOR,selector_downldpage)
    download_btn.click()
    time.sleep(2)
    download_btn_final = browser.find_element(By.CSS_SELECTOR,selector_downldbtn)
    download_btn_final.click()
    time.sleep(2)
    print("Form downloaded")
