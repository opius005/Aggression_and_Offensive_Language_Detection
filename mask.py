import pandas as pd

df = pd.read_csv('valid_tweets.csv')

for index, row in df.iterrows():
  line = str(row['tweet']).split(" ")
  new_line = ""
  for i in line:
    if len(i) != 0 and i[0] == '@':
      i = "@USER"
    new_line += i + " "
  df.loc[index,'tweet']=new_line


df.to_csv("masked_tweets_data.csv",index=False)
