def extraer_urls(html):
    hrefs = []
    srcs = []

    lexer.input(html)

    last_token = ""
    context_tag = None  # <a> o <img>

    for tok in lexer:
        if tok.type == "A_OPEN":
            context_tag = "a"
        elif tok.type == "IMG_OPEN":
            context_tag = "img"

        if last_token == "HREF" and tok.type == "URL" and context_tag == "a":
            hrefs.append(tok.value)
            context_tag = None  # Reset context after capture

        elif last_token == "SRC" and tok.type == "URL" and context_tag == "img":
            srcs.append(tok.value)
            context_tag = None

        if tok.type in ["TAG_CLOSE", "TAG_SLASH_CLOSE"]:
            context_tag = None  # Reset if tag cierra

        last_token = tok.type

    return hrefs, srcs
