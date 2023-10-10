#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of
    subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit.
        Returns 0 for an invalid subreddit.
    """
    # Define the URL of the Reddit API for the given subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Define a custom User-Agent to avoid Too Many Requests errors
    headers = {"User-Agent": "my_bot"}

    # Send an HTTP GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract and return the number of subscribers
        return data["data"]["subscribers"]
    else:
        # If the subreddit is invalid or another error occurred, return 0
        return 0


# If this script is run as the main program, test it with a subreddit argument
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(subscribers)
