import requests
import json
import time
import certifi
import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from datetime import datetime

urllib3.disable_warnings(InsecureRequestWarning)
def check_status(statuscode):
  if statuscode==200:
    return True
  elif statuscode==400:
    print(f"Bad request-check your parameters:{statuscode}")
    return False
  elif statuscode==429:
    print("Rate limit hit - too many requests. Wait before trying again")
    return False
  elif statuscode>=500:
    print(f"Server error({statuscode})- not your fault. Try again later")
    return False
  else:
    print(f"Unexpected status code:{statuscode}")
    return False
headers = {"User-Agent": "TrendPulse/1.0"}

url="https://hacker-news.firebaseio.com/v0/topstories.json"
params={
    "technology":["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews":["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports":["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
    "science":["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
    "entertainment":["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]
}
try:
  response=requests.get(url,headers=headers,verify=certifi.where())
  code=check_status(response.status_code)
  if code==True:
    top_story_IDs=response.json()
    top_500=top_story_IDs[:500]
  else:
    exit()
except requests.exceptions.RequestException as e:
  print(f"Failed to fetch top stories:{e}")
  exit()


all_result=[]

for ke,val in params.items():
  count=0
  for each_id in top_500:
    url1=f"https://hacker-news.firebaseio.com/v0/item/{each_id}.json"
    try:
      response=requests.get(url1,headers=headers,verify=certifi.where(),timeout=5)
      code=check_status(response.status_code)
      if code==True:
        data=response.json()
        Title=data.get('title')
      else:
        continue
      if not Title:
        continue
    
      Title_lowercase=Title.lower()
    except requests.exceptions.RequestException:
      continue
     
  
    for each_val in val:
      each_val_lower=each_val.lower()

      if each_val_lower in Title_lowercase:
        result={'post_id':data.get('id'),
        'title':Title,
        'category':ke,
        'score':data.get('score'),
        'num_comments':data.get('descendants'),
        'author':data.get('by'),
        'collected_at':datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
 

            
        all_result.append(result)
        count+=1
        print(f"{ke}]Collected {count} stories so far")
        break
        
    if count==25:
      break
  time.sleep(2)       
  
with open("data/trends_20260404.json","w") as f:
  json.dump(all_result,f,indent=4)    
print(f"Collected {len(all_result)} stories. Saved to data/trends_20260404.json")   


            