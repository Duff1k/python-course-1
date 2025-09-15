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

# Первая функция
def get_by_genre(songs, genre):
    return [song[0] for song in songs if song[2].lower() == genre.lower()]

# Вывод
print("Песни жанра 'pop':", get_by_genre(SONGS, "PoP"))

# Вторая функция
def get_by_artist(songs, artist):
    return [song[0] for song in songs if song[1].lower() == artist.lower()]

# Вывод
print("Песни исполнителя 'Billie_Eilish':", get_by_artist(SONGS, "BillIE Eilish"))

# Третья функция
def unique_artists(songs):
    unique_artists_list = []
    for song in songs:
        artist = song[1]
        if artist not in unique_artists_list:
            unique_artists_list.append(artist)
    return unique_artists_list

# Вывод
print("Уникальные исполнители в порядке первого появления:", unique_artists(SONGS))

# Четвертая функция
def search_title(songs, text):
    return [song[0] for song in songs if text.lower() in song[0].lower()]

# Вывод
print("Песни, в названии которых встречается 'you':", search_title(SONGS, "you"))

# Пятая функция
def top_longest(songs, n):
    def to_seconds(duration):
        minutes, seconds = map(int, duration.split(':'))
        time = minutes * 60 + seconds
        return time
    sorted_songs = sorted(songs, key=lambda song: to_seconds(song[3]), reverse=True)
    return sorted_songs[:n]

# Вывод
print("Топ-5 самых длинных песен:")
for i, song in enumerate(top_longest(SONGS, 5), 1):
    print(f"{i} - {song[0]}, {song[3]}")
