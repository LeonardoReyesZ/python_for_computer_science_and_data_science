""" Script to map potential healthy ingredients for a specific recipe.
    Ingredients are stored in dictionaries """

# ~~~~~~~~~  Dictionaries         ~~ ~~~~ ~~~~~~ ~~~~~~~~~~~~ ~~~~~~~~~~ ~~~~ ~~~~~ ~~~~~~~~~~ ~ #
healthier_replacements = {
    'sour cream': {
        '1 cup': '1 cup yogurt'
    },
    'milk': {
        '1 cup': '1/2 cup evaporated milk and 1/2 cup water\nor 1 cup soy milk'
    },
    'lemon juice': {
        '1 teaspoon': '1/2 teaspoon vinegar'
    },
    'sugar': {
        '1 cup': '1/2 cup honey\nor 1 cup molasses\nor 1/4 cup agave nectar'
    },
    'butter': {
        '1 cup': '1 cup margarine\nor 1 cup yogurt'
    },
    'flour': {
        '1 cup': '1 cup rye flour\nor 1 cup rice flour'
    },
    'mayonnaise': {
        '1 cup': '1 cup cottage cheese\nor 1/8 cup mayonnaise and 7/8 cup yogurt'
    },
    'egg': {
        '1': '2 tablespoons cornstarch\nor 2 tablespoons arrowroot flour\n'
             'or 2 tablespoons potato starch\nor 2 egg whites\nor 1/2 of a large banana (mashed)'
    },
    'oil': {
        '1 cup': '1 cup applesauce'
    }
}

# list of ingredients with default values
ingredients = ['milk', 'oil', 'egg']

# map potential replacements for default values
for ingredient in ingredients:
    print( f"Potential healthier replacement for {ingredient}:\n"
           f"{healthier_replacements[ingredient]}\n" )
