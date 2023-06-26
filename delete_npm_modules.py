import os

PAR_PATH = r"" # Path of the folder that contains subfolders that have node_modules folder
cmd = "rmdir /s /q "

for file in os.listdir(PAR_PATH):
    current_path =  '"' + os.path.join(PAR_PATH, file, "node_modules") + '"'
    try:
        os.system(cmd + current_path)
        print(f"{current_path} - Deleted")
    except Exception as err:
        pass
        
os.system('pause')