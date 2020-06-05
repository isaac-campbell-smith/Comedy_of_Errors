from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from collections import defaultdict
import pickle

def scrape_reviews():
    with open('review_links.pkl', 'rb') as f:
        search_links = pickle.load(f)

    specials = list(search_links.keys())
    search_links = list(search_links.values())
    
    user_review_dic = defaultdict(dict)

    options = Options()
    options.headless = True
    more_content = '//button[@id="load-more-trigger"]' 

    c = 0
    for title, link in list(search_links.items()):
        
        user_review_dic[title] = defaultdict()
        try:
            driver = webdriver.Chrome(options=options)
            driver.get(link)
        except:
            driver.close()
            time.sleep(10)
            continue
            
        while True:
            try:
                load_more_button = driver.find_element_by_xpath(more_content)
                time.sleep(2)
                load_more_button.click()
                time.sleep(2)
            except:
                break
        soup = BeautifulSoup(driver.page_source, "html.parser")
        review_div = soup.find_all('div', {'class':"review-container"})
        for review in review_div:
            try:
                score = int(review.find('span', {'class':''}).text)
                name = review.find('span', {'class':'display-name-link'}).text
                user_review_dic[title][name] = score
            except:
                pass

        c += 1
        if c % 25 == 0:
            print (f'{i} of {len(specials)} scraped')

    drive.close()

    f = open("user_reviews.pkl","wb")
    pickle.dump(user_review_dic,f)
    f.close()

    print ('All Done!')