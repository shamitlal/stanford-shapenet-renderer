# from __future__ import print_function
import meshio
import math, sys, random, argparse, json, os, tempfile, pickle
import shutil
import subprocess
import os
import numpy as np
import time
# import bpy
from subprocess import Popen, PIPE
import shlex
import sys 
import imageio
import ipdb
st = ipdb.set_trace
import imageio

render_dir = "/home/shamitl/datasets/ShapeNet/renders"
gif_dir = "/home/shamitl/datasets/ShapeNet/gifs"
obj_filename = "/home/shamitl/datasets/ShapeNet/d69aad24d253474dc984897483a49e2b.obj"
meshname = "d69aad24d253474dc984897483a49e2b.obj"
scale = 1
blender_command = f'blender --background --python render_blender.py -- --output_folder {render_dir} {obj_filename} --format OPEN_EXR --color_depth 16 --radius 2 --scale {scale}'
blender_command_args = shlex.split(blender_command)
p1 = Popen(blender_command_args, stdout=PIPE, stderr=PIPE)
time.sleep(0.1)
out, err = p1.communicate()
# print(err)
print("Done with rendering")

saved_render_dir = os.path.join(render_dir, meshname[:-4])
THETAS = list(range(0, 360, 45))
PHIS = list(range(20, 80, 20))
images = []
for phi in PHIS:
    for theta in THETAS:
        pngfilename = os.path.join(saved_render_dir, f"{meshname[:-4]}_{theta}_{phi}_.png")
        pngimage = imageio.imread(pngfilename)
        # pngimage = pngimage[:,:,:3]
        # blackpixels = (pngimage[:,:,0]==0) & (pngimage[:,:,1]==0) & (pngimage[:,:,2]==0)
        # pngimage[blackpixels] = np.array([[255,255,255]])
        images.append(pngimage)

imageio.mimsave(f'{gif_dir}/{meshname[:-4]}.gif', images)