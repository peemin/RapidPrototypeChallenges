import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album, Artist
 
engine = create_engine('sqlite:///mymusic.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
# querying for a record in the Artist table
res = session.query(Artist).filter(Artist.name=="Beach Boys").first()
print res
 
# Create a new album
res.albums = [Album("Surfing USA", 
                           datetime.date(1963,11,16), "MCA Records", "CD")]
  
# Add the record to the session object
session.add(res)

session.commit()