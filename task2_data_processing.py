import json
import pandas as pd

# Step 1: Load the JSON file
with open("data/trends_20260404.json","r")as f:
    loaded_data=json.load(f)

# Loading to DataFrame
df=pd.DataFrame(loaded_data)

# Count the number of rows in dataframe
rows_loaded=len(df)
print(f"Loaded {rows_loaded} stories from data/trends_20260404.json")

# Step 2: Clean the data
# Original dataframe is taken a copy in df_copy 
df_copy=df.copy()

# Rows with same PostId is removed
df_copy=df_copy.drop_duplicates(subset="post_id")
print("After removing duplicates: ",len(df_copy))

# To drops rows where post_id,title,score is missing
df_copy=df_copy.dropna(subset=["post_id"])
df_copy=df_copy.dropna(subset=["title"])
df_copy=df_copy.dropna(subset=["score"])
print("After removing nulls: ",len(df_copy))

# To make sure score and num_comments are integers
df_copy=df_copy.dropna(subset=["score","num_comments"])
df_copy["score"]=df_copy["score"].astype(int)
df_copy["num_comments"]=df_copy['num_comments'].astype(int)


# To remove stories where score is less than 5
df_copy=df_copy[df_copy["score"]>=5]

# To remove extra spaces from the title column
df_copy['title']=df_copy['title'].str.strip(" ")

# Number of rows remaining after cleaning
length_df_copy=len(df_copy)
print("After removing low scores:",len(df_copy))


# Step 3: Save as CSV
df_copy.to_csv("data/trends_clean.csv",index=False)

# confirmation message with the number of rows saved
# length_from_csv=len(df_copy["category"])
print(f"Saved {length_df_copy} rows to data/trends_clean.csv")

# Count per individual category
print("Stories per category:")
technology_count=(df_copy["category"]=="technology").sum()
print(f"{'  technology':20}{technology_count}")

worldnews_count=(df_copy["category"]=="worldnews").sum()
print(f"{'  worldnews':20}{worldnews_count}")

sports_count=(df_copy["category"]=="sports").sum()
print(f"{'  sports':20}{sports_count}")

science_count=(df_copy["category"]=="science").sum()
print(f"{'  science':20}{science_count}")

entertainment_count=(df_copy["category"]=="entertainment").sum()
print(f"{'  entertainment':20}{entertainment_count}")