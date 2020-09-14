from subprocess import Popen, PIPE
import shlex
import time
import os 
import sys 
from voxel_to_mesh import save_voxel_to_mesh
import numpy as np 
import ipdb
st = ipdb.set_trace

# carla_sim = "../../CarlaUE4.sh -carla-server -windows -ResX=100 -ResY=100 -benchmark"
# carla_sim_args = shlex.split(carla_sim)

basedir = "/home/shamitl/trash/automated_dir"
occs_dir = os.path.join(basedir, 'occs')
intermediate_meshdir = os.path.join(basedir, 'intermesh')
final_meshdir = os.path.join(basedir, 'finalmesh')
render_dir = os.path.join(basedir, 'renders')

cnt = 0
for occ in os.listdir(occs_dir):
    # Convert npy to mesh.
    occ_path = os.path.join(occs_dir, occ)
    intermediate_mesh_path = os.path.join(intermediate_meshdir, occ[:-4]+".obj")
    voxel_grid = np.load(occ_path ,allow_pickle=True)
    save_voxel_to_mesh(voxel_grid, intermediate_mesh_path)
    print("Done with intermediate mesh creation")

    # Process the mesh to fix scale, location, and rotation
    final_mesh_path = os.path.join(final_meshdir, occ[:-4]+".obj")
    blender_command = f'blender --background --python preprocess_pydisco_occ_meshes.py -- --input_mesh_path {intermediate_mesh_path} --output_mesh_path {final_mesh_path}'
    blender_command_args = shlex.split(blender_command)
    p1 = Popen(blender_command_args, stdout=PIPE, stderr=PIPE)
    time.sleep(0.1)
    out, err = p1.communicate()
    print(err)
    print("Done with final mesh creation")
    

    # Render
    blender_command = f'blender --background --python render_blender.py -- --output_folder {render_dir} {final_mesh_path} --format OPEN_EXR --color_depth 16'
    blender_command_args = shlex.split(blender_command)
    p1 = Popen(blender_command_args, stdout=PIPE, stderr=PIPE)
    time.sleep(0.1)
    out, err = p1.communicate()
    print(err)
    print("Done with rendering")