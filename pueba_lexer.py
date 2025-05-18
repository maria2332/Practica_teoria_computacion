from lexer import lexer

html = '''
<a href="http://example.com">Link</a>
<img src="http://example.com/image.png" />
'''

lexer.input(html)

for tok in lexer:
    print(f"{tok.type}: {tok.value}")
