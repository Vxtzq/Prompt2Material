import torch
from diffusers import StableDiffusionXLPipeline
import argparse

# Patch Conv2d to use circular padding for seamless texture generation
def patch_conv(padding_mode='circular'):
    cls = torch.nn.Conv2d
    orig_init = cls.__init__
    def __init__(self, *args, **kwargs):
        return orig_init(self, *args, **kwargs, padding_mode=padding_mode)
    cls.__init__ = __init__

patch_conv()

# Parse command line arguments
parser = argparse.ArgumentParser(description="Generate seamless texture using Stable Diffusion XL.")
parser.add_argument('prompt', type=str, help='Text prompt for image generation')
args = parser.parse_args()

# Load SDXL model
pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0", 
    torch_dtype=torch.float16,
    variant="fp16",
    use_safetensors=True
)
pipe = pipe.to("cuda")
pipe.enable_attention_slicing()           
pipe.enable_vae_tiling()                  
pipe.enable_model_cpu_offload()   
try:        
    pipe.enable_xformers_memory_efficient_attention()
except:
    pass

prompt = args.prompt

image = pipe(prompt, height=1024, width=1024, num_inference_steps=30).images[0]

image.save("results/texture.png")

