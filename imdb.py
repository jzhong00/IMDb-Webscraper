import csv
import requests
from bs4 import BeautifulSoup
import re


# Prints usage
print("Enter a URL to the IMDb website for a TOP 50 genre sorted by popularity and in detailed mode")

# Prompts user for a URL
url = input("Please enter a URL: ")

# Validate the URL using a regular expression
pattern = r"^https?://[^\s/$.?#].[^\s]*$"
if not re.match(pattern, url):
    print("Invalid URL")
else:
    # Send a GET request to the website and retrieve the HTML content
    try:
        response = requests.get(url)
        html = response.text
    except requests.exceptions.RequestException:
        print("Error: Could not send request to the website")

# Make an HTTP GET request to the website
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, "html.parser")


# Find all the div elements with the class "lister-item mode-advanced"
items = soup.find_all("div", {"class" : "lister-item mode-advanced"})

 # Create a CSV file to store the data
with open("movies.csv", "w", newline="") as csv_file:

    # Create a CSV writer object
    writer = csv.writer(csv_file)

    # Write the header row
    writer.writerow(["Name", "Ranking", "Rating", "Genre", "Release Date", "Description", "Number of Votes"])
    

    # Iterate over the list of items
    for item in items:

        # Find the title of the movie
        name = item.h3.a.text.strip()

        # Find the ranking of the movie
        ranking = item.find("span", class_="lister-item-index unbold text-primary").text.strip()
        ranking = ranking.replace(".", "")

        # Find the description of the movie
        genre = item.find("span", class_="genre").text.strip()

        # Find the release date of the movie
        date = item.find("span", class_="lister-item-year text-muted unbold").text.strip()
        # Remove any characters or symbols from the date that are not numbers
        date = ''.join(c for c in date if c.isdigit())
        
        # Find the line where the rating is found in the HTML
        score = soup.find('div', {'class': 'inline-block ratings-imdb-rating', 'name': 'ir'})

        # Extract the value of the data value attribute and make the rating a float
        rating = score['data-value']
        rating = float(rating)


        # Find the number of votes
        number_of_votes = soup.find('span', {'name': 'nv'})

        # Extract the value of the data value attrivute and make the number of votes an integer
        votes = number_of_votes["data-value"]
        votes = int(votes)

        # Write the values scraped into the file
        writer.writerow([name, ranking, rating, genre, date, votes])

# Print to let the user know of the success and name of the file it has been printed to
print("Success!. The file can be found at movies_csv.")
