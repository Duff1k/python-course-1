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
 
def to_seconds(mmss):
   
    parts = mmss.split(":")      
    minutes = int(parts[0])      
    seconds = int(parts[1])      
    total = minutes * 60 + seconds
    return total                
 
 

def get_by_genre(songs, genre):

    need = genre.lower()  
    result = []           
    for song in songs:
        song_genre = song[2]           
        if song_genre.lower() == need: 
            result.append(song)
    return result

def get_by_artist(songs, artist):

    need = artist.lower()
    result = []
    for song in songs:
        song_artist = song[1]
        if song_artist.lower() == need:
            result.append(song)
    return result
 
 
def unique_artists(songs):

    seen = set()     
    result = []      
    for song in songs:
        artist = song[1]
        if artist not in seen:
            result.append(artist)
            seen.add(artist)
    return result
 
 
def search_title(songs, text):

    need = text.lower()
    result = []
    for song in songs:
        title_lower = song[0].lower()
        if need in title_lower:
            result.append(song)
    return result
 
 

def top_longest(songs, n):
 

    if n <= 0:
        return []
 

    sorted_by_len = sorted(songs, key=lambda s: to_seconds(s[3]), reverse=True)
    return sorted_by_len[:n]
 
 

if __name__ == "__main__":
  
    print("get_by_genre(POP):")
    print(get_by_genre(SONGS, "POP"))
    print()
 
 
    print("get_by_artist(billie eilish):")
    print(get_by_artist(SONGS, "billie eilish"))
    print()
 
 
    print("unique_artists:")
    print(unique_artists(SONGS))
    print()
 

    print("search_title('love'):")
    print(search_title(SONGS, "love"))
    print()
 
    print("top_longest(n=5):")
    print(top_longest(SONGS, 5))