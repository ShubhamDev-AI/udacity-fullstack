
import urllib

def read_text():
    quotes_file = open(".\\movie_quotes.txt")
    quotes = quotes_file.read()
    print quotes
    quotes_file.close()
    return quotes

def check_profanity(text):
    conn = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
    output = conn.read()
    # print(output)
    conn.close()
    if "true" in output:
        print("PROFANITY DETECTED!!!")
    elif "false" in output:
        print("Text is clean!")
    else:
        print("Oops! Could not check for profanity.")

check_profanity(read_text())