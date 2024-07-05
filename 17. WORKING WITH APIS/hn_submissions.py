from operator import itemgetter
import requests

class HNews:

    def __init__(self):
        self.url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
        self.r = None
        self.submission_dicts = []
    
    def make_an_api_call_and_check_the_response(self):
        self.r = requests.get(self.url)
        print(f"Status code: {self.r.status_code}")

    def process_information_about_each_submission(self):
        submission_ids = self.r.json()
        for submission_id in submission_ids[:5]:
            # Make a new API call for each submission.
            url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
            self.r = requests.get(url)
            print(f"id: {submission_id}\tstatus: {self.r.status_code}")
            response_dict = self.r.json()
            # Build a dictionary for each article.
            submission_dict = {
                'title': response_dict['title'],
                'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
                'comments': response_dict['descendants'],
            }
            self.submission_dicts.append(submission_dict)

        self.submission_dicts = sorted(self.submission_dicts, key=itemgetter('comments'), reverse=True)

    def print_output(self):
        for submission_dict in self.submission_dicts:
            print(f"\nTitle: {submission_dict['title']}")
            print(f"Discussion link: {submission_dict['hn_link']}")
            print(f"Comments: {submission_dict['comments']}")
    
    def run(self):
        self.make_an_api_call_and_check_the_response()
        self.process_information_about_each_submission()
        self.print_output()

if __name__ == '__main__':
    Data = HNews()
    Data.run()
    