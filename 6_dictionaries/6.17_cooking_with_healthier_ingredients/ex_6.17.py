""" Script to find and recommend healthy ingredients for a specific recipe.
    Ingredients are stored in dictionaries """

import re


# ~~~~~~~  Definition of Functions   ~~~~~ ~~~~~~ ~~~~~~~ ~~~~~~~~~ ~~~~~~~~~~~~~ ~~~~~~~ ~ #
def multiply_numeric_values(string, factor):
    """Multiply the numbers in a string by a factor and return a string with the updated values."""
    pattern = re.compile(r'(\d+/\d+|\d+(\.\d+)?)')

    def replace(match):
        value = match.group(0)
        if '/' in value:
            numerator, denominator = map(int, value.split('/'))
            new_value = factor * numerator / denominator
            return f'{new_value:.1f}' if new_value % 1 != 0 else f'{int(new_value)}'
        else:
            new_value = float(value) * factor
            return f'{new_value:.1f}' if new_value % 1 != 0 else f'{int(new_value)}'

    return pattern.sub(replace, string)

def parse_ingredient(ingredient):
    """Get and return the amount, unit, and ingredient contained in a string."""
    pattern = re.compile(r'([\d/?\d?]+)\s*([a-zA-Z]+)?\s+(.+)')
    match = pattern.match(ingredient)
    return match.groups() if match else (None, None, None)

def find_replacement(recipe):
    """Find healthier ingredients to replace a recipe."""
    for element in recipe:
        amount, unit, ingredient = parse_ingredient(element)
        if ingredient in healthier_replacements:
            replacements = healthier_replacements[ingredient]
            key = f'1 {unit}' if unit else '1'
            if key in replacements:
                new_ingredient = replacements[key]
                replace = multiply_numeric_values(new_ingredient, int(amount))
                print(f'{amount} {unit or ""} {ingredient} -> {replace}', end="\n\n")
            else:
                print(f'No replacement found for {element}')
        else:
            print(f'No replacement found for {element}')


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

# Sample user input and usage
recipe = [
    '1 cup sour cream',
    '7 cup milk',
    '3 teaspoon lemon juice',
    '7 cup sugar',
    '4 cup butter',
    '10 cup flour',
    '2 cup mayonnaise',
    '3 egg',
    '6 cup oil'
]

# ~~~~~~~~~  Program Execution     ~~ ~~~~ ~~~~~~ ~~~~~~~~~~~~ ~~~~~~~~~~ ~~~~ ~~~~~ ~~~~~~~~~~ ~ #
print("Original recipe:")
for ingredient in recipe:
    print(ingredient)

print("\n\nHealthier ingredients for the recipe:")
find_replacement(recipe)
