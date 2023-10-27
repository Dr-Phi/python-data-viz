import requests
import plotly.express as px

# Make an API call and check the response
url = "https://api.github.com/search/repositories"
url += "?q=language:Javascript+sort:stars+stars:>10000"

headers = {"Accept": "aplication/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process overall results
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# Process repo info
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []

for rd in repo_dicts:
    repo_url = rd['html_url']
    repo_link = f"<a href='{repo_url}'>{rd['name']}</a>"
    repo_links.append(repo_link)
    stars.append(rd['stargazers_count'])
    #Build hover texts (tooltips)
    hover_text = f"{rd['owner']['login']}<br /> {rd['description']}"
    hover_texts.append(hover_text)

# Make visualization
title = "Most-starred Javascript projects on Github"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()
