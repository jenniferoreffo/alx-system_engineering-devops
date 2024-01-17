#!/usr/bin/python3
"""  a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit."""

from requests import get

def number_of_subscribers(subreddit):
    """queries to Reddit Api"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {'user-agent': 'my-app/0.0.1'}

    req = get(url, headers=headers, allow_redirects=False)

    if req.status_code != 200:
        return 0
    try:
        jsonf = req.json()
    except ValueError:
        return 0    
    data = jsonf.get("data")
    if data:
        sub_count = data["subscribers"]
        if sub_count:
            return sub_count
    return 0
