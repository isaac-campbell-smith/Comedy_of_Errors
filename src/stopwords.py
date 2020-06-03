import string
words='''a,able,about,across,after,all,almost,also,am,among,an,and,announcer,any,\
applause,are,as,at,audience,be,because,been,but,by,can,cheering,could,dear,did,do,does,either,\
else,ever,every,for,from,gentlemen,get,got,had,has,have,he,her,hers,him,his,\
how,however,i,if,in,into,is,it,its,just,ladies,laughter,least,let,like,likely,may,\
me,might,most,must,my,narrator,neither,no,of,off,often,on,only,or,other,our,\
own,rather,said,say,says,she,should,since,so,some,than,that,the,their,\
them,then,there,these,they,this,tis,to,too,transcript,twas,us,wants,was,we,were,\
what,when,where,which,while,who,whom,why,will,with,would,yet,you,your'''

loosies='''00,000,08,10,100,101,11,114,11th,12,120,13,13th,14,15,150,1500,16,16th,17,18,180,18th,\
19,1900s,1930s,1940s,1950s,1965,1970,1970s,1982,1986,1989,1990,1996,1997,1999,20,200,2000,\
2001,2004,2005,2012,2014,2015,2016,2017,2018,2019,21,21st,22,23,24,25,250,26,27,28,29,30,300,\
31,32,33,34,35,350,36,37,38,39,3rd,40,400,41,42,43,44,45,46,47,48,49,50,500,5000,51,52,53,55,\
56,57,60,600,62,63,65,67,68,69,70,700,71,72,73,75,76,80,800,82,83,85,87,88,89,90,900,911,92,94,95,98,99'''

def stopwords():
    sw = set(words.split(','))
    [sw.add(mark) for mark in punctuation_markers()]
    return sw

def punctuation_markers():
    markers = set(string.punctuation)
    markers.add('...')
    return markers

def second_filter_words():
    return set(loosies.split(','))