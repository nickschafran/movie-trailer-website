import media
import fresh_tomatoes

# Movie Instances:
end_of_the_tour = media.Movie(
    "The End of the Tour",
    "In 1996, immediately after the publication of one his best known and\
    hugely successful novels, Infinite Jest, David Foster Wallace goes on\
    a five day touring interview with Rolling Stone reporter and writer\
    David Lipsky",
    "http://ia.media-imdb.com/images/M/MV5BMTUwODU3NjQxNF5BMl5BanBnXkFtZTgwODE2NTE4NTE@._V1__SX687_SY726_.jpg",
    "https://www.youtube.com/watch?v=DBk1Mrb4RyM")

love_and_mercy = media.Movie(
    "Love & Mercy",
    "In the 1960s, Beach Boys leader Brian Wilson struggles with emerging \
    psychosis as he attempts to craft his avant-garde pop masterpiece. \
    In the 1980s, he is a broken, confused man under the 24-hour watch of \
    shady therapist Dr. Eugene Landy.",
    "http://ia.media-imdb.com/images/M/MV5BMTk1MTkwMzU4Nl5BMl5BanBnXkFtZTgwNjY0MDE1NTE@._V1__SX687_SY726_.jpg",
    "https://www.youtube.com/watch?v=lioWzrpCtGQ")

steve_jobs = media.Movie(
    "Steve Jobs",
    "Set backstage at three iconic product launches and ending in 1998 with\
    the unveiling of the iMac, Steve Jobs takes us behind the scenes of the\
    digital revolution to paint an intimate portrait of the brilliant man at\
    its epicenter.",
    "http://ia.media-imdb.com/images/M/MV5BMTUyNjc0NDkxM15BMl5BanBnXkFtZTgwOTc1OTI3NTE@._V1__SX687_SY726_.jpg",
    "https://www.youtube.com/watch?v=IeOxo7o9T8Q")

the_walk = media.Movie(
    "The Walk",
    "The story of French high-wire artist Philippe Petit's attempt to cross\
    the Twin Towers of the World Trade Center in 1974.",
    "http://ia.media-imdb.com/images/M/MV5BMTU5MDgyNDgzM15BMl5BanBnXkFtZTgwNDA1MjI0NTE@._V1__SX687_SY726_.jpg",
    "https://www.youtube.com/watch?v=rBicCZG4vg0")

straight_outta_compton = media.Movie(
    "Straight Outta Compton",
    "The group NWA emerges from the streets of Compton, California in the\
    mid-1980s and revolutionizes pop culture with their music and tales\
    about life in the hood.",
    "http://ia.media-imdb.com/images/M/MV5BMTA5MzkyMzIxNjJeQTJeQWpwZ15BbWU4MDU0MDk0OTUx._V1__SX687_SY726_.jpg",
    "https://www.youtube.com/watch?v=l5r5cZk0EfY",)

the_martian = media.Movie(
    "The Martian",
    "During a manned mission to Mars, Astronaut Mark Watney is presumed \
    dead after a fierce storm and left behind by his crew. With only meager\
    supplies, he must draw upon his ingenuity, wit and spirit to subsist and\
    find a way to signal to Earth that he is alive.",
    "http://ia.media-imdb.com/images/M/MV5BMTcwMjI2NzM2MF5BMl5BanBnXkFtZTgwNDkyNTI5NTE@._V1__SX687_SY726_.jpg",
    "https://www.youtube.com/watch?v=lQqhfq87FgY")

# List of Movies
movies = [end_of_the_tour, love_and_mercy, steve_jobs, the_walk,
          straight_outta_compton, the_martian]

# Generate and open html
fresh_tomatoes.open_movies_page(movies)
