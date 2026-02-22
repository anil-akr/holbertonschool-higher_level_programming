#!/usr/bin/python3
"""
task_02_requests.py

Fetch and process posts from JSONPlaceholder API using requests.
"""

import requests
import csv


URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder and print their titles.

    Prints:
        - Status code of the HTTP response
        - Titles of all posts if request is successful
    """
    response = requests.get(URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder and save selected
    fields (id, title, body) into posts.csv.
    """
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()

        # Structure data
        structured_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        # Write to CSV
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(structured_posts)
