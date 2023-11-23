import os
import shutil


dir_path = input("Please input dir name:")

if os.path.exists(dir_path):
    os.chdir(dir_path)
else:
    print("Dir is error")
    exit()

for filename in os.listdir(dir_path):
    file_path = os.path.join(dir_path,filename)
    base_name,ext_name = os.path.splitext(filename)
    new_filename = base_name
    base_name = base_name.replace(".","")
 
    #del ()
    sN = base_name.find('(')
    if sN != -1:
        eN = base_name.rfind(')')
        if eN != -1:
            new_filename = base_name[:sN] + "" +base_name[(eN+1):]
        else:
            new_filename = base_name[:sN] + ""
    
    sN = new_filename.find('（')
    if sN != -1:
        eN = new_filename.rfind('）')
        if eN != -1:
            new_filename = new_filename[:sN] + "" + new_filename[(eN+1):]
        else:
            new_filename = new_filename[:sN] + ""
    
    #del 【
    sN = new_filename.find('【')
    if sN != -1:
        eN = new_filename.rfind('】')
        if eN != -1:
            new_filename = new_filename[:sN] + "" + new_filename[(eN+1):]
        else:
            new_filename = new_filename[:sN] + ""   

   #del [
    sN = new_filename.find('[')
    if sN != -1:
        eN = new_filename.rfind(']')
        if eN != -1:
            new_filename = new_filename[:sN] + "" + new_filename[(eN+1):]
        else:
            new_filename = new_filename[:sN] + ""     
    #del by
    sN = new_filename.find("by")
    if sN != -1:
        new_filename = new_filename[:sN]


    new_filename = new_filename.replace(" ","")
    new_filename = new_filename + ext_name
    #os.rename(file_path,os.path.join(dir_path,new_filename))
    shutil.move(file_path,os.path.join(dir_path,new_filename))
    
