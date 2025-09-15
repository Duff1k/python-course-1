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


def get_by_genre(songs, genre):  # вернуть список песен указанного жанра. Поиск без учёта регистра.
    return [i for i in songs if i[2].lower() == genre.lower()]


def get_by_artist(songs, artist):  # вернуть список песен указанного исполнителя (без учёта регистра).
    return [i for i in songs if i[1].lower() == artist.lower()]


def unique_artists(songs):  # вернуть список уникальных исполнителей в порядке первого появления.
    artists = []
    for i in songs:
        artist = i[1]
        if artist not in artists:
            artists.append(artist)
    return artists


def search_title(songs, text):  # вернуть песни, в названии которых встречается подстрока text (без учёта регистра).
    return [i for i in songs if text.lower() in i[0].lower()]


def top_longest(songs, n):  # вернуть n самых длинных треков (сортировка по длительности).
    songs_with_seconds = []
    for song in songs:
        seconds = int(song[3][:2]) * 60 + int(song[3][3:])
        # print(seconds)
        songs_with_seconds.append((song,
                                   seconds))  # тут получается список из кортежей, в каждом из которых кортеж с песней и длительность песни
    songs_with_seconds.sort(key=lambda i: i[1], reverse=True)
    # print(songs_with_seconds)
    return [i for i, _ in songs_with_seconds[:n]]


print(get_by_genre(songs, 'pop'))
print(get_by_artist(songs, 'the WEEknd'))
print(unique_artists(songs))
print(search_title(songs, 'sm'))
print(top_longest(songs, 5))
