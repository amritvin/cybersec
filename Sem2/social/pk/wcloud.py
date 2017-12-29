from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import random

from wordcloud import WordCloud, STOPWORDS

t1 = 'Would love to take a selfie when you are in campus I will have 2 of my Ph D students hooded this year Congratulations Classof2017 of 250 students will graduate this year with 13 Ph Ds 10 CSE Ph Ds Special congratulations to all Medalists With this year s convocation our total Alumni base crosses 1000 mark DeanGiri ProfGiri IIITDConvocation Classof2017'
t="LastDay WinterSchool UserExperience Design WS17UXD ProfGiri Thanks to every participant to attend the Winter School it was great having you Thanks to TAs Pooja for support Special thanks to Aman without whom this would not have been possible designthinking"
text=t1+t
wordcloud = WordCloud(relative_scaling = 1.0, background_color='white',
                      stopwords = {'to', 'of'} # set or space-separated string
                      ).generate(text)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
import json
import re
from twython import Twython
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import Counter
from nltk import ngrams


import matplotlib.pyplot as plt
import random
from wordcloud import WordCloud, STOPWORDS

stopwords_english=stopwords.words('english')
for e in stopwords_english:
    e=e.encode('ascii','ignore')
    print type(e)
