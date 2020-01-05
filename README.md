# Reddit Ruby Bot

This app was created for the [r/rugbyunion](https://reddit.com/r/rugbyunion) community, a community dedicated to discussion about rugby, to automatically create match threads for upcoming Super Rugby games

The app pulls the data, and stores it in a PostgreSQL database. Once saved, it is deployed as a Flask (Python) web application to a Heroku server where it checks the database periodically to look for upcoming games. When a game is coming up, it creates the match thread with all the appropriate information, linking to tools for time zones and live match statistics.

The app has been used every year in the community since 2017
