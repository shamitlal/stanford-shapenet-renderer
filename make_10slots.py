folder = "/home/mprabhud/dataset/preprocessed_shapenet_4"
import glob
files = glob.glob(folder+"/*")
# import ipdb
# st = ipdb.set_trace
out_folder = "/home/mprabhud/dataset/out_shapenet_splits"
import shutil
import glob
import os
join = os.path.join
filename_filtered = list(set([filename[:-4] for filename in files]))

print(len(filename_filtered))
numSections = 10
sectionSize = len(filename_filtered)//numSections

for index,current_section in enumerate(range(numSections)):
	print(index)
	filename_current = filename_filtered[current_section*sectionSize:(current_section+1)*sectionSize]
	print(len(filename_current))
	out_folder_new = join(out_folder, f"split{index}")
	try:
		os.mkdir(out_folder_new)
	except Exception:
		print("already there")
	for ind,filename_current_i in enumerate(filename_current):
		print(index*sectionSize+ind)
		shutil.move(filename_current_i+".mtl",out_folder_new)
		shutil.move(filename_current_i+".obj",out_folder_new)

