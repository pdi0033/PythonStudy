from diffusers import DiffusionPipeline, LCMScheduler
from safetensors.torch import load_file
import torch
import os

pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0")
pipe.load_lora_weights("nerijs/pixel-art-xl")

prompt = "pixel art, a cute corgi" # , simple, flat colors"
negative_prompt = "3d render, realistic"

image = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        # num_inference_steps=8,
        guidance_scale=1.5,
    ).images[0]
image.save(f"lcm_lora_0.png")