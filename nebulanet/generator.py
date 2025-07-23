import svgwrite
import random
from .utils import random_opacity

class NebulaNet:
    def __init__(self, width, height, style: dict):
        self.width = width
        self.height = height
        self.style = style
        self.dwg = svgwrite.Drawing(size=(width, height), profile='tiny')
        self.points = []

    def generate_points(self, num_points):
        self.points = [
            (random.randint(0, self.width),
             random.randint(0, self.height),
             random.randint(self.style['min_point_size'], self.style['max_point_size']))
            for _ in range(num_points)
        ]

    def draw_background(self):
        self.dwg.add(self.dwg.rect(insert=(0, 0), size=(self.width, self.height), fill=self.style['background_color']))

    def draw_lines(self):
        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):
                x1, y1, _ = self.points[i]
                x2, y2, _ = self.points[j]
                distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
                if distance < self.style['line_threshold']:
                    self.dwg.add(self.dwg.line(start=(x1, y1), end=(x2, y2),
                                               stroke=self.style['line_color'],
                                               stroke_width=0.5,
                                               opacity=random_opacity()))

    def draw_points(self):
        for x, y, size in self.points:
            self.dwg.add(self.dwg.circle(center=(x, y), r=size,
                                         fill=self.style['point_color'],
                                         opacity=random_opacity()))

    def add_particles(self, num_particles=200):
        for _ in range(num_particles):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(1, 4)
            self.dwg.add(self.dwg.circle(center=(x, y), r=size, fill=self.style['line_color']))

    def generate(self, output_file, num_points=200, num_particles=200):
        self.generate_points(num_points)
        self.draw_background()
        self.draw_lines()
        self.draw_points()
        self.add_particles(num_particles)
        self.dwg.saveas(output_file)