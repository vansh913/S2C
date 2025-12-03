from PIL import Image
import math

def assemble_panels(panel_paths, out_path, cols=2, panel_w=512, panel_h=512):
    rows = math.ceil(len(panel_paths) / cols)
    canvas_w = cols * panel_w
    canvas_h = rows * panel_h
    canvas = Image.new('L', (canvas_w, canvas_h), color=255)
    for i, p in enumerate(panel_paths):
        img = Image.open(p).convert('L').resize((panel_w, panel_h))
        x = (i % cols) * panel_w
        y = (i // cols) * panel_h
        canvas.paste(img, (x, y))
    canvas.save(out_path)
