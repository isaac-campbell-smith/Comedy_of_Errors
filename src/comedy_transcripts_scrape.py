from bs4 import BeautifulSoup
from collections import defaultdict
import requests
import time
import pickle

def get_transcripts():
    url = "https://scrapsfromtheloft.com/stand-up-comedy-scripts/"
    trans_dict = defaultdict(list)
    
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html')

    title_containers = soup.find('ul', {'class':'display-posts-listing'})
    links = [tag['href'] for tag in title_containers.select('a')]

    for i, link in enumerate(links):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html')
        #isolate content
        paragraphs = soup.find('div', {'class':'post-content'})  
        #get all paragraphs in content
        text = ' '.join([p.text for p in paragraphs.select('p')])
        #simplify the name of the corresponding text
        k = url.split('/')[-2]
        trans_dict[k] = text
        #slow down the process, wait 15 seconds every loop
        time.sleep(15)
        
        if i % 25 == 0:
            print (f'{i} of {len(links)} scraped')

    f = open('comedy_transcripts.pkl', 'wb')
    pickle.dump(trans_dict, f)
    f.close()
    print ('All Done!')