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

#Реализация функций
def get_by_genre(songs, genre):
    needed_songs = []
    for i in songs:
        if i[2].lower() == genre.lower():
           needed_songs.append(i[0])
    return needed_songs


def get_by_artist(songs, artist):
    needed_songs = []
    for i in songs:
        if i[1].lower() == artist.lower():
            needed_songs.append(i[0])
    return needed_songs

def unique_artists(songs):
    needed_artists = []
    for i in songs:
        if i[1] not in needed_artists:
            needed_artists.append(i[1])
    return needed_artists

def search_title(songs, text):
    needed_songs = []
    for i in songs:
        if text.lower() in i[0].lower():
            needed_songs.append(i[0])
    return needed_songs

def top_longest(songs, n):
    songs_second = []
    needed_songs = []
    for i in songs:
        minute, second = i[3].split(':')
        total = int(minute) * 60 + int(second)
        songs_second.append(i + (total,))
    sorted_songs = sorted(songs_second, key=lambda x: x[4], reverse=True)
    for i in range (n):
        needed_songs.append(sorted_songs[i][0])
    return needed_songs

# Примеры работы функций 
print(get_by_genre(SONGS, "indie"))
print(get_by_artist(SONGS, "Dua Lipa"))
print(unique_artists(SONGS))
print(search_title(SONGS, "time"))
print(top_longest(SONGS, 4))