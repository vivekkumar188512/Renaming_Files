import os

path  = os.getcwd().replace("\\","/")
# path = input("Please enter complete path of the folder where all the files located e.g. \"C/folder1/folder2/documents\" :\n").replace("\\","/")
old_text = input("please enter text which needs to be replaced by new text : \n")
new_text = input("please enter new text which will replace old text :\n")

for filename in os.listdir(path):
    newfilename = filename.replace(old_text, new_text)
    os.rename(path + "/" + filename,path + "/" + newfilename)
