def parse_html(html):
    hrefs = []
    srcs = []

    lexer.input(html)
    last_tag = None
    last_token = None

    for tok in lexer:
        if tok.type == 'TAG_NAME':
            last_tag = tok.value.lower()

        elif last_token == 'HREF' and tok.type == 'URL' and last_tag == 'a':
            hrefs.append(tok.value)

        elif last_token == 'SRC' and tok.type == 'URL' and last_tag == 'img':
            srcs.append(tok.value)

        elif tok.value in ['>', '/>']:
            last_tag = None  # se cierra la etiqueta

        last_token = tok.type

    return hrefs, srcs
