import tweepy,json,re,collections 
from tweepy import OAuthHandler


consumer_key= 'tM5kw6PxV6QFQBC9HZ2npSNks'
access_token= '2758633369-ZJLmPrEEWQp1GisvheyVefJekVeF0weSXpgaeJQ'
consumer_secret= '3fSt1Vc5HWvjJ0HBXMaDR4HSeInmdmbPRuNbJNhppL2gmmlsXk'
access_secret= 'gCDhGmyk93k3hc7yTzJIPhKB5UsyDQlRGSeWJSNCkpLdd'

auth= OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#User Name Validation    
while True:
    try:
        twitter_name= (raw_input("Type the screen name of the user you want: "))
        #For 10 latest tweets 
        text= " "
        for status in tweepy.Cursor(api.user_timeline, screen_name=twitter_name).items(10):
            text= text + " " + status._json['text']
        break
    except Exception:
        print("Invalid user name")
		
text= ''.join([i for i in text if not i.isdigit()])
text= ' '.join(re.sub("(#[A-Za-z0-9]+)|(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())
words= text.split(' ')

words= [x.encode('ascii', errors='replace') for x in words]     #If we do not want the "u" to our code
counter= collections.Counter(words)                             #Find the frequency of each word
frequent= str((counter.most_common(1)))                         #Find the most frequent word
frequent= re.sub('[^a-zA-Z]+', '', frequent)                    #We only want the characters

print ("The most frequent word is: " + frequent )