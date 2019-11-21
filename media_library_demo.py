from song import Song
from playlist import Playlist

print("Creating songs")
try:
    x = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="1:30:44")
    s = Song(title="Enter Sandman", artist="Metallica", album="None", length="4:34")
    e = Song(title="Master of Puppets", artist="Metallica", album="Master of Puppets", length="3:23")
except ValueError as e:
    print(e)

print("Print songs based on Object attributes:\n")
print(s.title, s.artist, s.album, s.song_length)
print(e.title, e.artist, e.album, e.song_length)
print(x.title, x.artist, x.album, x.song_length)

# Blank space
print("\n---\n")

print("Print songs with str method:\n")
print(str(x))
print(str(e))
print(str(s))

# Blank space
print("\n---\n")

print("Print hash method:\n")
y = x
print(hash(x))
print(hash(y))
print(hash(s))
print(hash(e))

# Blank space
print("\n---\n")

print("Print length in songs in different formats:\n")
print(x.length(), x.length(seconds=True), x.length(minutes=True), x.length(hours=True))
print(e.length(), e.length(seconds=True), e.length(minutes=True), e.length(hours=True))

# Blank space
print("\n---\n")

print("Creating Playlists")
code_songs = Playlist(name="Songs For Coding", repeat=True, shuffle=True)
print(code_songs.name, code_songs.repeat, code_songs.shuffle, code_songs.song_list)

# Blank space
print("\n---\n")

print("Add Song to Playlist")
code_songs.add_song(s)
print(code_songs.name, code_songs.song_list)
code_songs.add_song(e)
code_songs.add_song(x)
print(code_songs.name, code_songs.song_list)

# Blank space
print("\n---\n")

print("Remove Song from Playlist")
print("songs in the playlist before delete: %i" % len(code_songs.song_list))
code_songs.remove_song(e)
print("songs in the playlist after delete: %i" % len(code_songs.song_list))
print(code_songs.name, code_songs.repeat, code_songs.shuffle, code_songs.song_list)

print("Adding again the same song twice and delete it once")
print("songs in the playlist before add: %i" % len(code_songs.song_list))
code_songs.add_song(e)
code_songs.add_song(e)
print("songs in the playlist after add twice: %i" % len(code_songs.song_list))
code_songs.remove_song(e)
print("songs in the playlist after delete once: %i" % len(code_songs.song_list))
print(code_songs.name, code_songs.repeat, code_songs.shuffle, code_songs.song_list)


# Blank space
print("\n---\n")

print("Add List of Songs to Playlist")
new_list_of_songs = []
new_list_of_songs.extend([s, e, x])
print("songs in the playlist before add: %i" % len(code_songs.song_list))
code_songs.add_songs(new_list_of_songs)
print("songs in the playlist after add: %i" % len(code_songs.song_list))
print(code_songs.song_list)

# Blank space
print("\n---\n")

print("Playlist Total Length:")
print(code_songs.total_length(), '-', len(code_songs.song_list), 'songs in the list')
print("Remove one song and try again:")
code_songs.remove_song(e)
print(code_songs.total_length(), '-', len(code_songs.song_list), 'songs in the list')

# Blank space
print("\n---\n")

print("Print Playlist in table format")
print(code_songs.print_playlist())

# Blank space
print("\n---\n")
print(code_songs.shuffle, code_songs.repeat)
print(code_songs.song_list)
print("Ask for next song in the list 1st time with Shuffle")
print(code_songs.next_song())
print("Ask for next song in the list 2nd time with Shuffle")
print(code_songs.next_song())
print("Ask for next song in the list 3rd time with Shuffle")
print(code_songs.next_song())
print("Ask for next song in the list 4th time with Shuffle")
print(code_songs.next_song())
print("Ask for next song in the list 5th time with Shuffle")
print(code_songs.next_song())
print("Ask for next song in the list 6th time with Shuffle")
print(code_songs.next_song())
print("Ask for next song in the list 7th time with Shuffle")
print(code_songs.next_song())
print("Ask for next song in the list 8th time with Shuffle")
print(code_songs.next_song())

# Blank space
print("\n---\n")

print("Creating Playlist without shuffle and repeat")
code_songs_1 = Playlist(name="Code")
print(code_songs_1.shuffle, code_songs_1.repeat)
code_songs_1.add_song(s)
code_songs_1.add_song(e)
code_songs_1.add_song(x)
code_songs_1.add_song(s)
code_songs_1.add_song(e)
code_songs_1.add_song(x)
print(code_songs_1.song_list)
print("Ask for next song in the list 1st time without Shuffle")
print(code_songs_1.next_song())
print("Ask for next song in the list 2nd time without Shuffle")
print(code_songs_1.next_song())
print("Ask for next song in the list 3rd time without Shuffle")
print(code_songs_1.next_song())
print("Ask for next song in the list 4th time without Shuffle")
print(code_songs_1.next_song())
print("Ask for next song in the list 5th time without Shuffle")
print(code_songs_1.next_song())
print("Ask for next song in the list 6th time without Shuffle")
print(code_songs_1.next_song())
print("Ask for next song in the list 7th time without Shuffle")
print(code_songs_1.next_song())

# Blank space
print("\n---\n")
print("Trying to save existing list")
try:
    code_songs.save()
except ValueError as e:
    print(e)

# Blank space
print("\n---\n")
print("Trying to load saved list")
try:
    loaded_list = Playlist.load("Songs-For-Coding.json")
except ValueError as e:
    print(e)

print(loaded_list.name, loaded_list.repeat, loaded_list.shuffle, loaded_list.song_list)
print(loaded_list.print_playlist())