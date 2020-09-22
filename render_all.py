import os 
import ipdb
st = ipdb.set_trace
root = "/home/shamitl/trash/pdisco_occs_obj"
paths = [os.path.join(root, f) for f in os.listdir(root) if f.endswith('.obj')]
for path in paths:
    # st()
    command = f'blender --background --python render_blender.py -- --output_folder /home/shamitl/trash/shapenet_render {path} --format OPEN_EXR --color_depth 16'
    os.system(command)