import requests
import csv

"""
Module that fetches and processes posts from an API.
"""

URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder API and prints
    the status code followed by the titles of all posts
    if the request is successful.
    """
    response = requests.get(URL)
    print(f"Status code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()

        for post in data:
            print(post["title"])
        
def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder API and saves
    selected fields (id, title, body) into a CSV file
    named 'posts.csv' if the request is successful.
    """
    response = requests.get(URL)
    
    if response.status_code == 200:
        data = response.json()

        posts_list = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            for post in data
        ]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])

            writer.writeheader()
            writer.writerows(posts_list)
