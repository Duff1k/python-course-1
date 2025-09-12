# Домашнее задание 1 (Кудимова А.В., студента группы М25-Ш01)
В файле task_one.py выполненное задание в виде функций. В файле test_file.py те же функции, но с тестовыми выводами.

## Задание ВИШ МИФИ Музыка 🎵🎵🎵
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
## 🗓 Срок сдачи и система баллов

| Баллы | Дедлайн                           |
|-------|-----------------------------------|
| **10 баллов** | до **15.09 числа** (включительно) |
| **5 баллов**  | до **18.09 числа** (включительно) |
| **0 баллов**  | после 18.09 числа                 |
