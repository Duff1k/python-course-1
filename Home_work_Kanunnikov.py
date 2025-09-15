# Домашнее задание 1. Нужно реализовать функции:
# 1. `get_by_genre(songs, genre)` — вернуть **список песен** указанного жанра. Поиск **без учёта регистра**.
# 2. `get_by_artist(songs, artist)` — вернуть **список песен** указанного исполнителя (без учёта регистра).
# 3. `unique_artists(songs)` — вернуть **список уникальных исполнителей** в порядке первого появления.
# 4. `search_title(songs, text)` — вернуть песни, в названии которых встречается подстрока `text` (без учёта регистра).
# 5. *Челлендж:* `top_longest(songs, n)` — вернуть **n** самых длинных треков (сортировка по длительности).  
# Дан список песен. Каждая песня — кортеж вида:
# `(title, artist, genre, duration_mmss)`

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
    finka_1 = []
    for el in songs:
        if el[2].lower() == genre.lower():
            finka_1.append(el[0])
    return finka_1


def get_by_artist(songs, artist):
    finka_2 = []
    for el in songs:
        if el[1].lower() == artist.lower():
            finka_2.append(el[0])
    return finka_2

def unique_artists(songs):
    finka_3 = []
    for el in songs:
        if el[1] not in finka_3:
            finka_3.append(el[1])
    return finka_3


def search_title(songs, text):
    finka_4 = []
    for el in songs:
        if text.lower() in el[0].lower():
            finka_4.append(el[0])
    return finka_4

def top_longest(songs, n):
    song_second_time = []
    finka_5 = []
    for el in songs:
        minute, second = el[3].split(':')
        total = int(minute) * 60 + int(second)
        song_second_time.append(el + (total,))
    sorted_songs = sorted(song_second_time, key=lambda x: x[4], reverse=True)
    for i in range(n):
        finka_5.append(sorted_songs[i][0])
    return finka_5

# Пример входных данных и работа функций:
genre = 'pop'
artist = 'THE WEekNd'
text = 'ME'
n = 5

print(f'Список песен жанра {genre}:')
print(get_by_genre(SONGS, genre))
print(f'Список песен исполнителя {artist}:')
print(get_by_artist(SONGS, artist))
print('Список уникальных исполнителей:')
print(unique_artists(SONGS))
print(f'Список песен, в названии которых встречается: {text}:')
print(search_title(SONGS, text))
print(f'Топ {n} самых длинных треков:')
print(top_longest(SONGS, n))