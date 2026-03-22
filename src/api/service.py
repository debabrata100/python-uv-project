from .config import Api_Config
from dotenv import load_dotenv
import requests
import os

load_dotenv()


class Api_Service:
    def __init__(self):
        self.api_config = Api_Config(os.getenv("API_KEY"))
        pass

    def get_profile(self):
        try:
            response = requests.get(
                self.api_config.profile(), headers=self.api_config.headers()
            )
            return response.json()
        except Exception as e:
            print(f"How exceptional! {e}")
            return None

    def get_repos(self, repos_url):
        try:
            response = requests.get(repos_url, headers=self.api_config.headers())
            return response.json()
        except Exception as e:
            print(f"How exceptional! {e}")
            return None
