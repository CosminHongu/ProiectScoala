from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://CAIA:postgres@localhost:5432/CAIA1')

#Creare conexiune noua la baza de date
Session = sessionmaker(bind=engine)

Base = declarative_base()