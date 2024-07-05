from operator import itemgetter
import requests
import plotly.express as px

class HNews:

    def __init__(self):
        self.url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
        self.r = None
        self.submission_dicts = []
        self.titles = None
        self.comments = None
        self.hover_texts = None

    def make_an_api_call_and_check_the_response(self):
        self.r = requests.get(self.url)
        print(f"Status code: {self.r.status_code}")

    def process_information_about_each_submission(self):
        submission_ids = self.r.json()

        for submission_id in submission_ids[:10]:  
            url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
            self.r = requests.get(url)
            print(f"id: {submission_id}\tstatus: {self.r.status_code}")
            response_dict = self.r.json()

            try:
                submission_dict = {
                    'title': response_dict['title'],
                    'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
                    'comments': response_dict['descendants'],
                }       
                self.submission_dicts.append(submission_dict)
            except KeyError as e:
                print(f"Skipping submission {submission_id} due to missing data: {e}")

        self.submission_dicts = sorted(self.submission_dicts, key=itemgetter('comments'), reverse=True)

    def print_output(self):
        for submission_dict in self.submission_dicts:
            print(f"\nTitle: {submission_dict['title']}")
            print(f"Discussion link: {submission_dict['hn_link']}")
            print(f"Comments: {submission_dict['comments']}")

    def prepare_data_for_the_bar_chart(self):
        self.titles = [f"<a href='{sub['hn_link']}'>{sub['title']}</a>" for sub in self.submission_dicts]
        self.comments = [sub['comments'] for sub in self.submission_dicts]
        self.hover_texts = [f"{sub['title']} ({sub['comments']} comments)" for sub in self.submission_dicts]

    def make_the_visualization(self):
        title = "Most Active Discussions on Hacker News"
        labels = {'x': 'Title', 'y': 'Comments'}

        fig = px.bar(x=self.titles, y=self.comments, title=title, labels=labels, text=self.comments)
        fig.update_layout(xaxis_tickangle=-45)
        fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
        fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6, textposition='outside',
                        hovertemplate='<b>%{customdata}</b><br>Comments: %{y}<extra></extra>',
                        customdata=self.hover_texts)

        fig.show()
    
    def run(self):
        self.make_an_api_call_and_check_the_response()
        self.process_information_about_each_submission()
        self.print_output()
        self.prepare_data_for_the_bar_chart()
        self.make_the_visualization()

if __name__ == '__main__':
    Data = HNews()
    Data.run()