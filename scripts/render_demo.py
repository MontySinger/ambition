"""Build the README illustration with Pillow; no model or network calls.

Install the optional asset dependency with `python -m pip install Pillow`,
then run `python scripts/render_demo.py` from any directory.
Fonts use macOS system files or DejaVu fonts when installed on other systems.
The skill does not run this script or require Pillow.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
WIDTH, HEIGHT, SCALE = 1200, 690, 2
PAPER = "#F7F5EF"
INK = "#252A27"
MUTED = "#686D67"
ORANGE = "#B74725"
RULE = "#D4D6CE"


def font(size, kind="sans"):
    options = {
        "sans": ["/System/Library/Fonts/Supplemental/Arial.ttf", "DejaVuSans.ttf"],
        "bold": ["/System/Library/Fonts/Supplemental/Arial Bold.ttf", "DejaVuSans-Bold.ttf"],
        "serif": ["/System/Library/Fonts/Supplemental/Georgia.ttf", "DejaVuSerif.ttf"],
        "mono": ["/System/Library/Fonts/Menlo.ttc", "DejaVuSansMono.ttf"],
    }
    for candidate in options[kind]:
        try:
            return ImageFont.truetype(candidate, size * SCALE)
        except OSError:
            pass
    raise RuntimeError("Install DejaVu fonts or use a system with the listed macOS fonts.")


def draw_frame(stage):
    image = Image.new("RGB", (WIDTH * SCALE, HEIGHT * SCALE), PAPER)
    draw = ImageDraw.Draw(image)

    def text(x, y, value, size=24, color=INK, kind="sans"):
        face = font(size, kind)
        # Every line is deliberately set, so detect overflow if a font changes.
        box = draw.textbbox((0, 0), value, font=face)
        if x * SCALE + box[2] > (WIDTH - 36) * SCALE:
            raise ValueError(f"Text exceeds canvas: {value}")
        draw.text((x * SCALE, y * SCALE), value, font=face, fill=color)

    def line(points, fill=RULE, width=1):
        draw.line([(x * SCALE, y * SCALE) for x, y in points], fill=fill, width=width * SCALE)

    draw.rectangle((48 * SCALE, 43 * SCALE, 61 * SCALE, 56 * SCALE), fill=ORANGE)
    text(75, 37, "AMBITION", 20, ORANGE, "mono")
    text(916, 39, "A WORKED EXAMPLE", 15, MUTED, "mono")
    text(48, 88, "Give the work a purpose.", 59, kind="serif")
    text(50, 171, "Start with the request you already have.", 24, MUTED)
    line([(48, 224), (1152, 224)])

    text(48, 251, "YOUR ROUGH REQUEST", 16, MUTED, "mono")
    text(48, 295, "Research this", 36, kind="serif")
    text(48, 342, "company.", 36, kind="serif")
    text(48, 435, "$ambition", 23, ORANGE, "mono")
    text(48, 478, "What do you need", 21, MUTED)
    text(48, 509, "the research to help you do?", 21, MUTED)

    line([(397, 267), (397, 566)])
    line([(432, 328), (474, 328)], ORANGE, 2)
    line([(465, 320), (474, 328), (465, 336)], ORANGE, 2)
    text(510, 251, "A STRONGER ASSIGNMENT", 16, MUTED, "mono")

    rows = [
        ("OUTCOME", ["Help me decide whether this company", "is worth pursuing as a customer."]),
        ("METHODS", ["Use evidence about its operations", "to identify a problem we could solve."]),
        ("CHECK", ["Separate facts from hypotheses.", "If the evidence is weak, say so."]),
    ]
    for index, (label, copy) in enumerate(rows):
        y = 292 + index * 96
        visible = index <= stage
        if visible:
            text(510, y, label, 13, ORANGE, "mono")
            for offset, value in enumerate(copy):
                text(510, y + 23 + offset * 30, value, 25)
        else:
            prompts = ["", "Which evidence would help?", "How will you check the result?"]
            text(510, y, label, 13, MUTED, "mono")
            text(510, y + 27, prompts[index], 23, MUTED)

    line([(48, 607), (1152, 607)])
    text(48, 632, "ILLUSTRATIVE EXAMPLE / NOT A LIVE SESSION", 13, MUTED, "mono")
    for index in range(3):
        x = 1052 + index * 36
        line([(x, 644), (x + 22, 644)], ORANGE if index <= stage else RULE, 3)
    return image.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)


def main():
    assets = ROOT / "assets"
    assets.mkdir(exist_ok=True)
    frames = [draw_frame(stage) for stage in range(3)]
    frames[-1].save(assets / "ambition-demo.png", optimize=True)
    # Reuse one palette across frames to keep text and colors stable.
    palette = frames[-1].quantize(colors=128, method=Image.Quantize.MEDIANCUT)
    indexed = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
    indexed[0].save(
        assets / "ambition-demo.gif",
        save_all=True,
        append_images=indexed[1:],
        duration=[3500, 4500, 8000],
        loop=0,
        disposal=2,
        optimize=True,
    )
    for name in ["ambition-demo.gif", "ambition-demo.png"]:
        path = assets / name
        print(f"{path.relative_to(ROOT)}: {path.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
