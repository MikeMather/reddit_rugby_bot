import praw



class RedditBot(praw.Reddit):

    agent = "Rugby Union match thread bot by u/justdelighted"
    success = False
    postTitle = ""
    postContent = ""
    url = "http://sanzarrugby.com/superrugby/match-centre/?season=2018&competition=205&match="

    def __init__(self, client_id, secret_key, username, password):
        praw.Reddit.__init__(self, user_agent=self.agent, client_id=client_id, client_secret=secret_key, username=username, password=password)

    def renderSubmission(self, data):

        self.postTitle = "Match Thread: %s vs %s 🏉 Round %s" % (data["home_team"], data["away_team"], data["round"])

        self.postContent = """

&nbsp;

### [Official lineups & live stats](""" + self.url + data["match_stats_key"] + """)

&nbsp;

**Venue**: """ + data["venue"] + """


**Start time**: """ + data["start_time"].strftime("%H:%M") + """ UTC


Click [HERE](http://www.thetimezoneconverter.com/?t=""" + data["start_time"].strftime("%H:%M") + """&tz=UTC&) to convert to your time.

&nbsp;

^(I am a bot. Bleep bloop)"""

    def submit(self, subreddit):

        try:
            self.subreddit(subreddit).submit(self.postTitle, selftext=self.postContent)
            print("Post submitted to " + subreddit)
            return True
        except:
            print("Failed to submit post, trying again in 3 minutes...")
            return False
