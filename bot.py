import requests
import pytz
from datetime import datetime
import os
from config import *
from models import Match
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import re
from RedditBot import RedditBot


def formatTeamName(team):
    team = team.lower()
    return team.replace("the ", "").capitalize()



def main():

    DEV = True

    if DEV:
        config = DevelopmentConfig()
        today = datetime.strptime("2018-02-17", "%Y-%m-%d")
        engine = create_engine('sqlite:///:matches.db:', echo=False)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.query(Match).delete()

    else:
        config = ProductionConfig()
        today = datetime.now()
        engine = create_engine('sqlite:///:matches-dev.db:', echo=False)
        Session = sessionmaker(bind=engine)
        session = Session()




    crawlerUrl = 'http://sanzarrugby.com/superrugby/match-centre/?season={0}&competition=205'.format(today.strftime("%Y"))
    url = 'https://api.sportradar.us/rugby/trial/v2/union/en/schedules/{0}/schedule.json?api_key={1}'.format(today.strftime("%Y-%m-%d"), config.API_KEY)

    r = requests.get(url)
    resp = r.json()

    for match in resp['sport_events']:

        game = {}
        if match['sport_event_context']['competition']['name'] == "Super Rugby":
            game["match_id"] = match["id"]
            game["home_team"] = formatTeamName(match["competitors"][0]["name"])
            game["away_team"] = formatTeamName(match["competitors"][1]["name"])

            matches = re.match(r'^([\d-]+).{4}([\d:]+).*', match["scheduled"])

            start_time = datetime.strptime(matches.group(1) + " " + matches.group(2), "%Y-%m-%d %H:%M")

            game["start_time"] = start_time
            game["venue"] = match["venue"]["name"] + ", " + match["venue"]["city_name"]
            game["round"] = match["sport_event_context"]["stage"]["round"]
            game["url"] = crawlerUrl #To be changed

            if config.DEBUG:
                print(game)

            if session.query(Match).filter_by(id=game["match_id"]).count() == 0:
                match = Match()
                match.id = game["match_id"]
                match.home_team = game["home_team"]
                match.away_team = game["away_team"]

                bot = RedditBot(config.CLIENT_ID, config.SECRET_KEY, config.USERNAME, config.PASSWORD)

                bot.renderSubmission(game)
                if config.DEBUG:
                    print(bot.postTitle)
                    print(bot.postContent)

                #bot.submit(config.SUBREDDIT)

                #if bot.success:
                #    session.add(match)
                #    session.commit()
            else:
                print("Games already posted")



if "__main__" == __name__:
    main()
