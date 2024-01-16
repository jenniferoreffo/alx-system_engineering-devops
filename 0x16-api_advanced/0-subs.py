#!/usr/bin/python3
"""  a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit."""

from requests import get
from json import loads

def number_of_subscribers(subreddit):
    """queries to Reddit Api"""
    u_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    headers = {
            'User-Agent': u_agent
    }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = get(url, headers=headers)
    reddits = response.json()

    try:
        subscribers = reddits.get('data').get('subscribers')
        return int(subscribers)
    except:
        return 0
