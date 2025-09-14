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
    for song in songs:
        artist = song[1]
        if artist not in seen:
            seen.add(artist)
            result.append(artist)
    return result

def search_title(songs, text):
    text_lower = text.lower()
    return [song for song in songs if text_lower in song[0].lower()]

def duration_to_seconds(duration_mmss):
    mm, ss = map(int, duration_mmss.split(":"))
    return mm * 60 + ss

def top_longest(songs, n):
    sorted_songs = sorted(songs, key=lambda song: duration_to_seconds(song[3]), reverse=True)
    return sorted_songs[:n]

def print_songs(songs, title="Результат"):
    print(f"\n=== {title} ===")
    if not songs:
        print("Песни не найдены")
        return
    for i, song in enumerate(songs, 1):
        print(f"{i}. {song[0]} - {song[1]} ({song[2]}) [{song[3]}]")

def main():
    while True:
        print(" "*50)
        print("1. Найти песни по жанру")
        print("2. Найти песни по исполнителю")
        print("3. Показать всех уникальных исполнителей")
        print("4. Поиск по названию песни")
        print("5. Топ самых длинных треков")
        print("6. Показать все песни")
        print("7. Выход")
        print(" "*50)

        choice = input("Выберите действие (1-7): ").strip()

        if choice == '1':
            genre = input("Введите жанр: ").strip()
            if genre:
                found = get_by_genre(SONGS, genre)
                print_songs(found, f"Песни жанра '{genre}'")
            else:
                print("Жанр не может быть пустым")

        elif choice == '2':
            artist = input("Введите имя исполнителя: ").strip()
            if artist:
                found = get_by_artist(SONGS, artist)
                print_songs(found, f"Песни исполнителя '{artist}'")
            else:
                print("Имя исполнителя не может быть пустым")

        elif choice == '3':
            artists = unique_artists(SONGS)
            print(f"\n=== Уникальные исполнители ({len(artists)}) ===")
            for i, artist in enumerate(artists, 1):
                print(f"{i}. {artist}")

        elif choice == '4':
            text = input("Введите текст для поиска в названии: ").strip()
            if text:
                found = search_title(SONGS, text)
                print_songs(found, f"Песни с '{text}' в названии")
            else:
                print("Текст для поиска не может быть пустым")

        elif choice == '5':
            try:
                n = int(input("Сколько самых длинных треков показать? ").strip())
                if n > 0:
                    longest = top_longest(SONGS, n)
                    print_songs(longest, f"Топ {n} самых длинных треков")
                else:
                    print("Введите число больше 0")
            except ValueError:
                print("Введите корректное число")

        elif choice == '6':
            print_songs(SONGS, "Все песни в библиотеке")

        elif choice == '7':
            print("\nДо свидания! Спасибо за использование музыкальной библиотеки!")
            break

        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 7.")

if __name__ == "__main__":
    # Запускаем меню
    main()