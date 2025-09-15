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
    genre = genre.lower()
    return [song for song in songs if song[2].lower() == genre]

def get_by_artist(songs, artist):
    artist = artist.lower()
    return [song for song in songs if song[1].lower() == artist]

def unique_artists(songs):
    seen = set()
    unique = []
    for song in songs:
        artist = song[1]
        if artist not in seen:
            seen.add(artist)
            unique.append(artist)
    return unique

def search_title(songs, text):
    text = text.lower()
    return [song for song in songs if text in song[0].lower()]

def top_longest(songs, n):
    def duration_to_seconds(duration):
        mm, ss = map(int, duration.split(':'))
        return mm * 60 + ss

    sorted_songs = sorted(songs, key=lambda x: duration_to_seconds(x[3]), reverse=True)
    return sorted_songs[:n]

genre = input("Введите жанр для поиска: ")
print("Песни жанра:", genre, ":", get_by_genre(SONGS, genre))

artist = input("Введите исполнителя для поиска: ")
print("Песни исполнителя:", artist, ":", get_by_artist(SONGS, artist))

print("Уникальные исполнители:", unique_artists(SONGS))

text = input("Введите текст для поиска в названиях песен: ")
print("Песни с", text, "в названии:", search_title(SONGS, text))

n = int(input("Сколько самых длинных треков показать?" ))
print("Топ -",n,"треков по длинне:", top_longest(SONGS, n))