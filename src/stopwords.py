import string
import pandas as pd
words='''a,anthony,able,about,across,after,ah,all,almost,also,am,among,an,and,announcer,any,\
applause,applauding,are,as,at,audience,be,because,been,but,by,can,cheering,clapping,could,dear,did,do,does,either,\
else,ever,every,filmed,for,from,fuck,gentlemen,get,got,ha,had,hart,hannibal,has,have,he,her,hers,him,his,\
how,hbo,however,i,im,if,in,into,is,it,its,just,kevin,know,laugh,laughing,laughter,least,let,like,likely,may,\
me,might,most,must,my,narrator,neither,peter,of,off,often,on,only,oh,or,other,our,\
own,rather,russell,said,say,says,she,should,since,so,some,televised,than,that,the,their,\
them,then,there,these,they,this,tis,to,too,transcript,twas,us,wants,was,we,were,\
when,where,which,while,who,whom,why,will,with,would,yet,you,your'''

def stopwords():
    sw = set(words.split(','))
    [sw.add(mark) for mark in punctuation_markers()]
    [sw.add(name) for name in names_filter_words()]
    return list(sw)

def punctuation_markers():
    markers = set(string.punctuation)
    markers.add('...')
    return list(markers)

def names_filter_words():
    names = set()
    pd.read_pickle('data/working_corpus.pkl')['special'].apply(lambda title: [names.add(char.lower()) for char in title.split(' ') if char.isalnum()])
    exclude = ['alive', 'bad', 'help', 'explain', 'kill', 'kills', 'embarrassed', 'dont', 
               'stuff', 'winning', 'work', 'united', 'dress', 'tell', 'feel', 'growing', 'hard',
               'clean', 'hungry', 'quit', 'blacker', 'touch', 'white', 'black']
    [names.remove(word) for word in exclude]
    return list(names)
