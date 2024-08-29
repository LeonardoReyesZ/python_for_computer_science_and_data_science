# ex_8.22: Cooking with healthier ingredients
import re

# ~~~~~~~~~  Definition of Functions   ~~~~~  ~~~~~~~   ~~ ~~~~ ~~~~~~ ~~~~~~~~~~~~ ~~~~~~~~~~ ~~~~ ~~~~~ ~~~~~~~~~~ ~ #
def convert_to_float( number ):
    """Convert a string number to float."""
    if '/' in number:   # handle fractions
        numerator, denominator = number.split('/')
        return float(numerator) / float(denominator)

    return float(number) # handle decimals and whole numbers
# end convert_to_float()

def update_quantity( match, multiplier ):
    """Update the quantity of the ingredient replacement."""
    # quantity of the healthy ingredient
    default_quantity = convert_to_float(match.group())

    # update the quantity of the healthy ingredient according to the one in the recipe
    return str(default_quantity * multiplier)
# end update_quantity()

def get_healthier_substitute( match ):
    """Look for healthier substitutes for ingredients in a recipe.
       group(1) -> quantity, group(2) -> unit if any, group(3) -> ingredient"""
    quantity = convert_to_float(match.group(1))
    #unit = match.group(2) # useless by the moment
    ingredient = match.group(3)

    # healthier substitutes for a specific ingredient
    replacements = ''.join( healthier_replacements[ingredient].values() )

    # substitute the quantity of the healthy ingredient according to the one in the recipe
    quantity_pattern = re.compile(r'\d+/\d+|\d+\.\d+|\d+') # for each quantity
    healthier_ingredient = re.sub(quantity_pattern, lambda m: update_quantity(m,quantity), replacements)

    return healthier_ingredient
# end parse_recip()


# ~~~~~~~~~  Dictionaries      ~~~~~~~~~~~~   ~~~~~~~   ~~ ~~~~ ~~~~~~ ~~~~~~~~~~~~ ~~~~~~~~~~ ~~~~ ~~~~~ ~~~~~~~~~~ ~ #
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


# ~~~~~~~~~  Program Execution  ~~~~   ~~~~~  ~~~~~~~   ~~ ~~~~ ~~~~~~ ~~~~~~~~~~~~ ~~~~~~~~~~ ~~~~ ~~~~~ ~~~~~~~~~~ ~ #
recipe_sample = '1 cup milk, 4 cup sugar, 1/2 cup sour cream,7.5 cup mayonnaise, 3 egg, 4 cup oil,1 teaspoon lemon juice'

# group(1) -> quantity, group(2) -> unit if any, group(3) -> ingredient
pattern = re.compile(r'(\d+|\d+\.\d+|\d+/\d+)\s*(\w+)?\s+(.+)')

# Process each ingredient and gather healthier substitutes
healthier_substitutes = "\n\n".join(
    get_healthier_substitute(pattern.match(ingredient.strip()))
    for ingredient in recipe_sample.split(',')
)

# print the results
print( f"Original recipe:\n{recipe_sample}\n")
print( f"Healthier recipe:\n{healthier_substitutes}")