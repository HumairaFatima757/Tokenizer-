from nltk.tokenize import wordpunct_tokenize

# Code snippet
code = """
whole main ( )                                                                                                                                                                               
{ 
    whole _i_ = 0;                                                                                                                                                           
    until(i < 5)                                                                                                                                                                                     
    {                                                                                                                                                                                                                           
        whole _i_ = 102;                                                                                                                                                                                                   
        printf("the value of i =", i );                                                                                                                                                                                      
        _i_++;    
    }                                                                                                                                                                              
    return 0;                                                                                                                                                                                                         
}                                                                                                                                                                                                                                                          
main ()
"""

# Tokenize the code using wordpunct_tokenize
tokens = list(wordpunct_tokenize(code))

# Print tokens in the desired format
print("{:<15} {:}".format("Token Part", "Class Part"))
for token in tokens:
    if token == "whole":
        token_class = "Keyword"
    elif token.isdigit():
        token_class = "Digit"
    elif token in "+-*/=><{}();,":
        token_class = "Operator"
    else:
        token_class = token
    print("{:<15} {:}".format(token, token_class))
