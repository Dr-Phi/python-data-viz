from operator import itemgetter
import requests
import plotly.express as px

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:5]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    # Build a dictionary for each article.
    submission_dict = {
    'title': response_dict['title'],
    'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
    'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
 reverse=True)
for submission_dict in submission_dicts:
 print(f"\nTitle: {submission_dict['title']}")
 print(f"Discussion link: {submission_dict['hn_link']}")
 print(f"Comments: {submission_dict['comments']}")

 disc_links, comments, hover_texts = [], [], []

for sd in submission_dicts:
    try:
        disc_link = f"<a href='{sd['hn_link']}'>{sd['title']}</a>"
    except KeyError:
        print('promotional link')
        continue
    else:
        disc_links.append(disc_link)
        comments.append(sd['comments'])

# Make visualization
title = "Most active discussions on HackerNews"
labels = {'x': 'Discussions', 'y': 'Comments'}
fig = px.bar(x=disc_links, y=comments, title=title, labels=labels)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()
