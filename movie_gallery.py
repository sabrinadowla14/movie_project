import fresh_tomatoes
import movie

""" Contents are taken from instructors notes and also
from you tuble websitesmovie. Movie() called the init
function inside the Movie class which is in movie file.
Create a new instance such as anger_management. """

anger_management = movie.Movie(
    "Anger Management",
    "One of the most hilarious motion picture comedy scenes ever",
    "https://upload.wikimedia.org/wikipedia/en/6/6c/Anger_management_poster.jpg",
    "https: //www.youtube.com/watch?v=9LZ35Ar3r2k"
)

titanic = movie.Movie(
    "Titanic",
    "Titanic is a 1997 American epic romance film.",
    "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
    "https://www.youtube.com/watch?v=2e-eXJ6HgkQ"
)

heart_of_the_sea = movie.Movie(
    "In the Heart of the Sea",
    "The film is about humankind's collective, slowly dawning\
     realization that whales are not big fish but intelligent mammals",
    "https://upload.wikimedia.org/wikipedia/en/8/8b/In_the_Heart_of_the_Sea_poster.jpg",
    "https://www.youtube.com/watch?v=b_n2CAhgPiA"
)

boss_baby = movie.Movie(
    "Boss Baby",
    "Hilariously universal story about how \
    a new baby's arrival impacts a family!",
    "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Boss_Baby_poster.jpg",
    "https://www.youtube.com/watch?v=O2Bsw3lrhvs"
)

despicable_me = movie.Movie(
    "Despicable Me",
    "Gru And The Girls Are Back! ",
    "https://upload.wikimedia.org/wikipedia/en/d/db/Despicable_Me_Poster.jpg",
    "https://www.youtube.com/watch?v=ej6dxNrh3Dc")

beauty_and_the_beast = movie.Movie(
    "Beauty and the Beast",
    "American animated musical romantic fantasy film.",
    "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg",
    "https://www.youtube.com/watch?v=OvW_L8sTu5E")

# creating list of movies

movies = [
    anger_management,
    titanic,
    heart_of_the_sea,
    boss_baby, despicable_me,
    beauty_and_the_beast
]

fresh_tomatoes.open_movies_page(movies)
