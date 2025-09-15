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
    list_of_songs=[]
    for song in songs:
        if song[2] == genre.lower():
            list_of_songs.append(song)
        else:
            continue
    return list_of_songs
    
print(get_by_genre(SONGS, "pop"))

def get_by_artist(songs, artist):
    songs_by_artist=[]
    for song in songs:
        if song[1].lower() == artist.lower():
            songs_by_artist.append(song)
        else:
            continue
    return songs_by_artist
print(get_by_artist(SONGS, "The Weeknd"))

def unique_artists(songs):
    seen = set()
    artists = []
    for _, artist, _, _ in songs:
        if artist not in seen:
            seen.add(artist)
            artists.append(artist)
    return artists
print(unique_artists(SONGS))

def search_title(songs, text):
    text = text.lower()
    title_songs = []
    for song in songs:
        if text in song[0].lower():
            title_songs.append(song[0])
        else:
            continue
    return title_songs
print(search_title(SONGS, "love"))

def top_longest(songs, n):
    def time_to_seconds(time_str):
        minutes, seconds = map(int, time_str.split(':'))
        return minutes * 60 + seconds

    sorted_songs = sorted(songs, key=lambda song: time_to_seconds(song[3]), reverse=True)
    return sorted_songs[:n]
print(top_longest(SONGS, 3))

