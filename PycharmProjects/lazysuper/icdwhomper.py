import os
import shutil

job_idc_dir = 'MOSTATE'


def get_user(identifier):
    f_user_in = open('userlist.txt')
    for row in f_user_in:
        trial = row[:3]
        dirname = row[4:]
        if trial == identifier:
            return dirname


def archiver(stripped_user_dir):
    shutil.make_archive(os.path.join('V:\\ZIP HOMEWORKER', stripped_user_dir, 'pickup'),
                        format="zip",
                        root_dir=os.path.join('V:\\ZIP HOMEWORKER', stripped_user_dir),
                        base_dir='pickup')
    print("Making Archive...")


def copifier(stripped_user_dir):
    if stripped_user_dir == 'jseals':
        shutil.copy(os.path.join('V:\\ZIP HOMEWORKER', stripped_user_dir, 'pickup.zip'),
                os.path.join('C:\\users\\sup\\Dropbox', 'cseals', 'pickup.zip'))
        print("Copying it special for Cheryl...")
    else:
        shutil.copy(os.path.join('V:\\ZIP HOMEWORKER', stripped_user_dir, 'pickup.zip'),
                    os.path.join('C:\\users\\sup\\Dropbox', stripped_user_dir, 'pickup.zip'))
        print("Copying to Dropbox...")
    shutil.copy(os.path.join('V:\\ZIP HOMEWORKER', stripped_user_dir, 'pickup.zip'),
                os.path.join('X:\\', stripped_user_dir))
    print("Copying to FTP...")


def read_idc(idc_number, pickup_folder):
    idc_in = open(os.path.join('U:\\UNIBASE\\idc', job_idc_dir, idc_number))
    shutil.copy(os.path.join('U:\\UNIBASE\idc', job_idc_dir, idc_number),
                os.path.join(pickup_folder, 'idc', job_idc_dir, idc_number))
    for line in idc_in:
        stripped_line = line.strip()
        sliced_line = stripped_line[:30]
        if not os.path.isdir(os.path.join(pickup_folder, 'image', stripped_line[:20])):
            os.mkdir(os.path.join(pickup_folder, 'image', stripped_line[:20]))
        shutil.copy(os.path.join('U:\\UNIBASE\image', sliced_line), os.path.join(
            pickup_folder, 'image', sliced_line))


def user_experience():
    myD = {}
    line = input('Initials? ')
    user_dir = get_user(line)
    stripped_user_dir = user_dir.strip()
    pickup_folder = (os.path.join('V:\\ZIP HOMEWORKER', stripped_user_dir, 'pickup'))
    while True:
        line_2 = input('IDC? ')
        if line_2 == '00000':
            user_experience()
        if line_2 == '99999':
            archiver(stripped_user_dir)
            copifier(stripped_user_dir)
            user_experience()
        line_2_clean = line_2 + '.IDC'

        read_idc(line_2_clean, pickup_folder)


user_experience()
