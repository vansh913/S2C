import os
import argparse
from nlp_utils import parse_story
from character import CharacterDictionary
from generate_panel import load_text2img, load_img2img, text2img, img2img
from bubble_layout import add_dialogue_to_panel
from assemble import assemble_panels
from utils import ensure_dir, save_image
from PIL import Image

# DEFAULT PATHS MOVED TO D DRIVE
DEFAULT_OUT_DIR = r'E:\updated project\Story2Comic-main\Story2Comic-main\outputs\comics'
DEFAULT_TMP_DIR = r'E:\updated project\Story2Comic-main\Story2Comic-main\outputs\tmp'



import pathlib

def run_pipeline(story_path, out_dir=DEFAULT_OUT_DIR, tmp_dir=DEFAULT_TMP_DIR, mode='baseline'):
    # Strip whitespace chars from paths to avoid invalid path errors
    out_dir = str(out_dir).strip()
    tmp_dir = str(tmp_dir).strip()
    ensure_dir(out_dir)
    ensure_dir(tmp_dir)

    with open(story_path, 'r', encoding='utf-8') as f:
        text = f.read()

    sentences, characters, dialogues = parse_story(text)

    # build character dictionary
    char_dict = CharacterDictionary()
    for name in characters.keys():
        char_dict.add_or_update(name, attrs=list(characters[name]['attrs']))

    # load pipelines
    text_pipe = load_text2img()
    img_pipe = load_img2img()

    # generate reference portraits
    for name, prof in char_dict:
        prompt = (
            f"manga portrait of {name}, black and white line art, consistent character, half-body"
            + (" " + ", ".join(prof.attrs) if prof.attrs else "")
        )

        ref = text2img(text_pipe, prompt, height=512, width=512, steps=20)
        # Ensure tmp_dir path is normalized to handle spaces properly
        tmp_dir_path = pathlib.Path(tmp_dir).resolve()
        ref_path = tmp_dir_path / f"ref_{name.replace(' ', '_')}.png"

    panel_paths = []

    # generate panels (one per sentence)
    prev_panel = None
    for i, sent in enumerate(sentences):
        prompt = f"manga panel: {sent} -- black and white line art, cinematic composition"
        tmp_dir_path = pathlib.Path(tmp_dir).resolve()
        panel_path = tmp_dir_path / f"panel_{i}.png"

        if mode == 'baseline' and prev_panel is not None:
            init_img = Image.open(prev_panel).convert('RGB').resize((512, 512))
            img = img2img(img_pipe, init_img, prompt, strength=0.6, steps=18)
            save_image(img, panel_path)
        else:
            img = text2img(text_pipe, prompt, height=512, width=512, steps=20)
            save_image(img, panel_path)

        # attach dialogues to this panel
        dialogues_for_panel = [d for d in dialogues if d[2] == i]

        if dialogues_for_panel:
            bubble_path = tmp_dir_path / f"panel_{i}_bubble.png"
            add_dialogue_to_panel(str(panel_path), dialogues_for_panel, str(bubble_path))
            panel_paths.append(str(bubble_path))
            prev_panel = str(bubble_path)
        else:
            panel_paths.append(str(panel_path))
            prev_panel = str(panel_path)

    final_path = os.path.join(out_dir, 'comic_final.png')

    assemble_panels(panel_paths, final_path, cols=2)

    print('Saved final comic to', final_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('story', nargs='?', default='example/example_story.txt')

    # Updated defaults to D drive
    parser.add_argument('--out', default=DEFAULT_OUT_DIR)
    parser.add_argument('--tmp', default=DEFAULT_TMP_DIR)

    parser.add_argument('--mode', choices=['baseline', 'enhanced'], default='baseline')

    args = parser.parse_args()

    run_pipeline(args.story, out_dir=args.out, tmp_dir=args.tmp, mode=args.mode)
