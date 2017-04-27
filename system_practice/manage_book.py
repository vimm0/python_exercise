# import glob
# import os
# #For Python books
# new_file = "/home/vimm/study_room/python_book"
# new_lower_python="/home/vimm/study_room/*python*.pdf"
# new_upper_python="/home/vimm/study_room/*Python*.pdf"
# if not os.path.exists(new_file):
# 	os.makedirs(new_file)
# 	with open('lower_python', 'wt') as f:
# 		for name in glob.glob("/home/vimm/study_room/*python*.pdf"):#Lower-cased Python named books
# 			f.write(name+'\n')
# 	f.close()
# 	command_lower="mv"+" "+ new_lower_python+ " "+ new_file
# 	os.popen(command_lower )

# 	with open('upper_python', 'wt') as f:
# 		for name in glob.glob("/home/vimm/study_room/*Python*.pdf"):#Upper-cased Python named books
# 			f.write(name + '\n')
# 	f.close()
# 	command_upper="mv"+" "+ new_upper_python+ " "+ new_file
# 	os.popen(command_upper)
# elif os.path.exists(new_file):
# 	os.makedirs(new_file)
# 	with open('lower_python', 'wt') as f:
# 		for name in glob.glob("/home/vimm/study_room/*python*.pdf"):  # Lower-cased Python named books
# 			f.write(name + '\n')
# 	f.close()
# 	command_lower = "mv" + " " + new_lower_python + " " + new_file
# 	os.popen(command_lower)

# 	with open('upper_python', 'wt') as f:
# 		for name in glob.glob("/home/vimm/study_room/*Python*.pdf"):  # Upper-cased Python named books
# 			f.write(name + '\n')
# 	f.close()
# 	command_upper = "mv" + " " + new_upper_python + " " + new_file
# 	os.popen(command_upper)
# else:
# 	pass
# #For Django books
# new_file = "/home/vimm/study_room/django_book"
# new_lower_python = "/home/vimm/study_room/*django*.pdf"
# new_upper_python = "/home/vimm/study_room/*Django*.pdf"
# if not os.path.exists(new_file):
# 	os.makedirs(new_file)
# 	with open('lower_django', 'wt') as f:
# 		for name in glob.glob("/home/vimm/study_room/*django*.pdf"):  # Lower-cased Django named books
# 			f.write(name + '\n')
# 	command_lower = "mv" + " " + new_lower_python + " " + new_file
# 	os.popen(command_lower)
# 	f.close()
# 	with open('upper_django', 'wt') as f:
# 		for name in glob.glob("/home/vimm/study_room/*Django*.pdf"):  # Upper-cased Django named books
# 			f.write(name + '\n')
# 	command_upper = "mv" + " " + new_upper_python + " " + new_file
# 	os.popen(command_upper)
# 	f.close()
# elif os.path.exists(new_file):
# 	with open('lower_django', 'wt') as f:
# 		for name in glob.glob("/home/vimm/study_room/*django*.pdf"):  # Lower-cased Django named books
# 			f.write(name + '\n')
# 	command_lower = "mv" + " " + new_lower_python + " " + new_file
# 	os.popen(command_lower)
# 	f.close()
# 	with open('upper_django', 'wt') as f:
# 		for name in glob.glob("/home/vimm/study_room/*Django*.pdf"):  # Upper-cased Django named books
# 			f.write(name + '\n')
# 	command_upper = "mv" + " " + new_upper_python + " " + new_file
# 	os.popen(command_upper)
# 	f.close()
# else:
# 	pass
"""
End Program
"""


# new_file = "/home/vimm/study_room/python_book"
# # change_dir=os.chdir('/home/vimm/study_room')
# lower_cased_python=glob.glob("/home/vimm/study_room/*python*.pdf")
# with open('lower_python', 'r') as r:
# 	one_book=str(r.readlines()[1])
# 	os.popen('cp one_book new_file')

# print(list_book())
# if search(*.pdf)#check for pdf files
# import re
# from shutil import *

# with open('extra_books','wt') as f:
# 	for name in glob.glob("/home/vimm/study_room/*.pdf"):
# 		f.write(name+'\n')
		# f.sort()
# new_file = "/home/vimm/study_room/python_book"
# count=0
# with open('lower_python','r') as r:
# 	# count=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
# 	# for i in count:
# 	# print(r.readlines())
# 	line=str(r.readlines())
# 	if line.endswith("\n"):
# 		# count+=1
# 		print(line)
	# print(r.readlines()[i])
	# one_book=r.readlines()[0]
	# print((one_book))
	# os.popen('ls')
	# print(list)
	# if not os.path.exists(new_file):
	# 	os.makedirs(new_file)
	# 	os.popen('cp one_book new_file')
	# 	# copytree("line","new_python_book_dir")
	# 	# copyfile("line", "new_python_book_dir")
	# else:
	# 	os.popen('cp one_book new_file')
		# copyfile("line", "new_python_book_dir")

		# if line.endswith("\n"):
		# 	if not os.path.exists(line):
		# 		if not os.path.exists(new_file):
		# 			new_python_book_dir = os.makedirs("/home/vimm/study_room/python_book")
		# 			copyfile("line","new_python_book_dir")
		# 		else:
		# 			copyfile("line","new_python_book_dir")
		# 			os.makedirs("/home/vimm/study_room/python_book")

	# 	count+=1
	# 	print(count)
	# 	print(line)

		# count=count(line)
		# print(line)
		# print("books",count)


# import linecache
# import os
# module_line=linecache.getline(’somefile’)
# print (repr(module_line))
# with open('somefile','r') as r:
# 	if r.read().endswith('.pdf'):
# 		with open('somefile','w+') as f:
# 			f.write('\n')
# 	# print(r.read())

"""
OPTIMIZATION
"""
import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")

# import re

# line = "Cats are smarter than dogs";

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
   print ("searchObj.group() : ", searchObj.group())
   print ("searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))
else:
   print ("Nothing found!!")