#!/usr/bin/python3
""" a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None."""

from requests import get

def recurse(subreddit, hot_list=[], after=""):
    """recursive function that queries the Reddit API and returns a list """
    if after is None:
        return hot_list
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    req = get(url, headers={'user-agent': 'my-app/0.0.1'},
            params={'limit': 100, 'after': after}, allow_redirects=False)
    if req.status_code != 200:
        return None
    try:
        jsonf = req.json()
    except ValueError:
        return None
    try:
        data = jsonf.get("data")
        after = data.get("after")
        children = data.get("children")
        for child in children:
            post = child.get("data")
            hot_list.append(post.get("title"))
    except:
        return None
    return recurse(subreddit, hot_list, after)

