# задаем кортеж вида: (title, artist, genre, duration_mmss)
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

# Создаем функцию для фильтрации данных по жанру
def get_by_genre(songs, genre):
    output = []
    for song in songs:
        if song[2].upper() == genre.upper():
            output.append(song[0])
    return output

# Создаем функцию для фильтрации данных по артисту
def get_by_artist(songs, artist):
    output = []
    for song in songs:
        if song[1].upper() == artist.upper():
            output.append(song[0])
    return output

# Создаем функцию для фильтрации данных по уникальному артисту
def unique_artists(songs):
    output = []
    for song in songs:
        if not song[1] in output:
            output.append(song[1])
    return output

# Создаем функцию для фильтрации данных по тексту в названии песни
def search_title(songs, text):
    output = []
    for song in songs:
        if text.upper() in song[0].upper():
            output.append(song[0])
    return output

# Создаем функцию для фильтрации данных по длительности треков (n самых длинных)
def top_logest(songs, n):
    output = []
    for song in songs:
        output.append(song[3])
    output.sort(reverse=True)
    return output[:n]

#Выводим все на экрпан
print(get_by_genre(SONGS, "indie"))
print(get_by_artist(SONGS, "Hans Zimmer"))
print(unique_artists(SONGS))
print(search_title(SONGS, "les"))
print(top_logest(SONGS, 3))



