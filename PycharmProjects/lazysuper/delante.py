import os
import shutil

# def get_dir(date):
#    shutil.copy(os.path.join(r'\\SDS-SRV300\Delante\Check_Images\ASM_NET', date),
#                os.path.join(r'u:\unibase\idc\DLGCHKS', date))

# get_dir('206-05-05')

# def get_files_that_contain_front(dashed_date):
#    undashed_date = dashed_date[:2] + dashed_date[3:5] + dashed_date[6:8]
#   for filename in os.listdir((os.path.join(r"U:\UNIBASE\image\DLGRSTS", undashed_date))):
#        if "front" in filename:


def get_asm_folder_names():
    clean_asm_list = os.listdir(os.path.join(r"R:\Check_Images\ASM_NET"))
    clean_asm_list.remove('Archive Check Images')
    return clean_asm_list


def get_rust_folder_names():
    clean_rust_list = os.listdir(os.path.join(r"R:\Check_Images\RUST_O_US"))
    clean_rust_list.remove('Archive Check Images')
    return clean_rust_list


def date_undasher(dasheddate):
    undasheddate = dasheddate[5:7] + dasheddate[8:10] + dasheddate[2:4]
    return undasheddate

def copy_to_unibase_images():
    for dirname_asm in get_asm_folder_names():
        shutil.copytree(os.path.join(r"R:\Check_Images\ASM_NET", dirname_asm),
                        os.path.join(r"U:\UNIBASE\image\DLGCHKS", dirname_asm))
    for dirname_rust in get_rust_folder_names():
        shutil.copytree(os.path.join(r"R:\Check_Images\RUST_O_US", dirname_rust),
                        os.path.join(r"U:\UNIBASE\image\DLGRSTS", dirname_rust))

def asm_from_dashed_to_undashed_directory():
    for dirname_asm in get_asm_folder_names():
        shutil.copytree(os.path.join(r"U:\UNIBASE\image\DLGCHKS", dirname_asm),
                        os.path.join(r"U:\UNIBASE\image\DLGCHKS", date_undasher(dirname_asm)))

def rust_from_dashed_to_undashed_directory():
    for dirname_rust in get_rust_folder_names():
        shutil.copytree(os.path.join(r"U:\UNIBASE\image\DLGRSTS", dirname_rust),
                        os.path.join(r"U:\UNIBASE\image\DLGRSTS", date_undasher(dirname_rust)))
#    for filename in os.listdir(os.path.join(r"U:\UNIBASE\image\DLGRSTS", date_undasher(dirname_rust))):
#        if 'front' in filename:
#            pass
#        elif 'AOLDIMAGE' in filename:
#            pass
#        else:
#            os.remove(os.path.join(r"U:\UNIBASE\image\DLGRSTS", date_undasher(dirname_rust), filename))

def remove_not_front_rust():
    mylist = os.listdir(r"U:\UNIBASE\image\DLGRSTS")
    matches = []
    for each in mylist:
        if len(each) == 6:
            matches.append(each)
#    for each in matches:




#    for filename in (os.path.join(r"U:\UNIBASE\image\DLGRSTS", location)):
#       if filename.find("front") == -1:
#            os.remove(os.path.join(r"U:\UNIBASE\image\DLGRSTS", location, filename))
import os

def rename11(location):
    for filename in os.listdir(os.path.join(r"U:\UNIBASE\image\DLGRSTS", location)):
        if filename.startswith("000"):
            os.rename(os.path.join(r"U:\UNIBASE\image\DLGRSTS", location, filename, ),
                      os.path.join(r"U:\UNIBASE\image\DLGRSTS", location,
                                   filename[:10] + ".tif"))