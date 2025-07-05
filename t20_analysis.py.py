#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import json
import pandas as pd
import matplotlib.pyplot as plt

print("Libraries loaded successfully!")


# In[3]:


# Yeh tumhara downloads folder ka path hai
folder_path = r"C:\Users\rajiv\Downloads"

# Check karo ki folder exist karta hai ya nahi
if os.path.exists(folder_path):
    print("✅ Folder found:", folder_path)
else:
    print("❌ Folder path not found!")


# In[4]:


files = os.listdir(folder_path)
all_matches = []

for file in files:
    if file.endswith(".json"):
        file_path = os.path.join(folder_path, file)
        with open(file_path, 'r') as f:
            match_data = json.load(f)
            all_matches.append(match_data)

print("Total matches loaded:", len(all_matches))


# In[5]:


files = os.listdir(folder_path)
all_matches = []

for file in files:
    if file.endswith(".json"):
        file_path = os.path.join(folder_path, file)
        with open(file_path, 'r') as f:
            match_data = json.load(f)
            all_matches.append(match_data)

print("Total matches loaded:", len(all_matches))



# In[6]:


print(os.listdir(folder_path))


# In[7]:


folder_path = r"C:\Users\rajiv\Downloads\t20s_json"


# In[8]:


print(os.listdir(folder_path))


# In[9]:


files = os.listdir(folder_path)
all_matches = []

for file in files:
    if file.endswith(".json"):
        file_path = os.path.join(folder_path, file)
        with open(file_path, 'r') as f:
            match_data = json.load(f)
            all_matches.append(match_data)

print("Total matches loaded:", len(all_matches))


# In[10]:


balls = []

for match in all_matches:
    for inning in match["innings"]:
        team = inning["team"]
        for over in inning["overs"]:
            over_num = over["over"]
            for delivery in over["deliveries"]:
                batter = delivery["batter"]
                bowler = delivery["bowler"]
                runs = delivery["runs"]["batter"]
                date = match["info"]["dates"][0]

                balls.append({
                    "team": team,
                    "over": over_num,
                    "batter": batter,
                    "bowler": bowler,
                    "runs": runs,
                    "date": date
                })

df = pd.DataFrame(balls)
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year

print("✅ DataFrame created successfully!")
print(df.head())


# In[11]:


import matplotlib.pyplot as plt

# Top 10 batsmen by total runs
top_batsmen = df.groupby("batter")["runs"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_batsmen.plot(kind='barh', color='teal')
plt.title("Top 10 Batsmen by Runs")
plt.xlabel("Runs")
plt.ylabel("Batsman")
plt.gca().invert_yaxis()
plt.show()


# In[12]:


# Top 10 teams by total runs
team_runs = df.groupby("team")["runs"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))
team_runs.head(10).plot(kind='bar', color='orange')
plt.title("Top 10 Teams by Total Runs")
plt.ylabel("Total Runs")
plt.xlabel("Team")
plt.xticks(rotation=45)
plt.show()


# In[13]:


# Year-wise total runs
year_runs = df.groupby("year")["runs"].sum().sort_index()

import matplotlib.pyplot as plt

plt.figure(figsize=(12,5))
plt.plot(year_runs.index, year_runs.values, marker='o', color='green')
plt.title("Year-wise Total Runs in T20 Matches")
plt.xlabel("Year")
plt.ylabel("Total Runs")
plt.grid(True)
plt.tight_layout()
plt.show()


# In[ ]:




