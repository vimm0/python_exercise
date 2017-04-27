import os
# import os import path
# ls=[ "/one/two/three","/one/two/three/","/",".",""]
# print(ls)
# for path in ls:
	# print ("%15s : %s" % (path, os.path.split(path)))
	# print ("%15s : %s" % (path, os.path.basename(path)))
	# print ("%15s : %s" % (path, os.path.split(path)))
	# print ("%15s : %s" % (path, os.path.split(path)))
	# print ("%15s : %s" % (path, os.path.split(path)))
# command=['cd ..','ls']
# command='cd ~'
# print(process.read())
# print(getstatus('lorem.txt'))
import subprocess
subprocess.call('df -k', shell=True)# subprocess.call("echo $HOME", shell=True)
# ak='cd ~'
# # process=os.popen(command)
# p1=os.popen(ak)
# p1.mkdir('yellow')
# print(p1.read())

# for command in ['ls','cd ~','ls']:
# 	# command=command.pop()
# 	# print(command)
# 	process=os.popen(command)
# 	print(process.read())

# print(dir(command))
# process=os.popen(command)
# str(process.read())
# print(process.read())
# import mmap
# import contextlib
# with open("lorem.txt", "r") as f:
# 	with contextlib.closing(mmap.mmap(f.fileno(), 0,access=mmap.ACCESS_READ)) as m:
# 		print ("First 10 bytes via read :", m.read(10))
# 		print ("First 10 bytes via slice:", m[:10])
# 		print ("2nd 10 bytes via read :", m.read(10))



# import os.path
# FILENAMES = [ __file__,os.path.dirname(__file__),"/","./broken_link",]
# for file in FILENAMES:
# 	print ("File:",file)
# 	print ("Absolute:",os.path.isabs(file))
# 	print ("Is File?:",os.path.isfile(file))
# 	print ("Is Dir?:",os.path.isdir(file))
# 	print ("Is Link?:",os.path.islink(file))
	# 	print ("Mountpoint? :",os.path.ismount(file))
# 	print ("Exists?:",os.path.exists(file))
# 	print ("Link Exists?:",os.path.lexists(file))
# 	print()
# import dircache
# path ="."
# first = dircache.listdir(path)
# second = dircache.listdir(path)
# print ("Contents :")
# for name in first:
# 	print (" ", name)
# 	print()
# 	print ("Identical:", first is second)
# 	print ("Equal:", first == second)	


# for parts in [ (’one’, ’two’, ’three’),(’/’, ’one’, ’two’, ’three’),(’/one’, ’/two’, ’/three’),]:
# print (parts, ’:’, os.path.join(*parts))
