import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table2_def import Album, Artist
 
engine = create_engine('sqlite:///mymusic1.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
# Create an artist
new_artist = Artist("Lyle Lovett")
new_artist.albums = [Album("Lyle Lovette and His Large Band", 
                           "Country", "MCA Records", "CD")]
 
# add more albums
more_albums = [Album("Release Me",
                     "Country",
                     "MCA Records", "CD")]
new_artist.albums.extend(more_albums)
 
# Add the record to the session object
session.add(new_artist)
# commit the record the database
session.commit()
 
# Add artist2
artist2 = Artist("Beach Boys")
artist2.albums = [Album("Surfer Girl", 
                           "Rock and Roll", "Publisher 1", "CD"),
                     Album("Summer Days", 
                           "Rock and Roll", "MCA Records", "CD")]
 
# Add the record to the session object
session.add(artist2)
# commit the record the database
session.commit

artist3 = Artist("Devo")
artist3.albums = [Album("Girl U Want", 
                           "Punk Rock", "Publisher 1", "CD"),
                     Album("Army Girls Gone Wild", 
                           "New Wave", "Publisher2", "CD")]
 
# Add the record to the session object
session.add(artist3)
# commit the record the database
session.commit()