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

def get_by_genre(songs, genre):
    result = []
    for song in songs:
        if song[2].casefold() == genre.casefold():
            result.append(song)
    return result

def get_by_artist(songs, artist):
    result = []
    for song in songs:
        if song[1].casefold() == artist.casefold():
            result.append(song)
    return result

def unique_artists(songs):
    result = []
    seen = set()
    for song in songs:
        artist_bro = song[1].casefold()
        if artist_bro not in seen:
            seen.add(artist_bro)
            result.append(song[1])
        return result

def search_title(songs, text):
    result = []
    for song in songs:
        song_bro = song[0].casefold()
        if text.casefold() in song_bro:
         result.append(song)
    return result

def top_longest(songs, n):
    if n <= 0:
        return "зачем тебе ноль самых длинных песен?..."
    result = []
    for song in songs:
        GG, WP = song[3].split(":", 1)
        total = int(GG) * 60 + int(WP)
        result.append((total, song))
    result.sort(key = lambda x: x[0], reverse = True)
    return [s for _, s in result[:n]]

print(get_by_genre(SONGS, "rock"))
print(get_by_artist(SONGS, "Eminem"))
print(unique_artists(SONGS))
print(search_title(SONGS, "numb"))
print(top_longest(SONGS, 2))
