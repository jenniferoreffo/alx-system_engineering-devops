#!/usr/bin/python3
""" a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit. 
"""

from requests import gets

def top_ten(subreddit)
    """queries to Reddit Api"""
      url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
      headers = {'user-agent': 'my-app/0.0.1'}
      req = get(url, headers=headers,
              allow_redirects=False, params={"limit": 10})
      if req.status_code != 200:
          print(None)
          return None
      try:
          jsonf = req.json()
      except ValueError:
          print(None)
          return None
      try:
          data = jsonf.get("data")
          children = data.get("children")
          for child in children:
              post = child.get("data")
              print(post.get("title"))
      except Exception:
          print(None)
