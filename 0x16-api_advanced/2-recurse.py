#!/usr/bin/python3

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively query the Reddit API and return a list containing
    the titles of all hot articles for a given subreddit.

    :param subreddit: The name of the subreddit to query.
    :type subreddit: str
    :param hot_list: A list to accumulate the titles
    of hot articles (used in recursion).
    :type hot_list: list
    :param after: A parameter used to paginate through
    results (used in recursion).
    :type after: str

    :return: A list containing the titles of all hot articles.
    Returns None if no results are found.
    :rtype: list
    """
    # Define the URL of the Reddit API for the given subreddit,
    # including the "after" parameter for pagination
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    # Define a custom User-Agent to avoid Too Many Requests errors
    headers = {"User-Agent": "my_bot"}

    # Send an HTTP GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract the titles of hot articles and add them to the hot_list
        for post in data["data"]["children"]:
            hot_list.append(post["data"]["title"])

        # Check if there are more pages of results
        after = data["data"]["after"]
        if after is not None:
            # Recursively call the function to fetch the next page of results
            return recurse(subreddit, hot_list, after)
        else:
            # If no more results, return the accumulated hot_list
            return hot_list
    else:
        # If the subreddit is invalid or an error occurs, return None
        return None


# If this script is run as the main program, test it with a subreddit argument
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            for title in result:
                print(title)
        else:
            print("None")
