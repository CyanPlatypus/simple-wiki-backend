from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://simple_wiki_user:toosimple@localhost:3306/simple_wiki')
Session = sessionmaker(bind=engine)

Base = declarative_base()