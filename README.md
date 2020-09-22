# Stanford Shapenet Renderer

A little helper script to render .obj files (such as from the stanford shapenet database) with Blender.

Tested on Linux, but should also work for other operating systems.
By default, this scripts generates 30 images by rotating the camera around the object.
Additionally, depth, albedo and normal maps are dumped for every image.

Tested with Blender 2.79.

## Example invocation

To render a single `.obj` file, run

    blender --background --python render_blender.py -- --output_folder /tmp path_to_model.obj

To get raw values that are easiest for further use, use `--format OPEN_EXR`. If the .obj file references any materials defined in a `.mtl` file, it is assumed to be in the same folder with the same name.

## Batch rendering

To render a whole batch, you can e. g. use the unix tool find:

    find . -name *.obj -exec blender --background --python render_blender.py -- --output_folder /tmp {} \;

To speed up the process, you can also use xargs to have multiple blender instances run in parallel using the `-P` argument

    find . -name *.obj -print0 | xargs -0 -n1 -P3 -I {} blender --background --python render_blender.py -- --output_folder /tmp {}

## Example images

Here is one chair model rendered with 30 different views:

![Chairs](examples/out_without_specular.png)

blender --background --python render_blender.py -- --output_folder /home/mprabhud/dataset/stanford_shapenet /home/mprabhud/dataset/preprocessed_shapenet_4/02958343_ffbf897d9867fadff9a62a8acc9e8cfe.obj --format OPEN_EXR --color_depth 16

find /home/mprabhud/dataset/out_shapenet_splits/split0  -name *.obj -print0 | xargs -0 -n1 -P6 -I {} blender --background --python r
ender_blender.py -- --output_folder /home/mprabhud/dataset/shapenet_renders/cars/ {} --format OPEN_EXR --color_depth 16

find /home/mprabhud/dataset/out_shapenet_splits/split1  -name *.obj -print0 | xargs -0 -n1 -P6 -I {} blender --background --python render_blender.py -- --output_folder /home/mprabhud/dataset/shapenet_renders/cars/ {} --format OPEN_EXR --color_depth 16

find /home/mprabhud/dataset/out_shapenet_splits/split2  -name *.obj -print0 | xargs -0 -n1 -P6 -I {} blender --background --python render_blender.py -- --output_folder /home/mprabhud/dataset/shapenet_renders/cars/ {} --format OPEN_EXR --color_depth 16
=======


# Pydisco occupancy rendering

Execute: python render_pdisco_occs.py

This will first take the saved occ voxels and convert it to mesh. Then it will process the mesh to get it in 
required pose. Finally, the mesh is rendered.

