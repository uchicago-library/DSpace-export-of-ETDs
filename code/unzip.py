from os.path import dirname, join, exists
import re
from os import scandir, mkdir
import zipfile

directory = "X:/ETDs"

contents = scandir(directory)

for f in contents:
    if f.name.endswith('.zip'):
        #zip_ref = zipfile.ZipFile(f.path, 'r')
        dirname = re.compile('(etdadmin_upload_\d{6})').search(f.name).group(1)
        path_root = "X:/ETDS"
        new_directory = join(path_root, dirname)
        if not(exists(new_directory)):
            mkdir(new_directory)
        zip_ref = zipfile.ZipFile(f.path, 'r')
        zip_ref.extractall(path=new_directory)
        zip_ref.close()
        print(new_directory)
        #print(zip_ref)