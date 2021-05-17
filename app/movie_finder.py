import requests
import json
import os
from dotenv import load_dotenv

#genres list
genres = [
    {"id":28, "genre": "action"},
    {"id":16, "genre": "animated"},
    {"id":99, "genre": "documentary"},
    {"id":18, "genre": "drama"},
    {"id":10751, "genre": "family"},
    {"id":14, "genre": "fantasy"},
    {"id":36, "genre": "history"},
    {"id":35, "genre": "comedy"},
    {"id":10752, "genre": "war"},
    {"id":80, "genre": "crime"},
    {"id":10402, "genre": "music"},
    {"id":9648, "genre": "mystery"},
    {"id":10749, "genre": "romance"},
    {"id":878, "genre": "sci fi"},
    {"id":27, "genre": "horror"},
    {"id":10770, "genre": "TV movie"},
    {"id":53, "genre": "thriller"},
    {"id":37, "genre": "western"},
    {"id":12, "genre": "adventure"},
]

#API key
load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

features = []

#Movie Criteria User Inputs
   
valid_genres = [item["genre"] for item in genres]
valid_certifications = ["G", "PG-13", "R", "NC-17", "NR", "PG"]
   
genre = input("Would you like to search by genre? (Yes or No)")

if genre.upper() == "YES":
    selected_genre = input("Which genre would you like to search by? (ie. Drama)")
    if selected_genre.lower() not in valid_genres:
        print("Hey, are you sure that the genre is correct? Please try again!")
        exit()
    else:
        for item in genres:
            if selected_genre.lower() == item["genre"]:
                features.append("&with_genres=" + str(item["id"]))
elif genre.upper() == "NO":
    features.append("")
else:
    print("Please enter a valid response and try again. (Yes or No)")
    exit()
   
year = input("Would you like to search by year? (Yes or No)")
   
if year.upper() == "YES":
    selected_year = int(input("Which year would you like to search by? (1900-2021)"))
    if selected_year < 1900 or selected_year > 2021:
        print("Hey, are you sure that the year is correct? Please try again!")
        exit()
    else:
        features.append("&primary_release_year=" + str(selected_year))
elif year.upper() == "NO":
    features.append("")
else:
    print("Please enter a valid response and try again. (Yes or No)")
    exit()
   
   
certification = input("Would you like to search by certification? (Yes or No)")
   
if certification.upper() == "YES":
    selected_certification = input("Which certification would you like to search by? (G, PG-13, R, NC-17, NR, PG)")
    if selected_certification.upper() not in valid_certifications:
        print("Hey, are you sure that the certification is correct? Please try again!")
        exit()
    else:
        features.append("&certification_country=US&certification.lte=" + str(selected_certification.upper()))
elif certification.upper() == "NO":
    features.append("")
else:
    print("Please enter a valid response and try again. (Yes or No)")
    exit()
   
#Movie Sorting User Inputs
   
valid_sorts = ["popularity", "revenue", "rating"]
   
sort = input("How would you like to sort your movie results? (Popularity, Revenue, or Rating)")
   
if sort.lower() not in valid_sorts:
        print("Hey, are you sure that the sorting criteria is correct? Please try again!")
        exit()
elif sort.lower() == valid_sorts[0]:
    features.append("&sort_by=popularity.desc")
elif sort.lower() == valid_sorts[1]:
    features.append("&sort_by=revenue.desc")
elif sort.lower() == valid_sorts[2]:
    features.append("&sort_by=vote_average.desc")

#API request

request_url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}{features[0]}{features[1]}{features[2]}{features[3]}" 

response = requests.get(request_url)
   
parsed_response = json.loads(response.text)
