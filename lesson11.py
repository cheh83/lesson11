from abc import ABC, abstractmethod
from typing import List


class SocialChannel(ABC):
    def __init__(self, name: str, followers: int):
        self.name = name
        self.followers = followers

    @abstractmethod
    def post_message(self, message: str, timestamp: str):
        pass


class YouTube(SocialChannel):
    def post_message(self, message: str, timestamp: str):
        print(
            f"Posting to {self.name} with {self.followers} followers at {timestamp}: {message}"
        )


class Facebook(SocialChannel):
    def post_message(self, message: str, timestamp: str):
        print(
            f"Posting to {self.name} with {self.followers} followers at {timestamp}: {message}"
        )


class Twitter(SocialChannel):
    def post_message(self, message: str, timestamp: str):
        print(
            f"Posting to {self.name} with {self.followers} followers at {timestamp}: {message}"
        )


def post_a_message(channel_name: str, message: str, timestamp: str) -> None:
    if channel_name.lower() == "youtube":
        channel = YouTube(name="YouTube", followers=1000)
    elif channel_name.lower() == "facebook":
        channel = Facebook(name="Facebook", followers=2000)
    elif channel_name.lower() == "twitter":
        channel = Twitter(name="Twitter", followers=3000)
    else:
        raise ValueError("Invalid channel name")

    channel.post_message(message, timestamp)


def process_schedule(posts: List[dict]) -> None:
    for post in posts:
        message, timestamp, channel_name = (
            post["message"],
            post["timestamp"],
            post["channel"],
        )
        post_a_message(channel_name, message, timestamp)


if __name__ == "__main__":
    posts = [
        {"message": "Hello Youtube!", "timestamp": "10:00", "channel": "YouTube"},
        {"message": "Hello Facebook!", "timestamp": "05:30", "channel": "Facebook"},
        {"message": "Hello Twitter!", "timestamp": "03:15", "channel": "Twitter"},
    ]

    process_schedule(posts)
