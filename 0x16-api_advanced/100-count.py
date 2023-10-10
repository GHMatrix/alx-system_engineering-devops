#!/usr/bin/python3
"""
Recursive function querrying Reddit API, parsing
the title of hot articles.
"""

import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    Recursively query the Reddit API, parse titles,
    and print a sorted count of given keywords.

    :param subreddit: The name of the subreddit to query.
    :type subreddit: str
    :param word_list: A list of keywords to count.
    :type word_list: list
    :param hot_list: A list to accumulate the titles of
    hot articles (used in recursion).
    :type hot_list: list
    :param after: A parameter used to paginate through
    results (used in recursion).
    :type after: str
    """
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
            hot_list.append(post["data"]["title"].lower())

        # Check if there are more pages of results
        after = data["data"]["after"]
        if after is not None:
            # Recursively call the function to fetch the next page of results
            return count_words(subreddit, word_list, hot_list, after)
        else:
            # If no more results, count the keywords and print the results
            count_and_print_keywords(word_list, hot_list)
    else:
        # If the subreddit is invalid or an error occurs, print nothing
        pass


def count_and_print_keywords(word_list, hot_list):
    """
    Count and print the sorted count of keywords in the hot articles list.

    :param word_list: A list of keywords to count.
    :type word_list: list
    :param hot_list: A list containing the titles of hot articles.
    :type hot_list: list
    """
    # Create a dictionary to store the counts of keywords
    keyword_counts = {}

    # Count the keywords in the hot articles
    for title in hot_list:
        for keyword in word_list:
            # Check if the keyword is surrounded by non-alphanumeric characters
            keyword_count = title.count(f' {keyword} ')
            keyword_counts[keyword] = keyword_counts.get(
                    keyword, 0) + keyword_count

    sorted_keywords = sorted(
            keyword_counts.items(), key=lambda x: (-x[1], x[0]))

    # Print the sorted keyword counts
    for keyword, count in sorted_keywords:
        print(f"{keyword}: {count}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'"
              .format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = [x.lower() for x in sys.argv[2].split()]
        count_words(subreddit, word_list)
