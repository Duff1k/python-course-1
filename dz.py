SONGS = [
    ("Blinding Lights", "The Weeknd", "pop", "03:20"),
    ("Levitating", "Dua Lipa", "pop", "03:23"),
    ("Believer", "Imagine Dragons", "rock", "03:24"),
    ("Do I Wanna Know?", "Arctic Monkeys", "indie", "04:32"),
    ("bad guy", "Billie Eilish", "pop", "03:14"),
    ("HUMBLE.", "Kendrick Lamar", "hip-hop", "02:57"),
    ("Numb", "Linkin Park", "rock", "03:07"),
    ("Nothing Else Matters", "Metallica", "metal", "06:28"),
    ("Shape of You", "Ed Sheeran", "pop", "03:53"),
    ("Lose Yourself", "Eminem", "hip-hop", "05:26"),
    ("Smells Like Teen Spirit", "Nirvana", "rock", "05:01"),
    ("Starboy", "The Weeknd", "pop", "03:50"),
    ("Get Lucky", "Daft Punk", "electronic", "04:08"),
    ("Sunset Lover", "Petit Biscuit", "electronic", "03:58"),
    ("Time", "Hans Zimmer", "soundtrack", "04:35"),
    ("Happier Than Ever", "Billie Eilish", "indie", "04:58"),
    ("Circles", "Post Malone", "pop", "03:35"),
    ("The Less I Know The Better", "Tame Impala", "indie", "03:36"),
]

#Task 1: return songs by genre
def get_by_genre(SONGS, genre):
    genre_lower = genre.lower()
    return [x for x in SONGS if x[2].lower() == genre_lower]

rock_songs = get_by_genre(SONGS, "rock")
print("LET'S ROCK:")
for x in rock_songs:
    print(x[0])

indie_songs = get_by_genre(SONGS, "indie")
print("\nFEEL THE INDIE BLAZE:")
for x in indie_songs:
    print(x[0])

#Task 2: return songs by artist
def get_by_genre(SONGS, artist):
    artist_lower = artist.lower()
    return [x for x in SONGS if x[1].lower() == artist_lower]

artist_songs = get_by_genre(SONGS, "Imagine Dragons")
print("\nYOU WANT DRAGONS? YOU GET DRAGONS:")
for x in artist_songs:
    print(x[0])

#Task 3: return unique artists
def unique_artists(SONGS):
    result = []
    for x in SONGS:
        artist = x[1]
        if artist not in result:
            result.append(artist)
    return result

artists = unique_artists(SONGS)
print("\nARTISTS BY ORDER OF APPEARANCE:")
print("\n".join(artists))

#Task 4: return songs with 'text' in the title
def search_title(SONGS, text):
    text_lower = text.lower()
    return [x for x in SONGS if text_lower in x[0].lower()]

songs_with_text = search_title (SONGS, "text")
print("\nRESULT:")
for x in songs_with_text:
    print(x[0])
