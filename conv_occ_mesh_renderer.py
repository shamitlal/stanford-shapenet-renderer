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
import ipdb
st = ipdb.set_trace

filename = "/home/mprabhud/shamit/cvpr21/17DRP5sb8fy.off"
outfilename = "/home/mprabhud/shamit/cvpr21/newnew.obj"
render_dir = "/home/mprabhud/shamit/cvpr21/renders"

# Convert mesh from off to obj format.
mesh = meshio.read(
    filename,  # string, os.PathLike, or a buffer/open file
)
print("Done with mesh reading")
meshio.write(
    outfilename,
    mesh,
)
print("Done with mesh writing")

# Render meshes
blender_command = f'blender --background --python render_blender.py -- --output_folder {render_dir} {outfilename} --format OPEN_EXR --color_depth 16'
blender_command_args = shlex.split(blender_command)
p1 = Popen(blender_command_args, stdout=PIPE, stderr=PIPE)
time.sleep(0.1)
out, err = p1.communicate()
print(err)
print("Done with rendering")