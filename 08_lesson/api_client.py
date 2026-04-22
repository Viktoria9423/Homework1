import requests
from config import BASE_URL, LOGIN, PASSWORD, COMPANY_ID


class YougileAPI:

    def __init__(self):
        self.token = self.get_token()

        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

    def get_token(self):
        url = f"{BASE_URL}/auth/keys"

        payload = {
            "login": LOGIN,
            "password": PASSWORD,
            "companyId": COMPANY_ID
        }

        response = requests.post(url, json=payload)
        data = response.json()

        if "key" not in data:
            raise Exception(f"Auth error: {data}")

        return data["key"]

    def create_project(self, title):
        url = f"{BASE_URL}/projects"

        payload = {"title": title}

        return requests.post(url, json=payload, headers=self.headers)

    def update_project(self, project_id, title):
        url = f"{BASE_URL}/projects/{project_id}"

        payload = {"title": title}

        return requests.put(url, json=payload, headers=self.headers)

    def get_project(self, project_id):
        url = f"{BASE_URL}/projects/{project_id}"

        return requests.get(url, headers=self.headers)
