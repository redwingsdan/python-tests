import os
import shutil
#w = write permissions (create if not exists)
#r = read permissions
#a = append to end of file
myFile = open('filemanipulationtest.txt', 'w+')
myFile.write('This is a test string')
myFile.close()
os.rename('D:/Python/filemanipulationtest.txt', 'D:/Python/filedir1/filemanipulationtest.txt')
shutil.move('D:/Python/filedir1/filemanipulationtest.txt', 'D:/Python/filedir2/filemanipulationtest.txt')
os.remove('D:/Python/filedir2/filemanipulationtest.txt')