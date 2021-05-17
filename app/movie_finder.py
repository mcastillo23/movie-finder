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

def get_movie_recommendations (genre, year, certification, sort):
    """
    Fetches movies from the Movies API, for a given genre, year, certification, and sorting criteria.

    Params:
        genre (str) the requested genre, like "action"
        year (str) the requested year, like "2020"
        certification (str) the requested year, like "PG-13"
        sort (str) the requested sorting method, like "popularity"

    Example:
        result = get_movie_recommendations(genre="action", year="2020", certification="PG-13", sort="popularity")

    Returns the movie as a parsed resposne with its attributes such as "original_title" and "release_date".
    """
    features = []

    #inputs
    for item in genres:
        if genre.lower() == item["genre"]:
            features.append("&with_genres=" + str(item["id"]))
    
    if len(features) == 0:
        features.append("")

    features.append("&primary_release_year=" + str(year))

    features.append("&certification_country=US&certification.lte=" + str(certification.upper()))

    valid_sorts = ["popularity", "revenue", "rating"]

    if sort.lower() == valid_sorts[0]:
        features.append("&sort_by=popularity.desc")
    elif sort.lower() == valid_sorts[1]:
        features.append("&sort_by=revenue.desc")
    elif sort.lower() == valid_sorts[2]:
        features.append("&sort_by=vote_average.desc&vote_count.gte=1000")

    #API request            
    request_url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}{features[0]}&with_original_language=en{features[1]}{features[2]}{features[3]}"  

    response = requests.get(request_url)

    parsed_response = json.loads(response.text)

    #output
    if parsed_response["total_results"] < 5:
        return "Sorry, couldn't find enough movies for those criteria."
        exit()

    recommendations = []

    recommendations.append(parsed_response["results"][0])
    recommendations.append(parsed_response["results"][1])
    recommendations.append(parsed_response["results"][2])
    recommendations.append(parsed_response["results"][3])
    recommendations.append(parsed_response["results"][4])

    return recommendations