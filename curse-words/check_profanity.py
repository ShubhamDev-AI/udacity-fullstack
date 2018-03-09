


def read_text():
    quotes_file = open(".\\movie_quotes.txt")
    quotes = quotes_file.read()
    print quotes
    quotes_file.close()

read_text()