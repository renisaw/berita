from html.parser import HTMLParser

class Antara(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
        self.skip = False
        self.br_printed = False
    def handle_starttag(self, tag, attrs):
        if (tag == 'div'):
            if ('class', 'post-content clearfix') in attrs:
                self.active = True
            elif ('class', 'quote_old') in attrs:
                self.skip = True
        elif (tag == 'span') and ('class', 'baca-juga') in attrs:
            self.skip = True
    def handle_data(self, text):
        if self.active and (not self.skip):
            print(text, end='')
            self.br_printed = False
    def handle_endtag(self, tag):
        if self.active and self.skip and (tag == 'div'):
            self.skip = False
        elif self.active and self.skip and (tag == 'span'):
            self.skip = False
        elif (tag == 'script'):
            self.active = False
    def handle_startendtag(self, tag, attrs):
        # handling annoying overused <br> in antara
        if (tag == 'br') and self.active and (not self.skip):
            if not self.br_printed:
                print('', end='')
                self.br_printed = True

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
