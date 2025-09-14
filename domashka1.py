def get_by_genre(songs, genre):
    """Вернуть список песен указанного жанра (без учёта регистра)"""
    genre_lower = genre.lower()
    return [song for song in songs if song[2].lower() == genre_lower]

def get_by_artist(songs, artist):
    """Вернуть список песен указанного исполнителя (без учёта регистра)"""
    artist_lower = artist.lower()
    return [song for song in songs if song[1].lower() == artist_lower]

def unique_artists(songs):
    """Вернуть список уникальных исполнителей в порядке первого появления"""
    seen = set()
    result = []
    for song in songs:
        artist = song[1]
        if artist not in seen:
            seen.add(artist)
            result.append(artist)
    return result

def search_title(songs, text):
    """Вернуть песни, в названии которых встречается подстрока text (без учёта регистра)"""
    text_lower = text.lower()
    return [song for song in songs if text_lower in song[0].lower()]
# Тестовые данные
songs = [
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

# Примеры вызовов функций
print("Рок песни:", get_by_genre(songs, "rock"))
print("Песни Michael Jackson:", get_by_artist(songs, "michael jackson"))
print("Уникальные исполнители:", unique_artists(songs))
print("Поиск по 'child':", search_title(songs, "child"))
