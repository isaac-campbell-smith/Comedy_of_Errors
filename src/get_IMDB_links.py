import requests
from requests import get
from bs4 import BeautifulSoup
from collections import defaultdict
import pickle

def load_links():
    with open('comedy_transcripts.pkl', 'rb') as f:
        specials = pickle.load(f)

    specials = list(search_links.keys())
    clean_specials = []
    for title in specials:
        name = ''
        for word in title.split('-'):
            holder = word
            if word == 'ko':
                holder = 'koy'
            if word not in ['full', 'transcript'] and word.isalpha():
                if word in ['d', 'l', 't', 'j', 'c', 'k']:
                    if title in ['chris-d-elia-white-male-black-comic-transcript', 'chris-d-elia-man-on-fire-transcript']:
                        holder += "'"
                    else:
                        holder += '.'
                    if name:
                        if name[-1] == '.':
                            name += holder
                        else:
                            name = name + '+' + holder
                    else:
                        name += holder
                elif word == 'ck':
                    name += '+c.k.'
                else:
                    if name:
                        if name[-1] == "'":
                            name += holder
                        else:
                            name = name + '+' + holder
                    else:
                        name += holder
        url = "https://www.imdb.com/search/title/?title=" + name.replace('+im+', "+i'm+").replace('whats',"what's").replace('arent', "aren't")
        url.replace
        clean_specials.append(url)
    
    clean_specials[36] = "https://www.imdb.com/search/title/?title=andy+woodhull+you'll+always+be+late"
    clean_specials[219] = "https://www.imdb.com/search/title/?title=frankie+boyle+hurt+like+you've+never+been+loved"
    clean_specials[310] = 'https://www.imdb.com/search/title/?title=louis+c.k.+2017'
    clean_specials[311] = 'https://www.imdb.com/search/title/?title=george+carlin+jammin+new+york'
    clean_specials[317] = "https://www.imdb.com/search/title/?title=george+carlin+it's+bad+for+ya"
    return specials, clean_specials

def problem_children(dic):
    dic['patrice-oneal-elephant-in-the-room-2011-full-transcript'] = "https://www.imdb.com/title/tt1625345/reviews?ref_=tt_ov_rt"
    dic['sincerely-louis-ck-transcript'] = "https://www.imdb.com/title/tt12087624/reviews?ref_=tt_ov_rt"
    dic['latin-history-for-morons-john-leguizamo-transcript'] = "https://www.imdb.com/title/tt9777830/reviews?ref_=tt_ov_rt"
    dic['jeff-foxworthy-larry-the-cable-guy-weve-been-thinking-transcript'] = "https://www.imdb.com/title/tt5571712/reviews?ref_=tt_ov_rt"
    dic['ron-white-if-you-quit-listening-ill-shutup-transcript'] = "https://www.imdb.com/title/tt9060534/reviews?ref_=tt_ov_rt"
    dic['joe-mandes-award-winning-comedy-special-transcript'] = "https://www.imdb.com/title/tt7183876/reviews?ref_=tt_ov_rt"
    dic['daniel-sloss-dark-transcript'] = "https://www.imdb.com/title/tt8984816/?ref_=fn_tt_tt_19"
    dic['daniel-sloss-jigsaw-transcript'] = "https://www.imdb.com/title/tt8984826/reviews?ref_=tt_ov_rt"
    dic['iliza-shlesinger-elder-millennial-2018-full-transcript'] = "https://www.imdb.com/title/tt8697266/reviews?ref_=tt_ov_rt"
    dic['kevin-james-never-dont-give-up-full-transcript'] = "https://www.imdb.com/title/tt8324578/reviews?ref_=tt_ov_rt"
    dic['marlon-wayans-wokeish-transcript'] = "https://www.imdb.com/title/tt7655590/reviews?ref_=tt_ov_rt"
    dic['mike-birbiglia-my-girlfriends-boyfriend-2013-full-transcript'] = "https://www.imdb.com/title/tt2937390/reviews?ref_=tt_ov_rt"
    dic['stewart-lee-standup-comedian-full-transcript'] = "https://www.imdb.com/title/tt0497531/reviews?ref_=tt_ov_rt"
    dic['christina-pazsitsky-mother-inferior-transcript'] = "https://www.imdb.com/title/tt7057376/reviews?ref_=tt_ov_rt"
    dic['chris-rock-kill-the-messenger-london-new-york-johannesburg-2008-movie-script'] = "https://www.imdb.com/title/tt1213574/reviews?ref_=tt_ov_rt"
    dic['rory-scovel-tries-stand-up-for-the-first-time-a-netflix-special'] = "https://www.imdb.com/title/tt7044010/reviews?ref_=tt_ov_rt"
    dic['norm-macdonald-hitlers-dog-gossip-trickery-2017-full-transcript'] = "https://www.imdb.com/title/tt6878486/reviews?ref_=tt_ov_rt"
    dic['george-carlin-playing-head-1986-full-transcript'] = "https://www.imdb.com/title/tt0199554/reviews?ref_=tt_ov_rt"
    dic['louis-c-k-live-at-the-beacon-theatre-2011-full-transcript'] = "https://www.imdb.com/title/tt2112999/reviews?ref_=tt_ov_rt"
    return dic

def get_title_ids():
    comedy_ids = defaultdict(list)
    headers = {"Accept-Language": "en-US, en;q=0.5"}

    specials, search_links = load_links()

    c = 0

    for title, url in zip(specials, search_links):
        results = requests.get(url, headers=headers)
        soup = BeautifulSoup(results.text, "html.parser")
        movie_div = soup.find_all('div', {'class':'ribbonize'})
        comedy_ids[title] = [tag['data-tconst'] for tag in movie_div]

        c += 1
        if c % 25 == 0:
            print (f'{i} of {len(specials)} scraped')

    for key, tags in comedy_ids.items():
        top = ("https://www.imdb.com/title/" + tags[0] + "/reviews?ref_=tt_ov_rt") if tags else ''
        comedy_ids[key] = top

    comedy_ids = clean_problem_children(comedy_ids)

    f = open("review_links.pkl","wb")
    pickle.dump(comedy_ids,f)
    f.close()

    print ('All Done!')