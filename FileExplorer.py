import os

# !!! IMPORATNT: Change adress before running script
folder_path = "C:/Users/You_Username/Downloads"

count =0

all_elements = os.listdir(folder_path)

for file in all_elements:

    file_adress = os.path.join(folder_path, file)

    if os.path.isdir(file_adress):
        continue
    else:
        count += 1
        print(f'{count}. {file} \n')

print('___ \n Finished!')