# Import media file and fresh_tomatoes file
import media
import fresh_tomatoes

# Call movie class to create an instance containing movie information
the_foreigner = media.Movie("The Foreigner",
                            "Old man Jackie kicks butt.",
                            "https://www.independent.ie/"
                            "incoming/article35858198.ece/"
                            "BINARY/foreigner%20poster.jpeg",
                            "https://www.youtube.com/watch?v=33iuQu3UtjI")
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/"
                        "en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://cdn.traileraddict.com/content/"
                     "20th-century-fox/avatar-6.jpg",
                     "http://www.youtube.com/water?v=-9ceBgWV8io")
hot_fuzz = media.Movie("Hot Fuzz",
                       "British cop battles the greater good.",
                       "https://images-na.ssl-images-amazon.com/"
                       "images/I/51%2BA3tXtUHL._SY450_.jpg",
                       "http://www.youtube.com/watch?v=ayTnvVpj9t4")
jackass = media.Movie("Jackass",
                      "Jackasses do jackass moves.",
                      "https://images-na.ssl-images-amazon.com/"
                      "images/I/513CXRu8biL._SY355_.jpg",
                      "https://www.youtube.com/watch?v=KwFZkLucUb0")
kundo = media.Movie("Kundo",
                    "A medieval western style action movie.",
                    "https://static1.tribute.ca/poster/540x800/kundo-5724.jpg",
                    "https://www.youtube.com/watch?v=NKq34E4y36o")
# Store movie information in a list to be used in fresh_tomatoes
movies = [the_foreigner, hot_fuzz, kundo, jackass, toy_story, avatar]
# Pass movie information into Webpage class that generates the .html file
fresh_tomatoes.open_movies_page(movies)
