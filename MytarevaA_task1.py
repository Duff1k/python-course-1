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


def convert_to_seconds(time_mmss):
    """Вспомогательная функция для конвертации времени в секунды"""
    minutes, seconds = map(int, time_mmss.split(':'))
    return minutes * 60 + seconds


def top_longest(songs, n):
    """Вернуть n самых длинных треков (сортировка по длительности)"""
    # Создаем копию списка с добавлением времени в секундах
    songs_with_seconds = [(song, convert_to_seconds(song[3])) for song in songs]

    # Сортируем по длительности (по убыванию)
    sorted_songs = sorted(songs_with_seconds, key=lambda x: x[1], reverse=True)

    # Возвращаем n самых длинных песен (только оригинальные кортежи)
    return [song[0] for song in sorted_songs[:n]]


# Тестирование функций
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

# Примеры использования:
if __name__ == "__main__":
    print("Песни в жанре 'rock':")
    for song in get_by_genre(SONGS, "rock"):
        print(f"  {song[0]} - {song[1]}")

    print("\nПесни Arctic Monkeys:")
    for song in get_by_artist(SONGS, "Arctic Monkeys"):
        print(f"  {song[0]}")

    print("\nУникальные исполнители:")
    print(unique_artists(SONGS))

    print("\nПоиск по названию 'ever':")
    for song in search_title(SONGS, "ever"):
        print(f"  {song[0]} - {song[1]}")

    print("\nТоп-5 самых длинных песен:")
    for i, song in enumerate(top_longest(SONGS, 5), 1):
        print(f"  {i}. {song[0]} - {song[1]} ({song[3]})")