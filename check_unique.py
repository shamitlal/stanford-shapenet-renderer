# filename = "/home/mprabhud/dataset/out_shapenet_splits/*"
# import glob
# import ipdb
# st = ipdb.set_trace
# st()
# abc = glob.glob(filename)
# new_abc = [i+"/*" for i in abc]
# all_files = []
# for file in new_abc:
# 	all_files = all_files + glob.glob(file)
# st()
# print(len(all_files))
# print(len(set(all_files)))
import os
for i in range(10):
	os.mkdir(f"/home/mprabhud/dataset/shapenet_renders/cars/split{i}")