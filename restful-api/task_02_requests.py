#!/usr/bin/python3
"""Fetch and process posts from an API."""

import csv
import requests


URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch posts and print the status code and post titles."""
    response = requests.get(URL)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch posts and save selected data to a CSV file."""
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()

        post_data = []

        for post in posts:
            post_data.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(post_data)
