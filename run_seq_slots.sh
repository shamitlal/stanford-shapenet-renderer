find /home/mprabhud/dataset/out_shapenet_splits/$1  -name *.obj -print0 | xargs -0 -n1 -P3 -I {} /home/mprabhud/blender-2.79b-linux-glibc219-x86_64/blender --background --python render_blender.py -- --output_folder /home/mprabhud/dataset/shapenet_renders/cars/$1 {} --format OPEN_EXR --color_depth 16


 find /home/mprabhud/dataset/out_shapenet_splits/$1 -name *.obj -exec /home/mprabhud/blender-2.79b-linux-glibc219-x86_64/blender --background --python render_blender.py -- --output_folder /home/mprabhud/dataset/shapenet_renders/cars/$1 {} --format OPEN_EXR --color_depth 16 \;
