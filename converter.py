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


image_types = [".png", ".jpg", ".jpeg", ".JPG"]
for folder_number, folder in enumerate(folders, 1):
	print("Processing " + str(folder_number) + " of " + str(folder_length))

	folder_images = [(folder + "/*" + image_type).encode(fileencoding) for image_type in image_types]
	command = ["convert"] + folder_images +  [(folder + ".pdf").encode(fileencoding)]
	call(command)

	#call(["convert", (folder + "/*").encode(fileencoding), (folder + ".pdf").encode(fileencoding)])

print("Done!")

