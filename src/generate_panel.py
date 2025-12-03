import os
import torch
from diffusers import StableDiffusionPipeline, StableDiffusionImg2ImgPipeline, DPMSolverMultistepScheduler
from PIL import Image
from typing import Optional

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
DEFAULT_MODEL = 'runwayml/stable-diffusion-v1-5'  # replace with your comic checkpoint if available

def load_text2img(model_id=DEFAULT_MODEL):
    pipe = StableDiffusionPipeline.from_pretrained(model_id,
                                                  torch_dtype=torch.float16 if DEVICE == 'cuda' else torch.float32)
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    pipe = pipe.to(DEVICE)
    try:
        pipe.enable_xformers_memory_efficient_attention()
    except Exception:
        pass
    return pipe

def load_img2img(model_id=DEFAULT_MODEL):
    pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id,
                                                          torch_dtype=torch.float16 if DEVICE == 'cuda' else torch.float32)
    pipe = pipe.to(DEVICE)
    try:
        pipe.enable_xformers_memory_efficient_attention()
    except Exception:
        pass
    return pipe

def text2img(pipe, prompt, height=512, width=512, steps=20, guidance=7.5, seed=None):
    generator = None
    if seed is not None:
        generator = torch.Generator(device=DEVICE).manual_seed(seed)
    out = pipe(prompt, height=height, width=width, num_inference_steps=steps,
               guidance_scale=guidance, generator=generator)
    img = out.images[0]
    # convert to high-contrast grayscale (manga-like)
    img = img.convert('L')
    return img

def img2img(pipe, init_image: Image.Image, prompt, strength=0.6, steps=20, guidance=7.5, seed=None):
    generator = None
    if seed is not None:
        generator = torch.Generator(device=DEVICE).manual_seed(seed)
    out = pipe(prompt=prompt, image=init_image.convert('RGB'),
               strength=strength, num_inference_steps=steps, guidance_scale=guidance,
               generator=generator)
    img = out.images[0].convert('L')
    return img

if __name__ == '__main__':
    pipe = load_text2img()
    img = text2img(pipe, "manga portrait of a young man, black and white line art, detailed")
    img.save('E:/updated project/Story2Comic-main/Story2Comic-main/outputs/tmp_test.png')
    print('Saved test image')
