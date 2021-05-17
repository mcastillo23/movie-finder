import os
import pytest

from app.movie_finder import get_movie_recommendations

CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server")
def test_movie_recommendations():
    # with valid movies, returns the movie name and release date:
    results = get_movie_recommendations(genre="action", year="2020", certification="PG-13", sort="popularity")
    assert len(results) == 5
    movie = results[0]
    assert movie["original_title"] == "Monster Hunter"
    assert movie["release_date"] == "2020-12-03"

    # with invalid movies, fails gracefully:
    invalid_results = get_movie_recommendations(genre="action", year="2090", certification="PG-13", sort="popularity")
    assert invalid_results == "Sorry, couldn't find enough movies for those criteria."
