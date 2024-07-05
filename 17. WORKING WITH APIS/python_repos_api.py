import requests

class GitRepos:

    def __init__(self):
        self.url = 'https://api.github.com/search/repositories'
        self.url += '?q=language:python+sort:stars+stars:>10000'
        self.r = None
        self.response_dict = None
        self.repo_dicts = []
    
    def make_api_call_and_check_response(self):
        headers = {"Accept": "application/vnd.github.v3+json"}
        self.r = requests.get(self.url, headers=headers)
        print(f"Status code: {self.r.status_code}")

    def convert_response_object_to_dictionary(self):
        self.response_dict = self.r.json()

    def process_results(self):
        print(self.response_dict.keys())
        print(f"Total repositories: {self.response_dict['total_count']}")
        print(f"Complete results: {not self.response_dict['incomplete_results']}")

    def explore_information_about_the_repositories(self):
        self.repo_dicts = self.response_dict['items']
        print(f"Repositories returned: {len(self.repo_dicts)}")

    def examine_the_first_repository(self):
        repo_dict = self.repo_dicts[0]
        print(f"\nKeys: {len(repo_dict)}")
        for key in sorted(repo_dict.keys()):
            print(key)

    def print_selected_information_about_repositories(self):
        print("\n\t---Selected information about repositories---")
        for repo_dict in self.repo_dicts:
            print(f"\nName: {repo_dict['name']}")
            print(f"Owner: {repo_dict['owner']['login']}")
            print(f"Stars: {repo_dict['stargazers_count']}")
            print(f"Repository: {repo_dict['html_url']}")
            print(f"Created: {repo_dict['created_at']}")
            print(f"Updated: {repo_dict['updated_at']}")
            print(f"Description: {repo_dict['description']}")
    
    def run(self):
        self.make_api_call_and_check_response()
        self.convert_response_object_to_dictionary()
        self.process_results()
        self.explore_information_about_the_repositories()
        self.examine_the_first_repository()
        self.print_selected_information_about_repositories()

if __name__ == '__main__':
    Data = GitRepos()
    Data.run()