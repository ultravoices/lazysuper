import os
import shutil

def rename_files(directory_name):
    for filename in os.listdir(os.path.join(r"U:\UNIBASE\image\WUMSURV", directory_name)):
        new_filename = filename[8:12] + filename[15:18] + filename[19:]
        os.rename(os.path.join(r"U:\UNIBASE\image\WUMSURV", directory_name, filename,),
                (os.path.join(r"U:\UNIBASE\image\WUMSURV", directory_name, new_filename)))

rename_files('101916A')