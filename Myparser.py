from html.parser import HTMLParser

class Antara(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
    def handle_starttag(self, tag, attrs):
        if (tag == 'div'):
            if ('class', 'post-content clearfix') in attrs:
                self.active = True
    def handle_data(self, text):
        if self.active:
            print(text)
    def handle_endtag(self, tag):
        if (tag == 'script'):
            self.active = False

class Tempo(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
    def handle_starttag(self, tag, attrs):
        if (tag == 'p'):
            self.active = True
    def handle_data(self, text):
        if self.active:
            print(text)
    def handle_endtag(self, tag):
        if (tag == 'p'):
            self.active = False

class Cnn(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
    def handle_starttag(self, tag, attrs):
        if (tag == 'p'):
            self.active = True
    def handle_data(self, text):
        if self.active:
            print(text)
    def handle_endtag(self, tag):
        if (tag == 'p'):
            self.active = False
