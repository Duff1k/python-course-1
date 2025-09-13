# Домашнее задание 1
## ВИШ МИФИ Музыка 🎵🎵🎵
Дан список песен. Каждая песня — кортеж вида:
`(title, artist, genre, duration_mmss)`

Нужно реализовать функции:
1. `get_by_genre(songs, genre)` — вернуть **список песен** указанного жанра. Поиск **без учёта регистра**.
2. `get_by_artist(songs, artist)` — вернуть **список песен** указанного исполнителя (без учёта регистра).
3. `unique_artists(songs)` — вернуть **список уникальных исполнителей** в порядке первого появления.
4. `search_title(songs, text)` — вернуть песни, в названии которых встречается подстрока `text` (без учёта регистра).
5. *Челлендж:* `top_longest(songs, n)` — вернуть **n** самых длинных треков (сортировка по длительности).  

## Входные данные

```python
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
```
# Решение
1. get_by_genre(songs, genre) — вернуть список песен указанного жанра. Поиск без учёта регистра.
```python
def get_by_genre(songs, genre):
    result = []  

    for song in songs:  
        song_genre = song[2]  
       
        if song_genre.lower() == genre.lower():
            result.append(song)  
    
    return result  
print(get_by_genre(SONGS, "pop"))
```

2. get_by_artist(songs, artist) — вернуть список песен указанного исполнителя (без учёта регистра).
```python
def get_by_artist(songs, artist):
    result = []  

    for song in songs: 
        song_artist = song[1]  

        if song_artist.lower() == artist.lower():
            result.append(song) 

    return result 
print(get_by_artist(SONGS, "BILLIE EILISH"))

3. unique_artists(songs) — вернуть список уникальных исполнителей в порядке первого появления.
```python
def unique_artists(songs):
    result = []           
    seen = []             

    for song in songs:    
        artist = song[1]  

        if artist not in seen:
            result.append(artist)
            seen.append(artist)

    return result 
print(unique_artists(SONGS))
```

4. search_title(songs, text) — вернуть песни, в названии которых встречается подстрока text (без учёта регистра).
```python
def search_title(songs, text):
    result = []  

    for song in songs:           
        title = song[0]         
        
        title_lower = title.lower()
        text_lower = text.lower()

        if text_lower in title_lower:
            result.append(song)  

    return result 
print(search_title(SONGS, "Know"))
```

5. Челлендж: top_longest(songs, n) — вернуть n самых длинных треков (сортировка по длительности).

```python
def top_longest(songs, n):
    def to_seconds(duration_str):
        mm, ss = map(int, duration_str.split(':'))
        return mm * 60 + ss

    sorted_songs = sorted(songs, key=lambda song: to_seconds(song[3]), reverse=True)

    return sorted_songs[:n]
print(top_longest(SONGS, 3))
```
