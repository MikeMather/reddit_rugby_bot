from bs4 import BeautifulSoup
import requests

def getMatchLink(url, home_team, away_team):

    html = requests.get(url)

    soup = BeautifulSoup(html.text, "html.parser")

    elements = soup.findAll("span", class_="sr-only")

    for i in elements:
        print(i)




if __name__ == "__main__":
    url = "http://sanzarrugby.com/superrugby/match-centre/?season=2018&competition=205"
    home = "STORMERS"
    away = "JAGUARES"
    print(getMatchLink(url, home, away))
