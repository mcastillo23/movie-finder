import requests
import json
import os
from dotenv import load_dotenv
from flask import Flask
from flask import Blueprint, request, jsonify, render_template, redirect, flash
from app.movie_finder import get_movie_recommendations

@routes.route("/")
def finder():
    return render_template("movie_finder.html")

@routes.route("/genres")
def genres():
    return render_template("genres.html")

@routes.route("/certifications")
def certifications():
    return render_template("certifications.html")