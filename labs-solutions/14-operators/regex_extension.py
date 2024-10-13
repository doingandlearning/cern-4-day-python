import re


# function to check string only contains letters and numbers
def contains_only_characters_and_numbers(string):
    # Returns a match for any characters except those specified
    re_pattern = re.compile(r'[^a-zA-Z0-9]')
    # invert result as we are only interested in chars and numbers
    return not bool(re_pattern.search(string))


print(contains_only_characters_and_numbers('John'))  # True
print(contains_only_characters_and_numbers('!John_Hunt'))  # False
print(contains_only_characters_and_numbers('42'))  # True
print(contains_only_characters_and_numbers('John42'))  # True
print(contains_only_characters_and_numbers('John 42'))  # False

# Function that will extract value held been start and end characters
def extract_values(start_char, end_char, string):
    return re.findall(start_char + r'(.*?)' + end_char, string)


print(extract_values('<', '>', '<John>'))
print(extract_values('<', '>', '<42>'))
print(extract_values('<', '>', '<John 42>'))
print(extract_values('<', '>', 'The <town> was in the <valley>'))
