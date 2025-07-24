# Prompt2Material
Leveraging stable diffusion XL to generate seamless textures from a single prompt

# Requirements
<pre>```pip show diffusers || pip install diffusers

pip show torch || pip install torch

pip show opencv-python || pip install opencv-python

pip show Flask || pip install Flask

pip show Pillow || pip install torch

pip show numpy || pip install numpy```</pre>

# Usage
 ``./generate_material.sh --prompt "Your texture prompt here"``

  ``./generate_material.sh --prompt "Your texture prompt here" --view_results`` To see generate material

  Texture, normal map and displacement (extrusion) map are saved in ``results/``.
  
# Prompt Tips
Texture generation works best with tags like 'seamless', 'pbr', 'texture', 'topview'

# Flask full web-UI
Coming soon
