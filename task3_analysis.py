import numpy as np
import pandas as pd

# Task 1: Load an explore
# Loaded the csv to dataframe
df=pd.read_csv("data/trends_clean.csv")

# Shape of the dataframe
print("Loaded data:",df.shape)

# First 5 rows
print("First 5 rows:\n",df.head())

# To print average score and num_comments across all stories
average_score=int(df['score'].mean())
average_num_comments=int(df['num_comments'].mean())
print("Average score   : {:,}".format(average_score))
print("Average comments: {:,}".format(average_num_comments))

# To get mean,median,std deviation,max and min using numpy
print("--- NumPy Stats ---")
print("Mean score   : {:,}".format(int(np.mean(df["score"]))))
print("Median score : {:,}".format(int(np.median(df["score"]))))
print("Std deviation: {:,}".format(int(np.std(df["score"]))))
print("Max score    : {:,}".format(int(np.max(df["score"]))))
print("Min score    : {:,}".format((np.min(df["score"]))))

# Category with most stories
most_stories_category=df['category'].value_counts().idxmax()
most_stories_count=df['category'].value_counts().max()
print(f"Most stories in: {most_stories_category} ({most_stories_count} stories)")

# Story with most comments
most_commented_story=df.loc[df['num_comments'].idxmax()]
print(f"Most commented story: \"{most_commented_story['title']}\" — {most_commented_story['num_comments']:,} comments")

# Columns engagement and is_popular is included into df
df["engagement"]= (df['num_comments']/ (df["score"]+1)).round(2)
df["is_popular"]=df["score"]>average_score

# Updated df is added to a csv file
df.to_csv("data/trends_analysed.csv",index=False)
print("Saved to data/trends_analysed.csv")