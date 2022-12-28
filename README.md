# IMDb Scraper
This is a Python script that allows you to scrape data from IMDb and save it to a CSV file. It is designed to work with IMDb webpages that display the top 50 movies in a genre sorted by popularity and in detailed mode. This project was inspired by the Week 7 CS50x course where we had to use SQL to get infomation out of a database with top movies and TV shows sources from IMDb. The webscraper aimed to provide a method to collect data reliably and efficiently. 

## Prerequisites
Before running the script, make sure you have the following installed on your computer:

Python 3
The requests library, which is used to send HTTP requests to the website
The bs4 (Beautiful Soup) library, which is used to parse the HTML content of the webpage
## Usage
To use the script, follow these steps:

1. Run the script in a terminal:
2. Copy code: python imdb_scraper.py
3. The script will prompt you to enter a URL to an IMDb webpage. Enter the URL to the IMDb webpage for the top 50 movies in a   genre sorted by popularity and in detailed mode. For example:
4. Copy code: https://www.imdb.com/search/title/?genres=action&start=1&count=50&sort=popularity,desc&view=detailed
5. The script will scrape the data from the webpage and save it to a CSV file called movies.csv in the current directory.
6. The CSV file will contain the following columns:
    - Name: the title of the movie
    - Ranking: the ranking of the movie on the IMDb list
    - Rating: the IMDb rating of the movie
    - Genre: the genre of the movie
    - Release Date: the release date of the movie
    - Description: a brief description of the movie
    - Number of Votes: the number of votes the movie has received on IMDb
## Notes
- The script only works with IMDb webpages that are in the specified format (top 50 movies in a genre sorted by popularity and in detailed mode).
- The script may not work if the webpage structure or class names change.
- The script may not work if the webpage is protected by a login or if it is blocked by a firewall.
- The script includes a validation step to check if the user-provided URL is in a valid format, but it does not check if the URL points to a valid webpage. If the user enters an invalid URL, the script will send a request to the website and may fail with an error.

## Credits
- Harvard University
    - Introduction to Computer Science (CS50x)
    - David Malan (Lecturer)

## License
MIT License

Copyright (c) [2022] [jzhong00]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
