# Python-Project-Submission--Soumya
# Movie Genre Web Scraper

This Python script is designed to scrape a list of movies based on the genre you specify from the IMDb website. It uses the `requests` library to make HTTP requests, `BeautifulSoup` for parsing HTML content, and `pandas` to create a CSV file with the scraped movie data.

## Usage

1. Make sure you have the required Python libraries installed. You can install them using `pip`:

   
   pip install requests beautifulsoup4 pandas
   

2. Run the script by executing it. You will be prompted to enter a movie genre. The script accepts a variety of genres such as action, adventure, animation, biography, comedy, and more.

3. The script will scrape movie data for the specified genre from IMDb.

4. If successful, the movie data will be saved to a CSV file named `list.csv`.

5. If the specified genre is not valid, the script will prompt the input again as 'enter the valid genre' in loop (while loop) until the valid input is received or if there are issues with the request, the script will provide appropriate error messages.

## Valid Genres

The script accepts the following genres as genre.lower():
- Action
- Adventure
- Animation
- Biography
- Comedy
- Crime
- Documentary
- Drama
- Family
- Fantasy
- Film-Noir
- History
- Horror
- Music
- Musical
- Mystery
- Romance
- Sci-Fi
- Short
- Sport
- Thriller
- War
- Western

## Error Handling

The script handles various error scenarios, such as HTTP errors, connection errors, and timeouts. It provides relevant error messages to help diagnose the issue.

Please ensure that you use this script responsibly and respect the IMDb website's terms of use and robots.txt file.
