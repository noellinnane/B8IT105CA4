import pandas as pd

df = pd.read_csv('changes.csv', quotechar="'") #added quotes around the comment column in the csv as extra commas causing pandas issues


# Who has done the most revisions?

top_authors = df.groupby('author')[['revision']].count()
top_authors.columns=['Number of revisions']
print(top_authors)        

# What time are most revisions done?

top_times = df.groupby(df.time.str[:2])[['revision']].count()
top_times.columns=['Number of revisions']
print(top_times)

# What days are most revisions done?

df['date'] = pd.to_datetime(df['date'])

top_days = df.groupby(df.date.dt.weekday)[['revision']].count()
top_days.columns=['Number of revisions']
print(top_days)

