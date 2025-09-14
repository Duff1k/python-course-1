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


def time_to_seconds(time_str):
    minutes, seconds = time_str.split(":")
    return int(minutes) * 60 + int(
        seconds
    )  # дополнительная функция для перевода времени в секунды для того, чтобы было удобнее сортировать песни по их продолжительности


def get_by_genre(songs, genre):
    result = []
    genre_lower = genre.lower()
    for song in songs:
        if song[2].lower() == genre_lower:
            result.append(song)
    return result


def get_by_artist(songs, artist):
    result = []
    artist_lower = artist.lower()
    for song in songs:
        if song[1].lower() == artist_lower:
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
    text_lower = text.lower()
    for song in songs:
        if text_lower in song[0].lower():
            result.append(song)
    return result


def top_longest(songs, n):
    sorted_songs = sorted(
        songs, key=lambda song: time_to_seconds(song[3]), reverse=True
    )
    return sorted_songs[:n]


print("Инди:", [s[0] for s in get_by_genre(SONGS, "indie")])
print("Metallica:", [s[0] for s in get_by_artist(SONGS, "Metallica")])
print("Исполнители:", unique_artists(SONGS))
print("Поиск 'Numb':", [s[0] for s in search_title(SONGS, "Numb")])
print("Топ-3:", [s[0] for s in top_longest(SONGS, 3)])
