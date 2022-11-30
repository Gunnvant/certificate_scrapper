import argparse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import logging 
import utils

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s | %(levelname)s | %(message)s')

parser = argparse.ArgumentParser(description="This will download encumberence certificate")
parser.add_argument("--sro_office",help = "Name of the sro office")
parser.add_argument("--doc_number",help="Doc number to be downloaded")
parser.add_argument("--year",help="Year for which you need data")
parser.add_argument("--doc_type",help="Type of doc you need to download")

if __name__=="__main__":
    base_url = "https://tnreginet.gov.in/portal/?UserLocaleID=en"
    args = parser.parse_args()
    sro_office = args.sro_office
    doc_number = args.doc_number
    year = args.year
    doc_type = args.doc_type
    logging.info("Launching Browser")
    browser = webdriver.Chrome(ChromeDriverManager().install())
    logging.info("Browsing home page")
    utils.load_home_page(base_url,browser)
    logging.info("Home page loaded, loading form")
    utils.navigate_to_form(browser)
    logging.info("Form fill and captcha input")
    utils.fill_form(browser,sro_office,doc_number,year,doc_type)
    captcha = input("Type in the captcha:")
    utils.fill_captcha(browser,captcha)
    utils.submit_form(browser)
    try:
        utils.download_certificate(browser)
        browser.close()
    except:
        print("No information found")
        browser.close()

