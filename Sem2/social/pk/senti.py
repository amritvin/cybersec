"""from vaderSentiment.vederSentiment import SentimentIntensityAnalyser
sentance = ""
analyzer=SentimentIntensityAnalyser()
vs=analyzer.polarity_score(sentence)"""
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sentence=["all is well","do are die","feeling alone","amazing, super morning"]
"""
for s in sentence:
    s=s.encode('utf-8')
    analyser = SentimentIntensityAnalyzer(s)
    sent=analyser.polarity_scores()
    print("{:-<40} {}".format(s, str(sent)))
"""
analyzer = SentimentIntensityAnalyzer()
for s in sentence:
    vs = analyzer.polarity_scores(s)
    print(str(vs))
    print(str(vs["compound"]))
