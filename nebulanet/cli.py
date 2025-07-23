import argparse
from nebulanet.generator import NebulaNet
from nebulanet.styles import PREDEFINED_STYLES
from nebulanet.config_loader import load_style_from_json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--style', help='Name of the predifined style, or path to json style file.')
    parser.add_argument('--output', default='output.svg', help='Output files name.')
    args = parser.parse_args()

    style = PREDEFINED_STYLES.get(args.style)
    if not style:
        try:
            style = load_style_from_json(args.style)
        except Exception as e:
            print(f"Error while loading style: {e}")
            return

    nn = NebulaNet(width=1920, height=1080, style=style)
    nn.generate(args.output)
    print(f"SVG generated at {args.output}")

if __name__ == "__main__":
    main()