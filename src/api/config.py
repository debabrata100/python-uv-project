class Api_Config:
    def __init__(self, api_key):
        self.api_key = api_key

    def headers(self):
        return {"Authorization": f"token {self.api_key}"}

    def profile(self):
        return "https://api.github.com/user"
