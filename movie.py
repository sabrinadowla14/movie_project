import webbrowser


class Movie():

    """ This class provides a way to store movie related information
        function initinitialize or createsspace in memory
        for the new instance or object. It is also called a constructure. """

    # When constant make all capital VALID_RATINGS

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):

        # create instance variable

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Instance method

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
