"""
It's about my favorite song
"""

# Declaring variables
SongArtist = "Roxette"

SongGenre = "Pop rock"
SongSinger = "Marie Fredriksson"
SongTitle = "The look"
SongRank = 10
SongDuration = "3:57"
SongWriter = "Per Gessle"

""" Making variables output
print(SongArtist)
print(SongGenre)
print(SongTitle)
print(SongRank)
print(SongDuration)
print(SongWriter)
"""

def songArtist(Artist):
    return Artist

def songRank(Rank):
    return Rank

def songWriter(Writer):
    return Writer

def songInTheDB():
    return True

#Making functions output
print("Artist: " + songArtist(SongArtist))
print("Rank:" + str(songRank(SongRank)))
print("Writer:" + songWriter(SongWriter))
if (songInTheDB()):
    print("This song is in our database");
