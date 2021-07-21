import tweepy
import schedule
import time
from random import randint
from bs4 import BeautifulSoup
import requests
import sys

quotes=[]

url = 'https://www.brainyquote.com/topics/life-quotes'
req = requests.get(url)
soup = BeautifulSoup(req.content, 'lxml')
reg=soup.findAll('div',{"class":'grid-item qb clearfix bqQt b-qt-lg'})
for i in reg:
    j=i.find('a',{"title":'view quote'})
    k=i.find('a',{"title":'view author'})
    l=j.text+' - '+k.text
    quotes.append(l)

quotes=quotes[:5]
#print(len(quotes))
#print(quotes)

auth = tweepy.OAuthHandler("A0k60J8Q2mrGTtnIr6goSnVhq", "E5tCD3w3LeSAz0F8PEQhWV8tDZ0cRnskJGpjyuUCGCORIAvcuJ")
auth.set_access_token("1416829817354293249-NfPGy9uEKV7Rg43Pj2o7xhm6ti3z6M", "2gBNEWTJlijntKpw8iFo96SBg48TjeunfmIlRWJFkHgxD")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during Authentication")

def send_message():
    auth = tweepy.OAuthHandler("A0k60J8Q2mrGTtnIr6goSnVhq", "E5tCD3w3LeSAz0F8PEQhWV8tDZ0cRnskJGpjyuUCGCORIAvcuJ")
    auth.set_access_token("1416829817354293249-NfPGy9uEKV7Rg43Pj2o7xhm6ti3z6M", "2gBNEWTJlijntKpw8iFo96SBg48TjeunfmIlRWJFkHgxD")

    api = tweepy.API(auth)

    num=randint(0,len(quotes)-1)
    tweet = quotes[num]
    quotes.remove(tweet)
    #print(len(quotes))

    api.update_status(status=tweet)
    print('Tweeted: %s' % tweet)

schedule.every(1).minutes.do(send_message)

while True:
    if(len(quotes)==0):
        break
    schedule.run_pending()
    time.sleep(1)

print("Done!")
sys.exit()
