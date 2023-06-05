# import OS module
import os

# Get the list of all files and directories
path = "./certificate/"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

dir_list_web = []
dir_list_name = []
dir_list_md = []
for file in dir_list:
    new_file = file.replace(" ", "%20")
    new_file = "https://heaohan.github.io/files/certificate/" + new_file
    dir_list_web.append(new_file)
    new_file_name = file.removeprefix("CertificateOfCompletion_")
    new_file_name = new_file_name.removesuffix(".pdf")
    dir_list_name.append(new_file_name)
    dir_list_md.append(f"[{new_file_name}]({new_file})")
# prints all files
#print(dir_list)
#print(dir_list_web)


import pandas as pd
dict = {'name': dir_list_name, 'address': dir_list_web, "md": dir_list_md}
     
df = pd.DataFrame(dict)
print(df)
df.to_csv("./certificates_list.csv")