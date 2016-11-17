from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Recipe, Base, RecipeCard, User, Ingredients, RecipeSteps
engine = create_engine('sqlite:///recipe.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

User1 = User(name ="Jason Morrissette", email="Porkins1@Live.com",)
#Card for Bacon Explosion   
recipe1 = Recipe(user_id=1, name = "Bacon Explosion", 
                recipePicture = "http://tipsforbbq.com/Include/Images/Recipes/BaconExplosionRevisited/BaconExplosionSlicedw.jpg",)
session.add(recipe1)
session.commit()


recipeCard1 = RecipeCard(user_id = 1, category = "Dinner",
                         rating = "5/5", recipe = recipe1 )

session.add(recipeCard1)
session.commit()

ingreidents1 = Ingredients(ingredientName = "Pork", recipe = recipe1)
session.add(ingreidents1)
session.commit()

ingreidents2 = Ingredients(ingredientName = " Lots of Bacon", recipe = recipe1)
session.add(ingreidents2)
session.commit()

ingreidents3 = Ingredients(ingredientName = " Exploding Cheese", recipe = recipe1)
session.add(ingreidents3)
session.commit()

recipestep1 = RecipeSteps(recipestep = "Mix Ground Pork in a bowl", recipe = recipe1)
session.add(recipestep1)
session.commit()

recipestep2= RecipeSteps(recipestep = "form pork into sausage", recipe = recipe1)
session.add(recipestep2)
session.commit()

recipestep3= RecipeSteps(recipestep = "Wrap sausage with bacon", recipe = recipe1)
session.add(recipestep3)
session.commit()

recipestep4= RecipeSteps(recipestep = "place on smoker for 12 hours", recipe = recipe1)
session.add(recipestep4)
session.commit()

recipestep5= RecipeSteps(recipestep = "Enjoy", recipe = recipe1)
session.add(recipestep5)
session.commit()


recipe2 = Recipe(user_id= 1, name = "Deep Fried Mac and Cheese Balls", 
                 recipePicture="http://www.thecupcaketheory.com/wp-content/uploads/2011/10/deep_fried_mac_and_cheese.jpg")
session.add(recipe2)
session.commit()

recipe3 = Recipe(user_id = 1, name = "BBQ Pork ",
                 recipePicture = "http://recipingo.com/wp-content/uploads/2014/02/Slow-Cookers-BBQ-Pulled-Pork-Recipe.jpg")
session.add(recipe3)
session.commit()

recipe4 = Recipe(user_id =1,name = "Seafood Chowder",
                 recipePicture = "http://cookdiary.net/wp-content/uploads/images/Seafood-Chowder_18564.jpg")
session.add(recipe4)
session.commit()

print "added Recipes!"