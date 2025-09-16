data = [
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

def user_choice():
    print('Выберите нужную функцию:\n'
          '1)Вернуть список песен указанного жанра\n'
          '2)Вернуть список песен указанного исполнителя\n'
          '3)Вернуть список уникальных исполнителей в порядке первого появления\n'
          '4)Вернуть песни, в названии которых встречается подстрока text\n'
          '5)Вернуть n самых длинных треков\n'
          )
    try:
        user_input = int(input('Введите номер:'))
    except ValueError:
        print('Ввести надо число 1-5')
        return

    match user_input:
        case 1:
            user_genre = input('Введите жанр:').strip()
            res = get_by_genre(data, user_genre)
            print(res or 'Ничего не найдено')
        case 2:
            user_artist = input('Введите исполнителя:').strip()
            res = get_by_artist(data, user_artist)
            print(res or 'Ничего не найдено')
        case 3:
            res = unique_artists(data)
            print(res or 'Ничего не найдено')
        case 4:
            user_text = input('Введите текст:').strip()
            res = search_title(data, user_text)
            print(res or 'Ничего не найдено')
        case 5:
            try:
                user_num = int(input('Введите число (n): '))
                if user_num <= 0:
                    raise ValueError('n must be > 0')
            except ValueError:
                print('n должно быть целым положительным числом')
                return
            res = top_longest(data, user_num)
            print(res or 'Ничего не найдено')
        case _:
            print('Нет такого пункта')

    pass

def get_by_genre(songs, genre):
    g = genre.casefold()
    genre_list = [song[0] for song in songs if song[2].casefold() == g]
    return genre_list

def get_by_artist(songs, artist):
    a = artist.casefold()
    artist_list = [song[0] for song in songs if song[1].casefold() == a]
    return artist_list

# def unique_artists(songs):
#     unique_artist_list = []
#     for song in songs:
#         if song[1] not in unique_artist_list:
#             unique_artist_list.append(song[1])
#     return unique_artist_list

def unique_artists(songs):
    unique_artist_list = list(dict.fromkeys(song[1] for song in songs))
    return unique_artist_list

def search_title(songs, text):
    t = text.casefold()
    title_list = [song[0] for song in songs if t in song[0].casefold()]
    return title_list

def top_longest(songs, n):
    # sort_list = sorted(songs, key = lambda song: to_seconds(song[3]), reverse = True)
    # result_list = [song[0] for song in sort_list[:n]]
    result_list = [song[0] for song in sorted(songs, key = lambda song: to_seconds(song[3]), reverse = True)[:n]]
    return result_list

def to_seconds(time):
    m, s = map(int, time.split(':'))
    return m*60 + s

def main():
    user_choice()
    pass

main()
