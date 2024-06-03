from textblob import TextBlob
from newspaper import Article


# # Get the article
# url = 'https://indianexpress.com/article/cities/delhi/three-year-old-girl-raped-smothered-to-death-dumped-in-drain-9350693/'
# article=Article(url)
# article.download()
# article.parse()
# article.nlp()

# text=article.summary
# print(text)

with open("myfile.txt","r") as f:
    text=f.read()

blob = TextBlob(text)
sentiment=blob.sentiment.polarity
print(sentiment)