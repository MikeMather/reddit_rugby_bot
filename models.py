from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Match(Base):
    __tablename__ = 'matches'

    id = Column(String(50), primary_key=True)
    home_team = Column(String(100))
    away_team = Column(String(100))


    def __repr__(self):
        return '<Match {0}. Home: {1}, Away: {2}>'.format(self.id,
                                               self.home_team,
                                               self.away_team)
