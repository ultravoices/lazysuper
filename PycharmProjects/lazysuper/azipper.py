import os
import zipfile


def zip_it_up(folder):
        folder = os.path.abspath(folder)
        zipfilename = os.path.basename(folder) + '.zip'
        print('creating...' + zipfilename)
        backupzip = zipfile.ZipFile(zipfilename, 'w')
        for foldername, subfolders, filesnames in os.walk(folder):
            print('Adding files in %s...' % (zipfilename))
            newbase = os.path.basename(folder) + ' '
            if zipfilename.startswith(newbase) and zipfilename.endswith('.zip'):
                continue
            backupzip.write(os.path.join(foldername, zipfilename))
        backupzip.close()
        print('Done.')

zip_it_up('V:\\ZIP HOMEWORKER\\bsmith\\pickup')