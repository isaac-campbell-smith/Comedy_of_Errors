import string
words='''a,able,about,across,after,all,almost,also,am,among,an,and,announcer,any,\
applause,are,as,at,audience,be,because,been,but,by,can,cheering,could,dear,did,do,does,either,\
else,ever,every,for,from,gentlemen,get,got,had,has,have,he,her,hers,him,his,\
how,however,i,if,in,into,is,it,its,just,ladies,laughter,least,let,like,likely,may,\
me,might,most,must,my,narrator,neither,no,of,off,often,on,only,or,other,our,\
own,rather,said,say,says,she,should,since,so,some,than,that,the,their,\
them,then,there,these,they,this,tis,to,too,transcript,twas,us,wants,was,we,were,\
what,when,where,which,while,who,whom,why,will,with,would,yet,you,your'''

def stopwords():
    sw = set(words.split(','))
    [sw.add(mark) for mark in punctuation_markers()]
    return sw

def punctuation_markers():
    markers = set(string.punctuation)
    markers.add('...')
    return markers