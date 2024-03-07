import requests
import time

class GitHubAPI:
    def __init__(self, token=None):
        self.base_url = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "X-GitHub-Api-Version": "2022-11-28"
        }
        if token:
            self.headers["Authorization"] = f"token {token}"
        self.rate_limit_remaining = None

    def _update_rate_limit(self, response):
        self.rate_limit_remaining = int(response.headers.get('X-RateLimit-Remaining', 0))
        self.last_response = response

    def _wait_for_rate_limit_reset(self):
        reset_time = int(self.last_response.headers.get('X-RateLimit-Reset', 0))
        sleep_duration = reset_time - time.time() + 1  # Add 1 second to ensure the reset has occurred
        if sleep_duration > 0:
            print(f"Rate limit exceeded. Waiting for {sleep_duration} seconds.")
            time.sleep(sleep_duration)
    
    def make_paginated_request(self, endpoint, params=None):
        all_items = []
        page = 1
        while True:
            if params is None:
                params = {}
            params['page'] = page
            items = self.make_request(endpoint, params)
            if not items:
                break
            all_items.extend(items)
            page += 1
        return all_items
    
    def make_request(self, endpoint, params=None):
        if self.rate_limit_remaining is not None and self.rate_limit_remaining <= 1:
            self._wait_for_rate_limit_reset()

        response = requests.get(f"{self.base_url}/{endpoint}", headers=self.headers, params=params)
        self._update_rate_limit(response)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 403 and "rate limit exceeded" in response.text.lower():
            self._wait_for_rate_limit_reset()
            return self.make_request(endpoint, params)
        else:
            raise Exception(f"GitHub API request failed with status code {response.status_code}: {response.text}")
