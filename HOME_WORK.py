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
    genre_lower = genre.lower()
    for song in songs:
        if song[2].lower() == genre_lower:
            result.append(song)
    result.sort()
    return result


def get_by_artist(songs, artist):
    result = []
    artist_lower = artist.lower()
    for song in songs:
        if song[1].lower() == artist_lower:
            result.append(song)
    result.sort()
    return result


def unique_artists(songs):
    artists = []
    for song in songs:
        if song[1] not in artists:
            artists.append(song[1])
    artists.sort()
    return artists


def search_title(songs, text):
    result = []
    text_lower = text.lower()
    for song in songs:
        if text_lower in song[0].lower():
            result.append(song)
    return result


def top_longest(songs, n):
    return sorted(songs, key=lambda s: int(s[3][:2])*60 + int(s[3][3:]), reverse=True)[:n]


test_genre = "pop"
test_artist = "Daft Punk"
test_search_text = "Like"
test_n = 5

# Задание№1: Вернуть список песен указанного жанра.
print(f"\nСписок песен в жанре - '{test_genre}':")
genre_songs = get_by_genre(SONGS, test_genre)
for i, song in enumerate(genre_songs, 1):
    print(f"{i}. {song[0]} - {song[1]} ({song[3]})")

# Задание№2: Вернуть список песен указанного исполнителя.
print(f"\nСписок песен исполнителя - '{test_artist}':")
artist_songs = get_by_artist(SONGS, test_artist)
for i, song in enumerate(artist_songs, 1):
    print(f"{i}. {song[0]} - {song[3]}")

# Задание№3: Вернуть список уникальных исполнителей
print(f"\nСписок исполнителей:")
artists = unique_artists(SONGS)
for i, artist in enumerate(artists, 1):
    print(f"{i}. {artist}")

# Задание№4: Вернуть песни, в названии которых встречается текст
print(f"\nСписок, в названии которых есть - '{test_search_text}':")
found_text = search_title(SONGS, test_search_text)
for i, song in enumerate(found_text, 1):
    print(f"{i}. {song[0]} - {song[1]}")

# Задание№5: Вернуть n самых длинных треков (сортировка по длительности)
print(f"\n{test_n} Сортировка по продолжительности песни:")
longest_songs = top_longest(SONGS, test_n)
for i, song in enumerate(longest_songs, 1):
    print(f"{i}. {song[0]} - {song[1]} - {song[3]}")