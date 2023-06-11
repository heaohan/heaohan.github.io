# import OS module
#import os

# Get the list of all files and directories
path = "./certificate/"
#dir_list = os.listdir(path)

from pathlib import Path
results = list(Path(path).rglob("*.pdf"))

print("Files and directories in '", path, "' :")

dir_list_web = []
dir_list_name = []
dir_list_md = []
dir_list_parents = []
for file in results:
    dir_list_parents.append(file.parent.as_posix())
    new_file = file.as_posix()
    new_file = new_file.replace(" ", "%20")
    new_file = new_file.replace("\\", "/")
    new_file = "https://heaohan.github.io/files/" + new_file
    dir_list_web.append(new_file)
    new_file_name = file.name.removeprefix("CertificateOfCompletion_")
    new_file_name = new_file_name.removesuffix(".pdf")
    dir_list_name.append(new_file_name)
    dir_list_md.append(f"- [{new_file_name}]({new_file})")
# prints all files
#print(dir_list)
#print(dir_list_web)


import pandas as pd
dict = {'parents': dir_list_parents, 'name': dir_list_name, 'address': dir_list_web, "md": dir_list_md}
     
df = pd.DataFrame(dict)
print(df)
df.to_csv("./certificates_list.csv")