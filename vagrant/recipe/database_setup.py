import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    name = Column(String(20), nullable = False)
    email = Column(String(20), nullable = False)
    picture = Column(String(250))

class Recipe(Base):
    __tablename__ = 'recipe'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    recipePicture = Column(String(250))
    description = Column(String(250))        
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return{
            'name': self.name,
            'id' : self.id,
            'recipePicture' : self.recipePicture,
            'description' : self.description,
         }

class Ingredients(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key = True)
    recipe_id = Column(Integer, ForeignKey('recipe.id'))
    recipe = relationship(Recipe)
    ingredientName = Column(String(250))
    ingredientType = Column(String(250))


    @property
    def serialize(self):
        return{
            'ingredientName' : self.ingredientName,
            'ingredientNote' : self.ingredientNote,
            'ingredientType' : self.ingredientType,
        }
# Database for Recipe steps       
class RecipeSteps(Base):
    __tablename__ = "recipesteps"

    id = Column(Integer, primary_key = True)
    recipestep = Column(String(250))
    recipe_id = Column(Integer, ForeignKey('recipe.id'))
    recipe = relationship(Recipe)

class RecipeCard(Base):
    __tablename__ = 'recipeCard'

    id = Column(Integer, primary_key = True)
    category = Column(String(250))
    rating = Column(String(8))
    recipe_id = Column(Integer, ForeignKey('recipe.id'))
    recipe = relationship(Recipe)
    ingredients_id = Column(Integer, ForeignKey('ingredients.id'))
    ingredient = relationship(Ingredients)
    receipesteps_id = Column(Integer, ForeignKey('recipesteps.id'))
    recipesteps = relationship(RecipeSteps)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return{
            'category': self.category,
            'id' : self.id,
            'rating' : self.raiting,
        }


engine = create_engine('sqlite:///recipe.db')
Base.metadata.create_all(engine)
    