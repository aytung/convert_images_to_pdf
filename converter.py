from subprocess import * 

# get the fileencoding
import sys
fileencoding = sys.getfilesystemencoding()

# print out all folders/files
folders = check_output(["ls", "*/", "-d"], shell=True)
# decode into string format
folders = folders.decode(fileencoding)
# separate string into folder/file names
folders = folders.split("\n")[:-1]

# do not want anything with a file extension -- ie, a file
folders = [folder for folder in folders if "." not in folder]

folder_length = len(folders)

for folder_number, folder in enumerate(folders, 1):
	print("Processing " + str(folder_number) + " of " + str(folder_length))
	call(["convert", (folder + "/*").encode(fileencoding), (folder + ".pdf").encode(fileencoding)])

print("Done!")

