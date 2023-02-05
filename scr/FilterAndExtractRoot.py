# import pandas lib as pd
import pandas as pd
array=[]
array2=[]
# setting the 3rd row as header.
df = pd.read_excel('Tweets-filterd2+Rooted.xlsx', sheet_name = 0)

# This Code For Filter Data Set
df['Tweet']=df['Tweet'].str.replace(r'@[a-zA-Z_0-9]{0,}','') #Deleting Mention
df['Tweet']=df['Tweet'].str.replace(r'#[^\s]{0,}','')   #Deleting Hashtag
df['Tweet']=df['Tweet'].str.replace(r'http\S+','')      #Deleting URL Links
df['Tweet']=df['Tweet'].str.replace(r'[\.,\+\$\%\!\[\]\'\"\|\^\&\`\:]',' ') #Deleting Special Charecter
df['Tweet']=df['Tweet'].str.replace(r'([^\u0621-\u064A0-9\s]+)','') #Deleting any char not arabic or number
df=df[~(df.Tweet.str.contains(u'AD|وظائف|إعلان|رواتب|راتب|وظيفة',na=False))] #Deleting rows that have this words




# This Code For Extracting Root For Each Tweet
#make propre display for unicode
import pyarabic.arabrepr
arepr = pyarabic.arabrepr.ArabicRepr()
repr = arepr.repr
from farasa.stemmer import FarasaStemmer

stemmer = FarasaStemmer(interactive=True)

from tashaphyne.stemming import ArabicLightStemmer
ArListem = ArabicLightStemmer()

df = df[df['Tweet'].notnull()]

for i in df['Tweet']:
    
    array2.append(stemmer.stem(i.strip())

    x=[]
    x=i.split(sep=' ')
    sentence=''
    for j in x:
        if(len(j)>3):
            ArListem.light_stem(j)
            sentence+=ArListem.get_root()
            if(x[len(x)-1]!=j): sentence+=" "
        else:
            sentence+=j
            sentence+=" "
    array.append(sentence)

df["RootTweet"]=array
df["SteemTweet"]=array2
df.to_excel('Tweets-filterd2+Rooted.xlsx')
