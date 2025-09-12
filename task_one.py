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


def get_by_genre(songs, genre): #вернуть список песен указанного жанра. Поиск без учёта регистра.
    list_songs_by_genre = []
    if songs == []:
        return "Песен нет("
    else:
        for title_of_song, artist_of_song, genre_of_song, timing_of_song in songs:
            if genre.lower() == genre_of_song.lower():
                list_songs_by_genre.append(title_of_song)

    if list_songs_by_genre == []:
        return "Данного жанра нет в списке("

    return list_songs_by_genre


def get_by_artist(songs, artist): #вернуть список песен указанного исполнителя (без учёта регистра).
    list_songs_by_artist = []
    if songs == []:
        return "Песен нет("
    else:
        for title_of_song, artist_of_song, genre_of_song, timing_of_song in songs:
            if artist.lower() == artist_of_song.lower():
                list_songs_by_artist.append(title_of_song)

    if list_songs_by_artist == []:
        return "Песен этого исполнителя нет в списке("

    return list_songs_by_artist


def unique_artists(songs): #вернуть список уникальных исполнителей в порядке первого появления.
    list_unique_artists = []
    if songs == []:
        return "Песен нет("
    else:
        for title_of_song, artist_of_song, genre_of_song, timing_of_song in songs:
            if artist_of_song in list_unique_artists:
                pass
            else:
                list_unique_artists.append(artist_of_song)

    if list_unique_artists == []:
        return "Песен нет("

    return list_unique_artists


def search_title(songs, text): #вернуть песни, в названии которых встречается подстрока text (без учёта регистра).
    list_songs_by_title = []
    if songs == []:
        return "Песен нет("
    else:
        for title_of_song, artist_of_song, genre_of_song, timing_of_song in songs:
            if text.lower() in title_of_song.lower():
                list_songs_by_title.append(title_of_song)

    if list_songs_by_title == []:
        return "Песен с таким названием нет("
    return list_songs_by_title


def top_longest(songs, n): #вернуть n самых длинных треков (сортировка по длительности).
    list_songs_by_longest = []
    if songs == []:
        return "Песен нет("
    elif n < 0:
        return "Введите корректное чило песен"
    else:
        list_songs_by_longest = sorted(songs, key=lambda x: x[3], reverse=True)

    return list(map(lambda x: x[0], list_songs_by_longest[0:n]))
