#!/usr/bin/python
from simplecv.api import Color, Image
from simplecv.core.drawing.layer import DrawingLayer

img = Image("color.jpg", sample=True)
line_l = DrawingLayer()
a = (20, 20)
b = (20, 100)
c = (100, 100)
d = (100, 20)
line_l.line(a, b, alpha=128, width=5)
line_l.line(b, c, alpha=128)
line_l.line(c, d, antialias=True)
line_l.line(d, a, color=Color.PUCE)
line_l.line(b, d, width=5)
img.add_drawing_layer(line_l)
temp = img.apply_layers()
print "line: %s" % temp.save(temp=True)
img.clear_layers()

lines_l = DrawingLayer()
a = (20, 20)
b = (20, 100)
c = (100, 100)
d = (100, 20)
pts = (a, b, c, d, a)
lines_l.lines(pts, alpha=128)
# translate over and down 10
pts = map(lambda x: ((x[0] + 10), (x[1] + 10)), pts)
lines_l.lines(pts, color=Color.BEIGE, width=10)
#translate over and down 10
pts = map(lambda x: ((x[0] + 10), (x[1] + 10)), pts)
lines_l.lines(pts, antialias=True)
img.add_drawing_layer(lines_l)
temp = img.apply_layers()
print "lines: %s" % temp.save(temp=True)
img.clear_layers()

rect_tr = DrawingLayer()
tr = (150, 50)
wh = (200, 100)
rect_tr.rectangle(tr, wh, color=Color.BLUE)
tr = (170, 70)
rect_tr.rectangle(tr, wh, color=Color.PUCE, width=5)
tr = (190, 90)
rect_tr.rectangle(tr, wh, color=Color.FORESTGREEN, alpha=128, filled=True)
tr = (210, 110)
rect_tr.rectangle(tr, wh, color=Color.GREEN, filled=True)
img.add_drawing_layer(rect_tr)
temp = img.apply_layers()
print "rectTR: %s" % temp.save(temp=True)
img.clear_layers()

rect_c = DrawingLayer()
cxy = (img.width / 2, img.height / 2)
wh = (200, 100)
rect_c.centered_rectangle(cxy, wh, color=Color.BLUE)
wh = (180, 80)
rect_c.centered_rectangle(cxy, wh, color=Color.PUCE, width=5)
wh = (160, 60)
rect_c.centered_rectangle(cxy, wh, color=Color.FORESTGREEN, alpha=128, filled=True)
wh = (140, 40)
rect_c.centered_rectangle(cxy, wh, color=Color.GREEN, filled=True)
img.add_drawing_layer(rect_c)
temp = img.apply_layers()
print "rectC: %s" % temp.save(temp=True)
img.clear_layers()

poly_l = DrawingLayer()
a = (50, img.height - 50)
b = (250, img.height - 50)
c = (150, 50)
pts = (a, b, c)
poly_l.polygon(pts, alpha=128)
pts = map(lambda x: ((x[0] + 10), (x[1] + 10)), pts)
poly_l.polygon(pts, antialias=True, width=3, alpha=210, filled=True, color=Color.LIME)
#translate over and down 10
pts = map(lambda x: ((x[0] + 10), (x[1] + 10)), pts)
poly_l.polygon(pts, color=Color.BEIGE, width=10)
#translate over and down 10
pts = map(lambda x: ((x[0] + 10), (x[1] + 10)), pts)
poly_l.polygon(pts, antialias=True, width=3, alpha=210)
img.add_drawing_layer(poly_l)
temp = img.apply_layers()
print "poly: %s" % temp.save(temp=True)
img.clear_layers()

circle_layer = DrawingLayer()
c = (img.width / 2, img.height / 2)
r = 150
circle_layer.circle(c, r, color=Color.RED, filled=True)
r = 130
circle_layer.circle(c, r, color=Color.ORANGE, alpha=128, filled=True)
r = 110
circle_layer.circle(c, r, color=Color.YELLOW, alpha=128, width=10)
r = 100
circle_layer.circle(c, r, color=Color.GREEN)
r = 90
circle_layer.circle(c, r, color=Color.BLUE, alpha=172)
img.add_drawing_layer(circle_layer)
temp = img.apply_layers()
print "circle: %s" % temp.save(temp=True)
img.clear_layers()

ellipse_layer = DrawingLayer()
cxy = (img.width / 2, img.height / 2)
wh = (200, 100)
ellipse_layer.ellipse(cxy, wh, color=Color.BLUE)
wh = (180, 80)
ellipse_layer.ellipse(cxy, wh, color=Color.PUCE, width=5)
wh = (160, 60)
ellipse_layer.ellipse(cxy, wh, color=Color.FORESTGREEN, alpha=128, filled=True)
wh = (140, 40)
ellipse_layer.ellipse(cxy, wh, color=Color.GREEN, filled=True)
img.add_drawing_layer(ellipse_layer)
temp = img.apply_layers()
print "ellipse: %s" % temp.save(temp=True)
img.clear_layers()

words_layer = DrawingLayer()
words_layer.set_default_color(Color.RED)
pos = (30, 30)
words_layer.set_font_size(30)
words_layer.text("THIS IS BIG", pos)
pos = (50, 50)
words_layer.set_font_size(10)
words_layer.text("THIS IS SMALL", pos)
pos = (70, 70)
words_layer.set_font_size(20)
words_layer.text("THIS IS medium", pos)
pos = (90, 90)
words_layer.set_font_bold(True)
words_layer.text("THIS IS bold", pos)
pos = (110, 110)
words_layer.set_font_italic(True)
words_layer.text("THIS IS italic", pos)
pos = (130, 130)
words_layer.set_font_underline(True)
words_layer.text("THIS IS underline", pos)
words_layer.set_font_bold(False)
words_layer.set_font_italic(False)
words_layer.set_font_underline(False)
pos = (150, 150)
words_layer.text("THIS IS PUCE, YES PUCE", pos, color=Color.PUCE)
pos = (170, 170)
words_layer.text("This is magical text", pos, color=Color.PLUM, alpha=128)
pos = (190, 190)
words_layer.ez_view_text("Can you read this better?", pos)
img.add_drawing_layer(words_layer)
temp = img.apply_layers()
print "words: %s" % temp.save(temp=True)
img.clear_layers()

#Now lets do some layer stuff
img.add_drawing_layer(line_l)
img.add_drawing_layer(circle_layer)
img.add_drawing_layer(words_layer)
temp = img.apply_layers([0, 2])
print "layers: %s" % temp.save(temp=True)
img.clear_layers()