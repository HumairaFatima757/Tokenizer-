from nltk.tokenize import wordpunct_tokenize

# Read the code from the file
filename = r"C:\tokenization.txt"
with open(filename, "r", encoding="utf-8") as file:
    code = file.read()

# Tokenize the code using wordpunct_tokenize
tokens = wordpunct_tokenize(code)

# Initialize an empty string to store the output
output = ""

# Concatenate tokens and their classes into a single string
output += "{:<15} {:}\n".format("Token Part", "Class Part")
is_inside_string = False
for token in tokens:
    if token == '"':
        is_inside_string = not is_inside_string
        token_part = token
        token_class = "String Delimiter"
    elif is_inside_string:
        token_part = token
        token_class = "String Literal"
    elif token.lower() in ["main", "whole", "until", "printf", "return"]:
        token_part = token
        token_class = token
    elif token.isdigit():
        token_part = token
        token_class = "Digit"
    elif token in "+-*/=><;,":
        token_part = token
        token_class = token
    elif token == "(":
        token_part = "( "
        token_class = "( "
    elif token == "++":
        token_part = "++ "
        token_class = "++ "
    elif token == "()":
        token_part = "() "
        token_class = "() "
    elif token == "_i_":
        token_part = "_i_"
        token_class = "id"
    elif token == ")":
        token_part = ") "
        token_class = ") "
    elif token == "{":
        token_part = "{ "
        token_class = "{ "
    elif token == "}":
        token_part = "} "
        token_class = "} "
    else:
        token_part = token
        token_class = type(token).__name__
    
    output += "{:<15} {:}\n".format(token_part, token_class)

# Print the output
print(output.strip())
