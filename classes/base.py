from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://CAIA:delta1@localhost:5432/CAIA1')

Session = sessionmaker(bind=engine)

Base = declarative_base()