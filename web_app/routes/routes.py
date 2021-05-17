import requests
import json
import os
from dotenv import load_dotenv
from flask import Flask
from flask import Blueprint, request, jsonify, render_template, redirect, flash
from app.movie_finder import get_movie_recommendations

routes = Blueprint("routes", __name__)

@routes.route("/")
def finder():
    return render_template("movie_finder.html")

@routes.route("/genres")
def genres():
    return render_template("genres.html")

@routes.route("/certifications")
def certifications():
    return render_template("certifications.html")

@routes.route("/movie/recommendations", methods=["GET", "POST"])
def movie_recommendations():
    print("Movie Recommendations...")

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    genre = request_data.get("genre") 
    year = request_data.get("year") 
    certification = request_data.get("certification")
    sort = request_data.get("sort") 

    results = get_movie_recommendations(genre=genre, year=year, certification=certification, sort=sort)
    if len(results) == 5:
        flash("Recommendations Generated Successfully!", "success")
        return render_template("movie_recommendations.html", genre=genre, year=year, certification=certification, sort=sort, results=results)
    else:
        flash("Sorry, couldn't find enough movies for those criteria.", "danger")
        return redirect("/")