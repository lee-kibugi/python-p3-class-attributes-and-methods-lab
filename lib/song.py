class Song:
     # Class variables to keep track of overall counts and unique genres/artists
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    @classmethod
    def add_song_to_count(cls):
        """Class method to increment the overall song count."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """
        Class method to add a genre to the list of unique genres.
        Also updates the count for each genre.
        """
        if genre not in cls.genres:
            cls.genres.append(genre)
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artists(cls, artist):
        """
        Class method to add an artist to the list of unique artists.
        Also updates the count for each artist.
        """
        if artist not in cls.artists:
            cls.artists.append(artist)
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

    def __init__(self, name, artist, genre):
        """
        Constructor method to initialize a Song instance.
        Increments overall counts and updates genre/artist information.
        """
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
    
