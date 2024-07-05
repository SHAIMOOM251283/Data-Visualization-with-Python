import requests
import plotly.express as px 

class GitRepos:

    def __init__(self):
        self.url = 'https://api.github.com/search/repositories'
        self.url += '?q=language:python+sort:stars+stars:>10000'
        self.r = None
        self.repo_names = []
        self.stars = []
        self.hover_texts = []

    def get_repos(self):
        headers = {"Accept": "application/vnd.github.v3+json"}
        self.r = requests.get(self.url, headers=headers)
        print(f"Status code: {self.r.status_code}")

    def process_repos(self):
        response_dict = self.r.json()
        print(f"Complete results: {not response_dict['incomplete_results']}")

        # Process repository information.
        repo_dicts = response_dict['items']

        for repo_dict in repo_dicts:
            self.repo_names.append(repo_dict['name'])
            self.stars.append(repo_dict['stargazers_count'])
            # Build hover texts.
            owner = repo_dict['owner']['login']
            description = repo_dict['description']
            hover_text = f"{owner}<br />{description}"
            self.hover_texts.append(hover_text)

    def make_visualization(self):
        title = "Most-Starred Python Projects on GitHub"
        labels = {'x': 'Repository', 'y': 'Stars'}
        fig = px.bar(x=self.repo_names, y=self.stars, title=title, labels=labels, hover_name=self.hover_texts)
        fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
        fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

        fig.show()
    
    def run(self):
        self.get_repos()
        self.process_repos()
        self.make_visualization()

if __name__ == '__main__':
    Visualize = GitRepos()
    Visualize.run()