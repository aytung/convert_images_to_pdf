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

# do not want to waste effort for pdfs already created
# keep pdf names without extension
remove_pdf_extension = lambda pdf_name : pdf_name[:pdf_name.index(".pdf")]
old_pdfs = [remove_pdf_extension(folder) for folder in folders if ".pdf" in folder]

# do not want anything with a file extension -- ie, a file and pdfs already created
folders = [folder for folder in folders if "." not in folder and folder not in old_pdfs]


folder_length = len(folders)

# only accept images of these types
image_types = [".png", ".jpg", ".jpeg", ".JPG"]

for folder_number, folder in enumerate(folders, 1):
	print("Processing " + str(folder_number) + " of " + str(folder_length))

	# find and split each separate files
	files = check_output(["ls", folder]).decode(fileencoding)
	files = files.split("\n")[:-1]

	# find all extension types
	files = [file[file.find("."):] for file in files]

	from collections import Counter 

	# only include the types that are accepted image types
	file_types = [key for key in Counter(files).keys() if key in image_types]

	folder_images = [(folder + "/*" + file_type).encode(fileencoding) for file_type in file_types]
	command = ["convert"] + folder_images +  [(folder + ".pdf").encode(fileencoding)]
	call(command)

	#call(["convert", (folder + "/*").encode(fileencoding), (folder + ".pdf").encode(fileencoding)])

print("Done!")

