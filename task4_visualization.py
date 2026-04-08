import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Loaded the csv file into dataframe
df=pd.read_csv("data/trends_analysed.csv")

# Chart 1:Top 10 stories by score
score_updated=df.sort_values(by="score",ascending=False).head(10)
score_updated['title']=score_updated['title'].str.slice(0,50)

plt.figure(figsize=(8,5))
plt.barh(score_updated['title'],score_updated['score'])
plt.title("Top 10 stories by score")
plt.xlabel("Score")
plt.ylabel("Title")
plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.show()

# Chart 2: Stories per Category 
stories_per_category=df.groupby('category')['category'].count()
print(stories_per_category)
plt.figure(figsize=(8,5))
colors_1=plt.cm.tab10(range(len(stories_per_category)))
plt.bar(stories_per_category.index,stories_per_category.values,
        color=colors_1)
plt.title("Stories per category")
plt.xlabel("Category")
plt.ylabel("Number of stories")
plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.show()

# Chart 3: Score vs Comments
plt.figure(figsize=(8,5))
colors_2=df["is_popular"].map({True:"blue",False:"red"})


plt.scatter(x=df['score'],y=df['num_comments' ],
                c=colors_2)

blue_patch=mpatches.Patch(color='blue',label='Popular')
red_patch=mpatches.Patch(color="red",label="Not Popular")
plt.legend(handles=[blue_patch,red_patch])

plt.title("Score vs Comments")
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.show()


fig,axes=plt.subplots(1, 3,figsize=(18,5))
axes[0].set_title("Top 10 stories by score")
axes[0].set_xlabel("Score")
axes[0].set_ylabel("Title")
axes[0].barh(score_updated['title'],score_updated['score'])

axes[1].set_title("Stories per category")
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Number of stories")
axes[1].bar(stories_per_category.index,
            stories_per_category.values,
color=colors_1)

axes[2].set_title("Score Vs Comments")
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Number of comments")
axes[2].scatter(x=df['score'],y=df['num_comments' ],
                c=colors_2)

axes[2].legend(handles=[blue_patch,red_patch])

fig.suptitle("TrendPulse Dashboard")
plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.show()