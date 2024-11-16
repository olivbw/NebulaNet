import svgwrite
import random

# Dimensions of the svg file
WIDTH = 1920
HEIGHT = 1080

# Points and lines parameters
BACKGROUND_COLOR = '#f0f0f0'  
LINE_COLOR = '#888888'  
POINT_COLOR = "#162635"  
NUM_POINTS = 200
MAX_POINT_SIZE = 8   
MIN_POINT_SIZE = 3 
LINE_THRESHOLD = 100  

# We create a svg file
dwg = svgwrite.Drawing('abstract_background.svg', profile='tiny', size=(WIDTH, HEIGHT))

# Random point with given width and height
def generate_point():
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    size = random.randint(MIN_POINT_SIZE, MAX_POINT_SIZE)
    return (x, y, size)

# Random opacity for the draw_points fonction, in order to have various opacity on points
def random_opacity():
    return random.uniform(0.3, 1.0)

# We generate a list of points
points = [generate_point() for num in range(NUM_POINTS)]

# Here we draw the background on the svg picture with given background_color
dwg.add(dwg.rect(insert=(0, 0), size=(WIDTH, HEIGHT), fill=BACKGROUND_COLOR))

# We draw lines bewteen points, using coordinates of each point
def draw_lines():
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1, _ = points[i]
            x2, y2, _ = points[j]
            distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5 
            if distance < LINE_THRESHOLD:
                opacity = random_opacity()
                dwg.add(dwg.line(start=(x1, y1), end=(x2, y2), stroke=LINE_COLOR, stroke_width=0.5, opacity=opacity))

# Draw the points on the svg picture
def draw_points():
    for x, y, size in points:
        opacity = random_opacity()
        dwg.add(dwg.circle(center=(x, y), r=size, fill=POINT_COLOR, opacity=opacity))

# Draw lines and points
draw_lines()
draw_points()

# Finally we add some particles to add texture to the picture
for num in range(200):  
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    size = random.randint(1, 4)  
    dwg.add(dwg.circle(center=(x, y), r=size, fill=LINE_COLOR))

dwg.save()

print("SVG background generated")
