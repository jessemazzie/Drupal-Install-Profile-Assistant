#Written on 8/20/2016
#By Jesse Mazzie

import os

os.chdir('modules')
print(os.getcwd() + " is the current directory.\n")

modDir = os.getcwd()

modules = [ item for item in os.listdir (modDir) if os.path.isdir(os.path.join(modDir, item)) ]

print (modules)

infoFile = open('example.info', 'w')

count = 0


#Loop to write module dependencies to info file
for item in modules:
	infoFile.write( 'dependencies[] = ' + modules[count] + '\n')
	count += 1 
	