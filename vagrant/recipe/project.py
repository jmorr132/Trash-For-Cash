from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Recipe, RecipeCard, User, Ingredients

app = Flask(__name__)

from flask import session as login_session
import random, string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError


import httplib2
import json
from flask import make_response
import requests


engine = create_engine('sqlite:///recipe.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/recipe')
def showRecipe():
    recipes = session.query(Recipe).all()
    return render_template('recipe.html', recipes = recipes)

@app.route('/recipe/new')
def newRecipe():
    return "this link allows you to create a new recipe"


@app.route('/recipe/<int:recipe_id>/edit')
def editRecipe(recipe_id):
    return "this link will allow you to edit a recipe"

@app.route('/recipe/<int:recipe_id>/delete')
def deleteRecipe(recipe_id):
    return "this link will allow you to delete a recipe"

@app.route('/recipe/<int:recipe_id>/')
@app.route('/recipe/<int:recipe_id>/card')
def showRecipeCard(recipe_id):
    recipes = session.query(Recipe).all()
    ingredients = session.query(Ingredients).filter_by(recipe_id = recipe_id).all()
    recipesteps = session.query(RecipeSteps).filter_by(recipe_id = recipe_id).all()
    items = session.query(RecipeCard).filter_by(recipe_id=recipe_id).all()
    return render_template('recipeCard.html', items = items , recipe = recipes, ingredients = ingredients, recipesteps = recipesteps)

@app.route('/recipe/<int:recipe_id>/card/new')
def newRecipeCard(recipe_id):
    return  "This Link will allow you to add new recipes"

@app.route('/recipe/<int:recipe_id>/card/<int:card_id>/edit')
def editRecipeCard(recipe_id, card_id):
    return "This Linke will allow you to edit recipes"

@app.route('/recipe/<int:recipe_id>/card/<int:card_id>/delete')
def deleteRecipeCard(recipe_id, card_id):
    return "This Link will allow you to delete recipes"


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)