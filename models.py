from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()


class Match(Base):
    __tablename__ = 'matches'

    id = Column(String(50), primary_key=True)
    home_team = Column(String(100))
    away_team = Column(String(100))
    match_stats_key = Column(String(50))
    start_time = Column(String(100))
    match_round = Column(Integer)
    venue = Column(String(100))


    def __repr__(self):
        return '<Match {0}. Home: {1}, Away: {2}, Match stats key: {3}, start_time: {4}, Match round: {5}, Venue: {6}>'.format(self.id,
                                               self.home_team,
                                               self.away_team,
                                               self.match_stats_key,
                                               self.start_time,
                                               self.match_round,
                                               self.venue)

#engine = create_engine(os.environ["DATABASE_URL"])
#Base.metadata.create_all(engine)
