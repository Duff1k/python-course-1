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
    genre_songs=[]
    for song in songs:
        if song[2].lower() == genre.lower():
            genre_songs.append(song[0])
    return genre_songs


def get_by_artist(songs, artist):
    artist_songs=[]
    for song in songs:
        if song[1].lower() == artist.lower():
            artist_songs.append(song[0])
    return artist_songs

def unique_artists(songs):
    unique_songs=[]
    for song in songs:
        if song[1] not in unique_songs:
            unique_songs.append(song[1])
    return unique_songs

def search_title(songs, text):
    tittle_songs=[]
    for song in songs:
        if text.lower() in song[0].lower():
            tittle_songs.append(song[0])
    return tittle_songs

def top_longest(songs, n):
    time_songs=[]
    longest_songs=[]
    for song in songs:
        time_songs.append(song[3])
    time_songs.sort(reverse=True)
    for i in range(0, n):
        for song in songs:
            if time_songs[i] in song[3]:
                longest_songs.append(song)
    return longest_songs

genre = input("Введите жанр: ")
print(get_by_genre(SONGS, genre))

artist = input("Введите артиста: ")
print(get_by_artist(SONGS, artist))

print(unique_artists(SONGS))

text = input("Введите подстроку: ")
print(search_title(SONGS, text))

print(top_longest(SONGS, 5))