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

def idc_image_firstlast(idc_number):
    idc_in = open(os.path.join('U:\\UNIBASE\\idc', job_idc_dir, idc_number))
    for line in idc_in:
        if 'MBC' in line:
            image_type = 'MBC'
            break
        if 'SNC' in line:
            image_type = 'SNC'
            break
        if 'MNC' in line:
            image_type = 'MNC'
            break
    idc_in = open(os.path.join('U:\\UNIBASE\\idc', job_idc_dir, idc_number))
    counter = 0
    for line in idc_in:
        counter += 1
        if counter == 1:
            first_image_number = line[20:26]
    last_line = counter
    counter_2 = 0
    idc_in = open(os.path.join('U:\\UNIBASE\\idc', job_idc_dir, idc_number))
    for line in idc_in:
        counter_2 += 1
        if counter_2 == last_line:
            last_image_number = line[20:26]
    counter_3 = 0
    idc_in = open(os.path.join('U:\\UNIBASE\\idc', job_idc_dir, idc_number))
    for line in idc_in:
        if line[37] == '1':
            counter_3 += 1
    if counter_3 is 0:
        employer_count = last_line
    elif counter_3 > 0:
        employer_count = counter_3
    return (image_type, first_image_number, last_image_number, last_line, employer_count)

def user_experience():
    line = input('Initials? ')
    user_dir = get_user(line)
    stripped_user_dir = user_dir.strip()
    pickup_folder = (os.path.join('V:\\ZIP HOMEWORKER', stripped_user_dir, 'pickup'))
    while True:
        line_2 = input('Batch Number: ')
        if line_2 == '00000':
            user_experience()
        if line_2 == '99999':
            archiver(stripped_user_dir)
            copifier(stripped_user_dir)
            user_experience()
        line_2_clean = line_2 + '.IDC'
        print('Batch Type:', idc_image_firstlast(line_2_clean)[0],
              'First Employer:', idc_image_firstlast(line_2_clean)[1],
              'Last Employer:', idc_image_firstlast(line_2_clean)[2],
              'Employer Count:', idc_image_firstlast(line_2_clean)[4])
        read_idc(line_2_clean, pickup_folder)

user_experience()
