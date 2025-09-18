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
        if song[2].lower() == genre.lower():
            result.append(song)
    return result

def get_by_artist(songs, artist):
    result = []
    for song in songs:
        if song[1].lower() == artist.lower():
            result.append(song)
    return result

def unique_artists(songs):
    result = []
    for song in songs:
        artist = song[1]
        if artist not in result:
            result.append(artist)
    return result

def search_title(songs, text):
    result = []
    for song in songs:
        if text.lower() in song[0].lower():
            result.append(song)
    return result

def top_longest(songs, n):
    def duration_to_seconds(mmss):
        minutes, seconds = mmss.split(':')
        return int(minutes) * 60 + int(seconds)

    sorted_songs = sorted(songs, key=lambda song: duration_to_seconds(song[3]), reverse=True)
    return sorted_songs[:n]
