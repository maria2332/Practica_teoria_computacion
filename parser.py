from html.parser import HTMLParser

class HTMLBalanceChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.unbalanced = False
        self.void_tags = {'br', 'img', 'meta', 'input', 'hr', 'link', 'area'}

    def handle_starttag(self, tag, attrs):
        if tag not in self.void_tags:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1] != tag:
            self.unbalanced = True
        else:
            self.stack.pop()

    def is_balanced(self):
        return not self.stack and not self.unbalanced
