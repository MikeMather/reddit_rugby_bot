import praw






class RedditBot(praw.Reddit):

    agent = "Rugby Union match thread bot by u/justdelighted"
    success = False
    postTitle = ""
    postContent = ""

    def __init__(self, client_id, secret_key, username, password):
        praw.Reddit(self, user_agent=self.agent, client_id=client_id, secret_key=secret_key, username=username, password=password)



    def renderSubmission(data):

        self.postTitle = "Match Thread: %s vs %s 🏉 Round %s" % (data["home_team"], data["away_team"], data["round"])

        self.postContent = """### [Official lineups & live stats](""" + data["url"] + """)
                            Start time: """ + data["start_time"] + """
                            Click [HERE](http://www.thetimezoneconverter.com/?t=""" + data["start_time"] + """&tz=UTC&) to convert to your time.

                            Venue: """ + data["venue"] + """

                            <sub><sub>I am a bot. Bleep bloop</sub></sub>
                            """
