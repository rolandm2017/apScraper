class Scrape:
    def __init__(self, results):
        self.results = results
        self.issues = []

    def add_issue(self, issue):
        self.issues.append(issue)

    def get_results(self):
        return self.results

    def get_issues(self):
        return self.issues
