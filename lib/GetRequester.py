import requests
import json

class GetRequester:
    
    dbUrl = ''

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        dbUrl = self.url
        response = requests.get(dbUrl)
        return response.content

    def load_json(self):
        json_response = json.loads(self.get_response_body())
        return json_response
        