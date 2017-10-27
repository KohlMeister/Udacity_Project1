# Import necessary files
import webbrowser


# Creation of movie class
class Movie():
    """ This class stores movie information. It takes no arguments. """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
