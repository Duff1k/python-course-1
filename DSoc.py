# Домашнее задание 1
# ВИШ МИФИ Музыка 🎵🎵🎵

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
    genre_lower = genre.lower()
    return [song for song in songs if song[2].lower() == genre_lower]


def get_by_artist(songs, artist):
    artist_lower = artist.lower()
    return [song for song in songs if song[1].lower() == artist_lower]


def unique_artists(songs):
    seen = set()
    result = []
    for _, artist, _, _ in songs:
        if artist not in seen:
            seen.add(artist)
            result.append(artist)
    return result


def search_title(songs, text):
    text_lower = text.lower()
    return [song for song in songs if text_lower in song[0].lower()]


def top_longest(songs, n):
    def duration_to_seconds(duration):
        minutes, seconds = map(int, duration.split(":"))
        return minutes * 60 + seconds

    return sorted(songs, key=lambda song: duration_to_seconds(song[3]), reverse=True)[:n]

def print_songs(songs):
    if not songs:
        print("Песен нет.")
        return

    title_len = max(len(song[0]) for song in songs)
    artist_len = max(len(song[1]) for song in songs)
    genre_len = max(len(song[2]) for song in songs)
    duration_len = max(len(song[3]) for song in songs)

    print(
        f"{'Название'.ljust(title_len)} | {'Исполнитель'.ljust(artist_len)} | {'Жанр'.ljust(genre_len)} | {'Длительность'.ljust(duration_len)}")
    print("-" * (title_len + artist_len + genre_len + duration_len + 9))

    for title, artist, genre, duration in songs:
        print(
            f"{title.ljust(title_len)} | {artist.ljust(artist_len)} | {genre.ljust(genre_len)} | {duration.ljust(duration_len)}")


if __name__ == "__main__":
    print("=== Песни жанра 'pop' ===")
    print_songs(get_by_genre(SONGS, "pop"))

    print("\n=== Песни Billie Eilish ===")
    print_songs(get_by_artist(SONGS, "Billie Eilish"))

    print("\n=== Уникальные исполнители ===")
    for artist in unique_artists(SONGS):
        print(artist)

    print("\n=== Песни с 'love' в названии ===")
    print_songs(search_title(SONGS, "love"))

    print("\n=== Топ 3 самых длинных песен ===")
    print_songs(top_longest(SONGS, 3))
