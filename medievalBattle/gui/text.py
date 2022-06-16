class Text:
    def __init__(self, window, text, x, y, font, color):
        self.window = window
        self.text = text
        self.textColor = color
        self.textFont = font
        self.x = x
        self.y = y

    def show(self):
        txt = self.textFont.render(self.text, True, self.textColor)
        txtX = self.x - (txt.get_width() / 2)
        txtY = self.y - (txt.get_height() / 4 * 3)
        self.window.blit(txt, (txtX, txtY))

    def changeText(self, text):
        self.text = text
