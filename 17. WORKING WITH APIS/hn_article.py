import requests
import json

class HNEws:

    def __init__(self):
        self.url = 'https://hacker-news.firebaseio.com/v0/item/31353677.json'
        self.r = None
    
    def make_an_api_call_and_store_the_response(self):
        self.r = requests.get(self.url)
        print(f"Status code: {self.r.status_code}")

    def explore_the_structure_of_the_data(self):
        response_dict = self.r.json()
        response_string = json.dumps(response_dict, indent=4)
        print(response_string)

    def run(self):
        self.make_an_api_call_and_store_the_response()
        self.explore_the_structure_of_the_data()

if __name__ == '__main__':
    Data = HNEws()
    Data.run()