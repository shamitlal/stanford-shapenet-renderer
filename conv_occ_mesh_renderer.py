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


root = "/home/shamitl/projects/convolutional_occupancy_networks/out/pointcloud/shapenet_grid32/generation_pretrained/meshes"
npzroot = "/projects/katefgroup/datasets/ShapeNet/"
gt_mesh_download = "http://shapenet.cs.stanford.edu/shapenet/obj-zip/ShapeNetCore.v1/{}/{}/model.obj"
# categories = ['03001627']
categories = ["02691156",  "02933112",  "03001627",  "03636649",  "04090263",  "04379243",  "04530566", "02828884",  "02958343",  "03211117",  "03691459",  "04256520",  "04401088"]
for category in categories:
    off_dir = os.path.join(root, category)
    obj_dir = os.path.join(root, category + "_obj")
    render_dir = os.path.join(root, category + "_render")
    gif_dir = os.path.join(root, category + "_gif")
    obj_gt_dir = os.path.join(root, category + "_obj_gt")
    render_gt_dir = os.path.join(root, category + "_render_gt")
    gif_gt_dir = os.path.join(root, category + "_gif_gt")
    
    if not os.path.isdir(obj_dir):
        os.mkdir(obj_dir)

    if not os.path.isdir(render_dir):
        os.mkdir(render_dir)

    if not os.path.isdir(gif_dir):
        os.mkdir(gif_dir)

    if not os.path.isdir(obj_gt_dir):
        os.mkdir(obj_gt_dir)

    if not os.path.isdir(render_gt_dir):
        os.mkdir(render_gt_dir)

    if not os.path.isdir(gif_gt_dir):
        os.mkdir(gif_gt_dir)


    off_meshes = [filename for filename in os.listdir(off_dir) if filename.endswith('.off')]
    off_meshes = np.random.permutation(off_meshes)
    count = 0
    for meshname in off_meshes:
        count +=1
        if count > 2:
            break
        scale = np.load(os.path.join(npzroot, category, meshname[:-4], 'pointcloud.npz'))['scale']
        # Convert mesh from off to obj format.
        off_filename = os.path.join(off_dir, meshname)
        mesh = meshio.read(
            off_filename,  # string, os.PathLike, or a buffer/open file
        )
        print("Done with mesh reading")
        obj_filename = os.path.join(obj_dir, meshname[:-3] + "obj")
        meshio.write(
            obj_filename,
            mesh,
        )
        print("Done with mesh writing")

        # Render meshes
        blender_command = f'blender --background --python render_blender.py -- --output_folder {render_dir} {obj_filename} --format OPEN_EXR --color_depth 16 --radius 1.25 --scale {scale}'
        blender_command_args = shlex.split(blender_command)
        p1 = Popen(blender_command_args, stdout=PIPE, stderr=PIPE)
        time.sleep(0.1)
        out, err = p1.communicate()
        print(err)
        print("Done with rendering")


        #Load rendered pngs to create gif
        saved_render_dir = os.path.join(render_dir, meshname[:-4])
        THETAS = list(range(0, 360, 45))
        PHIS = list(range(20, 80, 20))
        images = []
        for phi in PHIS:
            for theta in THETAS:
                pngfilename = os.path.join(saved_render_dir, f"{meshname[:-4]}_{theta}_{phi}_.png")
                pngimage = imageio.imread(pngfilename)
                images.append(pngimage)

        imageio.mimsave(f'{gif_dir}/{meshname[:-4]}.gif', images)
        print("Saved gif")
        # shutil.rmtree(saved_render_dir)
        # os.remove(obj_filename)
        # print("Deleted stuff")
        gt_link = gt_mesh_download.format(category, meshname[:-4])
        obj_filename = os.path.join(obj_gt_dir, meshname[:-3] + "obj")
        os.system(f"wget {gt_link} -O {obj_filename}")
        print("Downloaded gt mesh")

         # Render meshes
        blender_command = f'blender --background --python render_blender.py -- --output_folder {render_gt_dir} {obj_filename} --format OPEN_EXR --color_depth 16 --radius 1.25 --scale 1'
        blender_command_args = shlex.split(blender_command)
        p1 = Popen(blender_command_args, stdout=PIPE, stderr=PIPE)
        time.sleep(0.1)
        out, err = p1.communicate()
        print("Done with gt rendering")


        saved_render_dir = os.path.join(render_gt_dir, meshname[:-4])
        images = []
        for phi in PHIS:
            for theta in THETAS:
                pngfilename = os.path.join(saved_render_dir, f"{meshname[:-4]}_{theta}_{phi}_.png")
                pngimage = imageio.imread(pngfilename)
                images.append(pngimage)

        imageio.mimsave(f'{gif_gt_dir}/{meshname[:-4]}.gif', images)
        print("Saved gt gif")









        


