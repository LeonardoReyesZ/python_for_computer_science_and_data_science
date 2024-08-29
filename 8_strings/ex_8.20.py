# ex_8.20: Munging Dates
import re
from datetime import datetime

# Input string containing dates in different formats
text = """
042555
12/25/2022
January 9, 1985
"""

def convert_mmddyy(match):
    """Convert MMDDYY to MM/DD/YYYY"""
    date = match.group(0)
    return datetime.strptime(date, '%m%d%y').strftime('%m/%d/%Y')
# end convert_mmddyy()

def convert_slash_format(match):
    """Convert MM/DD/YYYY to Month Day, Year"""
    date = match.group(0)
    return datetime.strptime(date, '%m/%d/%Y').strftime('%B %d, %Y')
# end convert_slash_format()

def convert_full_date_format(match):
    """Convert Month Day, Year to MMDDYY"""
    date = match.group(0)
    return datetime.strptime(date, '%B %d, %Y').strftime('%m%d%y')
# end convert_full_date_format()


# Regex patterns for the three formats
pattern_mmddyy = r'\b\d{6}\b'                # MMDDYY
pattern_slash_format = r'\b\d{2}/\d{2}/\d{4}\b'  # MM/DD/YYYY
pattern_full_date = r'\b\w+ \d{1,2}, \d{4}\b'  # Month Day, Year

# Perform transformations
# Convert MMDDYY to MM/DD/YYYY
text = re.sub(pattern_mmddyy, convert_mmddyy, text)

# Convert MM/DD/YYYY to Month Day, Year
text = re.sub(pattern_slash_format, convert_slash_format, text)

# Convert Month Day, Year to MMDDYY
text = re.sub(pattern_full_date, convert_full_date_format, text)

print("Munged Dates:")
print(text)
