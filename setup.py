from setuptools import setup, find_packages

setup(
    name='NebulaNet',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['svgwrite'],
    entry_points={
    'console_scripts': [
        'nebulanet=nebulanet.cli:main',
    ],
    },
    author='Olivier Bouët-Willaumez',
    description='SVG background generator inspired by constellations',
    license='MIT',
)