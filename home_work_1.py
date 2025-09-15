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

def duration_to_seconds(d: str) -> int:
    m, s = map(int, d.split(":"))
    return m * 60 + s

def get_by_genre(songs, genre):
    return [s for s in songs if s[2].lower() == genre.lower()]

def get_by_artist(songs, artist):
    return [s for s in songs if s[1].lower() == artist.lower()]

def unique_artists(songs):
    seen = set()
    result = []
    for _, artist, _, _ in songs:
        if artist not in seen:
            seen.add(artist)
            result.append(artist)
    return result

def search_title(songs, text):
    return [s for s in songs if text.lower() in s[0].lower()]

def top_longest(songs, n):
    return sorted(songs, key=lambda s: duration_to_seconds(s[3]), reverse=True)[:n]

print(get_by_genre(SONGS, "pop"))

print(get_by_artist(SONGS, "Billie Eilish"))

print(unique_artists(SONGS))

print(search_title(SONGS, "love"))

print(top_longest(SONGS, 3))