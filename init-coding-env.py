#! /bin/python

import os
import sys

scripts = os.getenv("WCC_SCRIPTS_PATH")
library = os.getenv("WCC_LIBRARY_PATH")
usedlib = ""

def fread(path):
	fil = open(path, "r")
	content = fil.read()
	fil.close()
	return content

def fwrite(path, content):
	fil = open(path, "w")
	fil.write(content)
	fil.close()

def initenv(name, lang):

	def cmakefile(clang):
		template = fread("%s/template/makefile-c"%scripts)
		template = template.replace("<NAME>", name).replace("<LANG>", clang).replace("<USEDLIB>", usedlib)
		template = template.replace("<COMPILE>", "gcc" if clang == "c" else "g++ -std=gnu++11");
		fwrite("Makefile", template)

	def cpptemplate():
		template = fread("%s/template/template.cpp"%scripts)
		template = template.replace("<NAME>", name.split(".")[0])
		fwrite("%s/template/template.lang"%scripts, template)

	def pymakefile():
		template = fread("%s/template/makefile-py"%scripts)
		template = template.replace("<NAME>", name)
		fwrite("Makefile", template)

	def pytemplate():
		template = fread("%s/template/template.py"%scripts)
		fwrite("%s/template/template.lang"%scripts, template)

	def javamakefile():
		base_name = name.split(".")[0]
		template = fread("%s/template/makefile-java"%scripts)
		template = template.replace("<NAME>", base_name);
		fwrite("Makefile", template)

	if lang == "c":
		name += ".c"
		cmakefile("c")
	if lang == "cpp" or lang == "c++":
		name += ".cpp"
		cmakefile("cpp")
		cpptemplate()
	if lang == "py" or lang == "python":
		name += ".py"
		pymakefile()
		pytemplate()
	if lang == "java" or lang == "j":
		name += ".java"
		javamakefile()

	os.system("echo %s > %s/share/sourcename"%(name, scripts))
	os.system("echo %s > %s/share/usedlib"%(usedlib, scripts))

if __name__ == "__main__":
	print "scripts: %s"%scripts
	print "library: %s"%library

	lang, name = sys.argv[1], sys.argv[2]
	for i in range(3, len(sys.argv)):
		usedlib += "-l%s "%sys.argv[i]

	initenv(name, lang)

	print "source file: %s"%name
	print "used libraries: %s"%usedlib
