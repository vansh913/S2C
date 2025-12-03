from PIL import Image, ImageDraw, ImageFont
import textwrap

# Use default PIL font; for project, you can add a manga font and use ImageFont.truetype

def draw_speech_bubble(img: Image.Image, text: str, pos=(20, 20), max_chars=28):
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    lines = textwrap.wrap(text, width=max_chars)
    line_h = font.getbbox('A')[3] - font.getbbox('A')[1]  # Use getbbox for height
    padding = 8
    text_w = max(font.getbbox(line)[2] - font.getbbox(line)[0] for line in lines)  # Use getbbox for width
    box_w = text_w + padding * 2
    box_h = line_h * len(lines) + padding * 2
    x, y = pos
    # draw white rounded rectangle
    draw.rectangle([x, y, x + box_w, y + box_h], fill='white', outline='black')
    ty = y + padding
    for line in lines:
        draw.text((x + padding, ty), line, fill='black', font=font)
        ty += line_h
    return img

def add_dialogue_to_panel(panel_img_path, dialogues_for_panel, out_path):
    img = Image.open(panel_img_path).convert('RGB')
    x = 20
    y = 20
    for speaker, text, _ in dialogues_for_panel:
        bubble_text = f"{speaker + ': ' if speaker else ''}{text}"
        img = draw_speech_bubble(img, bubble_text, pos=(x, y))
        y += 120
    img.save(out_path)
