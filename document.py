import os
import shutil

from_dir="/Users/jiyasavalia/Downloads"
to_dir="/Users/jiyasavalia/Desktop/DocumentFiles"
listoffiles=os.listdir(from_dir)
for file_name in listoffiles:
    name,ext=os.path.splitext(file_name)
    if ext=="":
        continue
    if ext in ['.txt','.doc','.docx','.pdf']:
        path1=from_dir+'/'+file_name
        path2=to_dir+'/'+"Document_Files"
        path3=to_dir+'/'+"Document_Files"+'/'+ file_name
        if os.path.exists(path2):
            print("Moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving")
            shutil.move(path1,path3)