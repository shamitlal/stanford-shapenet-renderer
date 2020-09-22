from __future__ import print_function
import math, sys, random, argparse, json, os, tempfile, pickle
import mathutils
import shutil
import subprocess
import os
import numpy as np
import time
# import pathos.pools as pp
import bpy
import ipdb 
st = ipdb.set_trace

# blender --background --python preprocess_pydisco_occ_meshes.py -- --input_mesh_path /home/shamitl/trash/automated_dir/intermesh/shapenetcar_vox.obj --output_mesh_path /home/shamitl/trash/automated_dir/finalmesh/shapenetcar_vox.obj
parser = argparse.ArgumentParser(description='Renders given obj file by rotation a camera around it.')
parser.add_argument('--input_mesh_path', type=str,
                    help='Path to input mesh.')
parser.add_argument('--output_mesh_path', type=str,
                    help='Directory where to save output path.')

argv = sys.argv[sys.argv.index("--") + 1:]
args = parser.parse_args(argv)

for obj in bpy.context.scene.objects:
    obj.select = True
bpy.ops.object.delete()

imported_object = bpy.ops.import_scene.obj(filepath=args.input_mesh_path)
obj_object = bpy.context.selected_objects[0]
obj_object.scale=(0.05, 0.035, 0.08)
bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='MEDIAN')
obj_object.rotation_euler[1] = np.pi
obj_object.location[2] = 1
bpy.ops.export_scene.obj(filepath=args.output_mesh_path)


    
