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
    list_of_songs = []
    genre_lower = genre.lower()
    for song in songs:
        if song[2].lower() == genre_lower:
            list_of_songs.append(song)
    return list_of_songs

def get_by_artist(songs, artist):
    result = []
    artist_lower = artist.lower()
    for song in songs:
        if song[1].lower() == artist_lower:
            result.append(song)
    return result

def unique_artists(songs):
    artists = []
    seen = set()
    for song in songs:
        if song[1] not in seen:
            seen.add(song[1])
            artists.append(song[1])
    return artists

def search_title(songs, text):
    title_songs = []
    text_lower = text.lower()  # Не изменяем оригинальный параметр
    for song in songs:
        if text_lower in song[0].lower():
            title_songs.append(song)
    return title_songs

def top_longest(songs, n):
    def time_to_seconds(time_str):
        parts = time_str.split(':')
        if len(parts) == 2:
            return int(parts[0]) * 60 + int(parts[1])
        return 0

    return sorted(songs, key=lambda s: time_to_seconds(s[3]), reverse=True)[:n]




print(get_by_genre(SONGS, "rock"))
print(get_by_artist(SONGS, "Billie Eilish"))
print(unique_artists(SONGS))
print(search_title(SONGS, "na"))
print( top_longest(SONGS, 3))

