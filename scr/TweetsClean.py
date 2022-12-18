import pandas as pd

path = 'Tweets_C1.xlsx'
df_tweets = pd.read_excel(path)

df_filtered = df_tweets[(df_tweets['Tweet'].str.len() > 3)]
print(df_filtered)
