import os

# This is to get the directory that the program is currently running in.
def get_allfiles():
    all_files =[]
    all_files_roots =[]
    dir_path = os.path.dirname(os.path.realpath('C:/Users/ngane/Documents/GitHub/ESCwebsite/'))

    for root, dirs, files in os.walk(dir_path):
        for file in files:
            # print(root.replace("\\", '/'))
            if file.endswith('.html') and (root.replace('\\', '/') == 'C:/Users/ngane/Documents/GitHub/ESCwebsite'):
                all_files.append(str(file))
                all_files_roots.append(root+'/'+file)
    return all_files
