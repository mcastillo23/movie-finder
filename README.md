# MovieFinder

Web application that allows users to specify movie criteria in order to get a list of recommendations based on user preferences.  

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/mcastillo23/movie-finder) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd movie-finder
```

Use Anaconda to create and activate a new virtual environment, perhaps called "moviefinder-env":

```sh
conda create -n movie-finder-env python=3.8
conda activate movie-finder-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above)

## Setup

This application issues requests to The Movie Database (TMDb) API in order to provide movie data and recommendations. In order to get an API key, an account in The Movie Database is required. Sign up for an account [here](https://www.themoviedb.org/signup).

Then, take a moment to [obtain an AlphaVantage API Key](https://www.themoviedb.org/settings/api).

There are [instructions and screenshots](https://developers.themoviedb.org/3/getting-started/introduction) on how to obtain the API key if necessary. 

After obtaining an API key, in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your API Key. 

     ALPHAVANTAGE_API_KEY="abc123"

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [.gitignore](/.gitignore) file)

## Usage

Run the get movie script:

```sh
python -m app.movie_finder
```

### Web app

```sh
# mac:
FLASK_APP=web_app flask run

# windows:
export FLASK_APP=web_app
flask run
```

## [License](/LICENSE.md)