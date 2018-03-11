from media import Movie
import fresh_tomatoes


movies_0 = Movie("Howl's Moving Castle", 
                    "Sophie, a young milliner, encounters a wizard named Howl on her way to visit her sister Lettie. Upon returning home, she meets the Witch of the Waste, who transforms her into a ninety-year-old woman.", 
                    "http://78.media.tumblr.com/af666bde26c8bac1db9ae900c3949f64/tumblr_nea5i0zoJ21t7b5qro1_1280.jpg", 
                    "https://www.youtube.com/watch?v=iwROgK94zcM"
                )
movies_1 = Movie("Watchmen", 
                    "Watchmen is set in an alternate reality that closely mirrors the contemporary world of the 1980s. The primary difference is the presence of superheroes. The point of divergence occurs in the year 1938. Their existence in this version of the United States is shown to have dramatically affected and altered the outcomes of real-world events such as the Vietnam War and the presidency of Richard Nixon.", 
                    "https://upload.wikimedia.org/wikipedia/en/a/a2/Watchmen%2C_issue_1.jpg", 
                    "https://www.youtube.com/watch?v=PVjA0y78_EQ"
                )
movies_2 = Movie("Grandma's Boy", 
                    "Grandma's Boy", 
                    "https://upload.wikimedia.org/wikipedia/en/2/26/Grandma%27s_Boy_poster.jpg", 
                    "https://www.youtube.com/watch?v=Bi5CfCHknZs"
                )
movies = [movies_0, movies_1, movies_2]
fresh_tomatoes.open_movies_page(movies)