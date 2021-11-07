"""
Homework Assignment #7: Dictionaries and Sets
"""

Song = {"SongArtist": "Roxette", "SongGenre": "Pop rock", "SongSinger": "Marie Fredriksson", "SongTitle": "The look",
        "SongRank": "10", "SongDuration": "3:57", "SongWriter": "Per Gessle"}

for key in Song:
    print(key + ": " + Song[key])

print("---")


def checkKeyVal(key, value):
    if Song[key] == value:
        print(True)
    else:
        print(False)


key = input("Guess key: ")
value = input("Guess value: ")

print("---")

checkKeyVal(key, value)
