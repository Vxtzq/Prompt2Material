# Prompt2Material
Leveraging stable diffusion XL to generate seamless textures from a single prompt

# Requirements
<pre>python -m pip show diffusers     || python -m pip install diffusers
python -m pip show torch         || python -m pip install torch
python -m pip show opencv-python || python -m pip install opencv-python
python -m pip show Flask         || python -m pip install Flask
python -m pip show Pillow        || python -m pip install Pillow
python -m pip show numpy         || python -m pip install numpy
</pre>

# Usage
 ``./generate_material.sh --prompt "Your texture prompt here"``

  ``./generate_material.sh --prompt "Your texture prompt here" --view_results`` To see generate material

  Texture, normal map and displacement (extrusion) map are saved in ``results/``.
  
# Prompt Tips
Texture generation works best with tags like 'seamless', 'pbr', 'texture', 'topview'

# Flask full web-UI
Coming soon
