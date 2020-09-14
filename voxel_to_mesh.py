
import skimage
from skimage.measure import marching_cubes as mcl
# from mayavi import mlab
import numpy as np


def save_voxel_to_mesh(voxel_grid, output_fname):
    voxel_grid = (voxel_grid>0.5)
    voxel_grid = voxel_grid.astype(np.float)

    verts, faces, normals, values = mcl(voxel_grid, 0.0)


    # mlab.triangular_mesh([vert[0] for vert in verts],
    #                         [vert[1] for vert in verts],
    #                         [vert[2] for vert in verts],
    #                         faces)
    faces = faces + 1
    #mlab.show()

    thefile = open(output_fname, 'w')
    for item in verts:
        thefile.write("v {0} {1} {2}\n".format(item[0],item[1],item[2]))
    for item in normals:
        thefile.write("vn {0} {1} {2}\n".format(item[0],item[1],item[2]))
    for item in faces:
        thefile.write("f {0}/{0} {1}/{1} {2}/{2}\n".format(item[0],item[1],item[2]))  
    thefile.close()

def main():
    # load voxel grid

    voxel_grid = np.load('shapenetcar_vox.npy' ,allow_pickle=True)
    print(f'shape of voxel grid: {voxel_grid.shape}') # D, H, W
    save_voxel_to_mesh(voxel_grid, "test1.obj")

if __name__ == "__main__":
    main()
