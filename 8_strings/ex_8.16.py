# ex_8.16: Locating URLs
# For this exercise, assume that a valid URL has the form "http://www.domain_name.extension"
# where extension must be two or more characters
import re

# text sample
text_sample = """
Check out the following websites: http://www.example.com, http://www.test.org,
and http://www.invalid-url. Also, http://www.site.co.uk and http://www.fakewebsite.fakelongextension.
"""

# regular expression pattern for matching URLs
url_pattern = r'http://www\.\w+\.\w{2,}'

# find URLs in the text
urls = re.findall(url_pattern, text_sample)

# print results
for url in urls:
    print( url )
