import os

job_idc_dir = 'MOSTATE'


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

print(idc_image_firstlast('44510.IDC'))
