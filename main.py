import requests
from bs4 import BeautifulSoup
from pandas import DataFrame



def scrape_movies():
    try:

        response = requests.get(f"https://www.imdb.com/search/title/?genres={genre}&explore=genres&title_type=movie&ref_=ft_movie_0")

    #if response.status_code == 200:

        soup = BeautifulSoup(response.content, "html.parser")
        movies = []


        for movie in soup.findAll('h3', attrs={'class': 'lister-item-header'}):
           title = movie.a.text

           movies.append({
               "Title": title,
               "genre": genre.lower()
           })
        return movies


    except requests.exceptions.HTTPError as err1:
        print("Http Error:", err1)

    except requests.exceptions.ConnectionError as err2:
        print("Error Connecting:", err2)

    except requests.exceptions.Timeout as err3:
        print("Timeout Error:", err3)

    except requests.exceptions.RequestException as err4:
        print("Unknown error", err4)
        #(f"Failed to fetch data. Status code: {response.status_code}")


# if __name__ == "__main__":
while True:
    genre = input("what genre movie do you want to watch:\n")

    if genre.lower() in {"action", "adventure", "animation", "biography", "comedy", "crime", "documentary",
                             "drama", "family", "fantasy", "film-noir", "history", "horror", "music", "musical",
                             "mystery", "romance", "sci-fi", "short", "sport", "thriller", "war", "western"}:
        movies = scrape_movies()

        if movies:
            df = DataFrame(movies)
            df.to_csv("list.csv",index= False)
            print("Top 50 movies saved to list.csv")

        else:
            print("Try again")
        exit()
    else:
        print("enter the valid genre")




