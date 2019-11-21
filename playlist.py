import datetime
import random
import json
from song import Song

class Playlist():
    """ Creating playlist out of songs """

    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.song_list = []
        self.current_song = -1
        self.played_songs = []


    # Custom methods
    def add_song(self, song):
        """ Adds a new song to the playlist """
        current_list_length = len(self.song_list)
        self.song_list.append({'id': current_list_length,
                               'artist': song.artist, 
                               'title': song.title, 
                               'album': song.album,
                               'song_length': song.song_length})


    def remove_song(self, song):
        """ 
        Removes the last entry for a given song.
        If it is present multiple times, all older duplicates will remain.
        Multiple execution is needed for multiple deletiong of the same song
        which is present multiple times. 
        """
        remove_song_counter = -1
        remove_song_stop = len(self.song_list) * -1
        
        while remove_song_counter > remove_song_stop:
            if  self.song_list[remove_song_counter]['artist'] == song.artist \
                and self.song_list[remove_song_counter]['title'] == song.title \
                and self.song_list[remove_song_counter]['album'] == song.album \
                and self.song_list[remove_song_counter]['song_length'] == song.song_length:
                deleted_song_id = self.song_list[remove_song_counter]['id']
                self.song_list.pop(remove_song_counter)
                remove_song_counter = remove_song_stop
            remove_song_counter -= 1
        
        # Set the position of the deleted song and last song
        rearrange_start = deleted_song_id
        rearrange_stop = len(self.song_list)
        # Check if it is the last song
        # If YES - no changes
        if rearrange_start == rearrange_stop: 
            pass
        else:
            for i in range(rearrange_start, rearrange_stop):
                self.song_list[i]['id'] = rearrange_start


    def add_songs(self, songs):
        """ Adds a new list of songs to the playlist """
        number_of_new_songs = len(songs)
        current_list_length = len(self.song_list)
        for i in range(number_of_new_songs):
            self.song_list.append({'id': current_list_length,
                                   'artist': songs[i].artist, 
                                   'title': songs[i].title, 
                                   'album': songs[i].album,
                                   'song_length': songs[i].song_length})
        print('log: %i new songs added to the playlist!' % number_of_new_songs)


    def total_length(self):
        # Count the number of iterations needed
        number_of_itterations = range(len(self.song_list))
        
        # Set initial 00:00:00 time
        total_length = datetime.timedelta()
        
        for i in number_of_itterations:
            # Extract the string for the song for this iteration
            current_song_length_string = self.song_list[i]["song_length"]
            
            # If there is no hours set in the string, prepend it as "0:" to the string
            if len(list(map(int, current_song_length_string.split(':')))) == 2:
                current_song_length_string = "0:" + current_song_length_string
                
            # Split the string and convert it to real time using integers
            (h, m, s) = current_song_length_string.split(':')
            current_song_length = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            
            # Add the length of the current song to the total length
            total_length += current_song_length
        
        return "%s" % total_length
    
    
    def artists(self):
        return
    
    
    def next_song(self):
        """ Return the next song in the playlist """
        # If there is no current song, assign the first in the list 
        # or a random one as next song based on shuffle settings
        if self.current_song == -1 and self.shuffle == False:
            self.current_song = 0
            self.played_songs.append(self.current_song)
            
            # Return the string of the new song
            current_song_string = "Next song: %i. %s - %s" % ((self.current_song + 1),
                                                          self.song_list[self.current_song]["artist"],
                                                          self.song_list[self.current_song]["title"])
            return current_song_string
        elif self.current_song == -1 and self.shuffle == True:
            new_next_song_id = random.sample(self.song_list, 1)[0]["id"]
            self.current_song = new_next_song_id
            self.played_songs.append(self.current_song)
            
            # Return the string of the new song
            current_song_string = "Next song: %i. %s - %s" % ((self.current_song + 1),
                                                          self.song_list[self.current_song]["artist"],
                                                          self.song_list[self.current_song]["title"])
            return current_song_string
        
        # If there is already a current song "playing" and
        # Shuffle is False -> pick the next song based on sequence in the list
        # But if Shuffle is true -> pick random song from the list
        if self.shuffle == False:
            self.current_song += 1
            # If reach the end of list and Repeat is True start from beginning
            if self.current_song == len(self.song_list) and self.repeat == True:
                self.played_songs = []
                self.current_song = 0
                self.played_songs.append(self.current_song)
            # If reach the end of list and Repeat is False stop playing
            elif self.current_song == len(self.song_list) and self.repeat == False:
                self.played_songs = []
                self.current_song = -1
                return "stop() - no more songs in list and Repeat=False"
                # a stop() should be implemented here
        elif self.shuffle == True:
            for i in range(len(self.song_list)):
                next_song_id = random.sample(self.song_list, 1)[0]['id']
                if next_song_id not in self.played_songs:
                    self.current_song = next_song_id
                    self.played_songs.append(self.current_song)
                else:
                    if i == (len(self.song_list)-1):
                        if self.repeat == True:
                            # Clear the played songs and start with random song
                            self.played_songs = []
                            self.current_song = random.sample(self.song_list, 1)[0]['id']
                            self.played_songs.append(self.current_song)
                        elif self.repeat == False:
                            self.played_songs = []
                            self.current_song = -1
                            return "stop() - no more songs in list and Repeat=False"
                            # a stop() should be implemented here
        
        # Return the string of the next song
        current_song_string = "Next song: %i. %s - %s" % ((self.current_song + 1),
                                                      self.song_list[self.current_song]["artist"],
                                                      self.song_list[self.current_song]["title"])
        return current_song_string
    
    
    def print_playlist(self):
        table_titles = ["Artist", "Song", "Length"]
        table_artists = []
        table_song_titles = []
        table_song_lengths = []
        
        for dictX in self.song_list:
            for key in dictX:
                if key == "artist": 
                    table_artists.append(dictX[key])
                elif key == "title":
                    table_song_titles.append(dictX[key])
                elif key == "song_length":
                    table_song_lengths.append(dictX[key])
                else:
                    pass
        
        data = [table_titles] + list(zip(table_artists, table_song_titles, table_song_lengths))
        longest_artist_name = max(map(len, table_artists))
        longest_song_title = max(map(len, table_song_titles))
        if longest_artist_name > longest_song_title:
            col_width = longest_artist_name + 1
        else:
            col_width = longest_song_title + 1
        table_output = ''
        
        for i, d in enumerate(data):
            line = '|'.join(str(x).ljust(col_width) for x in d) + '\n'
            table_output += line
            if i == 0:
                table_output += '-' * len(line) + '\n'
    
        return table_output
    
    def save(self):
        """ Save playlist settings and songs list in JSON file """
        playlist_data = []
        playlist_data.append({"name": self.name,
                                "repeat": self.repeat,
                                "shuffle": self.shuffle})
        
        for (song_seq, song_val) in enumerate(self.song_list):
            playlist_data.append(self.song_list[song_seq])
        
        
        
        new_file_name = self.name.replace(" ", "-") + ".json"
        full_path = 'playlist-data/' + new_file_name
        with open(full_path, 'w', encoding='utf-8') as json_write_file:
            json.dump(playlist_data, json_write_file, ensure_ascii=False, indent=4)
        print("log: Playlist successfully saved")
    
    @staticmethod
    def load(playlist_file):
        """ Create playlist and populate songs from JSON file """
        full_path = 'playlist-data/' + playlist_file
        with open(full_path) as json_read_file:
            data = json.load(json_read_file)
            
        new_playlist = Playlist(name=data[0]["name"], 
            repeat=data[0]["repeat"], 
            shuffle=data[0]["shuffle"])
        
        songs_saved_in_the_list = []
        for i in range(1, len(data)):
            songs_saved_in_the_list.append(Song(title=data[i]["title"], 
                                                artist=data[i]["artist"],
                                                album=data[i]["album"],
                                                length=data[i]["song_length"]))
        
        new_playlist.add_songs(songs_saved_in_the_list)
        
        return new_playlist