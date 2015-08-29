import media
import fresh_tomatoes

# Store data for each movie
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "https://goo.gl/zvLQkw",
                        "https://youtu.be/KYz2wyBy3kc",
                        "Tom Hanks")

interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole \
                           to save humanity",
                           "http://goo.gl/uDW6ii",
                           "https://youtu.be/zSWdZVtXT7E",
                           "Matthew McConaughey")

inception = media.Movie("Inception",
                        "Dreams, ideas, and cool special effects",
                        "http://goo.gl/rYyKwt",
                        "https://goo.gl/c3KKam",
                        "Leonardo Decaprio")

the_big_lebowski = media.Movie("The Big Lebowski",
                               '"The Dude" Lebowski, enlists his bowling \
                               buddies to help get restitution for his rug.',
                               "http://goo.gl/8izb9Z",
                               "https://youtu.be/cd-go0oBF4Y",
                               "Jeff Bridges")

# Set movies array.
movies = [toy_story, interstellar, inception, the_big_lebowski]

# Generate movies webpage
fresh_tomatoes.open_movies_page(movies)
