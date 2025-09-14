def get_by_genre(songs, genre):
    result = []
    genre_lower = genre.lower()
    for song in songs:
        if song[2].lower() == genre_lower:
            result.append(song)
    return result

def get_by_artist(songs, artist):
    result = []
    artist_lower = artist.lower()
    for song in songs:
        if song[1].lower() == artist_lower:
            result.append(song)
    return result

def unique_artists(songs):
    artists = []
    for song in songs:
        if song[1] not in artists:
            artists.append(song[1])
    return artists

def search_title(songs, text):
    result = []
    text_lower = text.lower()
    for song in songs:
        if text_lower in song[0].lower():
            result.append(song)
    return result

def convert_to_seconds(time_mmss):
    minutes, seconds = map(int, time_mmss.split(':'))
    return minutes * 60 + seconds

def top_longest(songs, n):
    songs_with_seconds = []
    for song in songs:
        title, artist, genre, duration = song
        seconds = convert_to_seconds(duration)
        songs_with_seconds.append((song, seconds))
        
    sorted_songs = sorted(songs_with_seconds, key=lambda x: x[1], reverse=True)
    
    return [song[0] for song in sorted_songs[:n]]

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

test_genre = "indie"           
test_artist = "The Weeknd"   
test_search_text = "ever"    
test_top_n = 5               
print("=== ТЕСТИРОВАНИЕ ФУНКЦИЙ ===")
    
print(f"\n1. Песни в жанре '{test_genre}':")
genre_songs = get_by_genre(SONGS, test_genre)
for song in genre_songs:
    print(f"   {song[0]} - {song[1]} ({song[3]})")
    
print(f"\n2. Песни исполнителя '{test_artist}':")
artist_songs = get_by_artist(SONGS, test_artist)
for song in artist_songs:
    print(f"   {song[0]} - {song[3]}")
    
print(f"\n3. Уникальные исполнители (в порядке первого появления):")
artists = unique_artists(SONGS)
for i, artist in enumerate(artists, 1):
    print(f"   {i}. {artist}")
    
print(f"\n4. Поиск по названию '{test_search_text}':")
found_songs = search_title(SONGS, test_search_text)
for song in found_songs:
    print(f"   {song[0]} - {song[1]}")
    
print(f"\n5. Топ-{test_top_n} самых длинных песен:")
longest_songs = top_longest(SONGS, test_top_n)
for i, song in enumerate(longest_songs, 1):
    print(f"   {i}. {song[0]} - {song[1]} - {song[3]}")