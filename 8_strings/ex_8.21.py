# ex_8.21: Metric Conversions
import re

# Define conversion factors
conversion_factors = {
    ('meters', 'inches'): 39.3701,
    ('meters', 'feet'): 3.28084,
    ('centimeters', 'inches'): 0.393701,
    ('inches', 'centimeters'): 2.54,
    ('feet', 'meters'): 0.3048,

    ('liters', 'quarts'): 1.05669,
    ('quarts', 'liters'): 0.946353,

    ('kilograms', 'pounds'): 2.20462,
    ('ounces','grams'): 28.3495,
    ('pounds', 'kilograms'): 0.453592,
}

# regular expression to parse the question
pattern = re.compile(r'how many (\w+) are in (\d+(?:\.\d+)?) (\w+)\?', re.IGNORECASE)


def convert_units( question ):
    """Convert units to English metric"""
    match = pattern.match(question)
    if not match:
        print( "Invalid question format." )

    target_unit = match.group(1).lower()
    value = float(match.group(2))
    source_unit = match.group(3).lower()

    # check if conversion is valid
    if (source_unit, target_unit) in conversion_factors:
        conversion_factor = conversion_factors[(source_unit, target_unit)]
        converted_value = value * conversion_factor
        return f"{value} {source_unit}  is approximately {converted_value:.2f} {target_unit}."

    else:
        return f"Cannot convert {source_unit} to {target_unit}."
# end convert_units()


# test conversions
questions = [
    "How many inches are in 2 meters?",
    "How many liters are in 10 quarts?",
    "How many feet are in 5 kilograms?",
    "How many grams are in 3 ounces?"
]

for question in questions:
    print( convert_units(question) )
