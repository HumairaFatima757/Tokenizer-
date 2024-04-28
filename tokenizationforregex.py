import re

def custom_tokenizer(code):
    token_specification = [
        (r'whole','WHOLE'),
        ('MAIN', r'main'),
        ('LPAREN', r'\('),
        ('RPAREN', r'\)'),
        ('LBRACE', r'\{'),
        ('RBRACE', r'\}'),
        ('SEMICOLON', r';'),
        ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
        ('DIGIT', r'\d+(\.\d*)?'),
        ('LESS', r'<'),
        ('GREATER', r'>'),
        ('OPERATOR', r'='),
        ('comma', r','),
        ('STRING', r'"[^"]*"'),
        ('PRINTF', r'printf'),
    ]
    tok_regex = '|'.join('(?P<{0}>{1})'.format(*pair) for pair in token_specification)
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == '(':
            kind = value  # Set kind to the value of the '(' character
        yield (kind, value)

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
tokens = list(custom_tokenizer(code))
print("{:<15} {:}".format( "Class Part","Token Part"))
for part, class_ in tokens:
    print(f"{part:<15} {class_}")
