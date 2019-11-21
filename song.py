import re

class Song():
    """ 
    Create a new song! Use as:
    Song(title="Song_Title", 
    artist="Artist_Name", 
    album="Album_Title", 
    length="xx:yy or xx:yy:zz") 
    """
    
    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.song_length = length    
    
    # Length validation
    @property
    def song_length(self):
        return self._song_length
    
    @song_length.setter
    def song_length(self, l):
        pattern = re.compile(r'^(\d+)(?::([0-5]?\d)(?::([0-5]?\d))?)?$')
        match = pattern.match(l)
        if not match:
            raise ValueError("Invalid input: %s" % l)
        else:
            self._song_length = l

    
    # Override methods
    def __str__(self):
        """ 
        Returns info about the song as string 
        """
        return "%s - %s from %s - %s" % (self.artist, self.title, self.album, self.song_length)
    
    
    def __hash__(self):
        return hash(str(self))
    
    
    def __eq__(self, other):
        return self.__class__ == other.__class__ \
            and self.title == other.title \
            and self.artist == other.artist \
            and self.album == other.album \
            and self.song_length == other.song_length

    
    # Custom methods
    def length(self, hours=False, minutes=False, seconds=False):
        """ 
        Return the length of the song in different format
        length() - for default xx:yy:zz notation
        
        For more specific output use one of the following
        length(seconds=True) - for length in seconds
        length(minutes=True) - for length in minutes
        length(hours=True) - for length in hours 
        
        Please give only one input! Otherwise only the first one
        to match will be shown in the order seconds->minutes->hours
        """
        full_time = list(map(int, self.song_length.split(':')))
        if len(full_time) == 2:
            song_length_hours = 0
            song_length_minutes = full_time[0]
            song_length_seconds = full_time[1]
        else:
            song_length_hours = full_time[0]
            song_length_minutes = full_time[1]
            song_length_seconds = full_time[2]
                
        if seconds == True:
            return (song_length_hours * 3600) \
                + (song_length_minutes * 60) \
                + (song_length_seconds)
        elif minutes == True:
            return (song_length_hours * 60) \
                + (song_length_minutes)
        elif hours == True:
            return song_length_hours
        else:
            return "%s" % self.song_length