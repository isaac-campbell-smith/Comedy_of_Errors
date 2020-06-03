import numpy as np
import unicodedata
from .stopwords import stopwords, second_filter_words
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.util import ngrams
from sklearn.feature_extraction.text import TfidfVectorizer
import string

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii.decode()

def filter_(ls):
    stopwords_ = stopwords()
    return [word for word in ls if word not in stopwords_]

def tokenize_and_filter(series):
    #takes a series of 
    clean_series = series.apply(lambda s: remove_accents(s))
    tokens = clean_series.apply(lambda s: [word.lower() for word in word_tokenize(s)])
    return tokens.apply(lambda word_list: filter_(word_list))

def lemmatize_tokens(series):
    lemmatizer = WordNetLemmatizer()
    filtered_tokens = tokenize_and_filter(series)
    lemmatized_tokens = filtered_tokens.apply(lambda ls: [lemmatizer.lemmatize(w) for w in ls][10:])
    return lemmatized_tokens.apply(lambda ls: [word for word in ls if word not in second_filter_words()])
