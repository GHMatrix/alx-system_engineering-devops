#!/usr/bin/python3

import requests


def top_ten(subreddit):
    """
    Query the Reddit API and print the titles of the
    first 10 hot posts for a given subreddit.

    :param subreddit: The name of the subreddit to query.
    :type subreddit: str
    """
    # Define the URL of the Reddit API for the given subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Define a custom User-Agent to avoid Too Many Requests errors
    headers = {"User-Agent": "my_bot"}

    # Send an HTTP GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract and print the titles of the first 10 hot posts
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        # If the subreddit is invalid or another error occurs, print None
        print(None)


# If this script is run as the main program, test it with a subreddit argument
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
