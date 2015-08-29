import webbrowser


class Movie():
    """ This class provides a way to store movie related data and functions """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube, movie_actor):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.actor = movie_actor

    def showtrailer(self):
        webbrowser.open(self.trailer_youtube_url)
