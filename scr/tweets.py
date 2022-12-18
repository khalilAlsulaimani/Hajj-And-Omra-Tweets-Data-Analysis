import snscrape.modules.twitter as sntwitter
import pandas as pd
tweets = []
limit = 500000


query = '(مكة OR العمره OR الحج OR العمرة OR مكه OR منى OR مزدلفة OR مزدلفه OR المشاعر المقدسة OR عرفة OR عرفه OR الحرم OR المسجد الحرام OR الكعبة OR المشاعر المقدسه OR الكعبه OR الصفا OR المروة OR المروه OR الجمرات OR الاضحى OR نمرة OR نمره)'

for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    if len(tweets) == limit:
        break
    else:
        tweets.append([(tweet.date).strftime("%m/%d/%Y, %H:%M:%S"),tweet.user.username,
        tweet.user.verified,tweet.content,
        tweet.lang,tweet.replyCount,
        tweet.retweetCount,tweet.likeCount,tweet.quoteCount])
        
df = pd.DataFrame(tweets,columns=['Date','User','isVerified','Tweet','Language','ReplyCounter','RetweetCounter','LikeCounter','QuoteCounter'])
writer = pd.ExcelWriter('Tweets.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='Sheet1')
writer.save()
print(df)
