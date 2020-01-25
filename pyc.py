import sys,os
import re as reg

class pyc():
	def __init__(self):
		
		try:
			self.filename = sys.argv[1]
			self.dirlist = sys.argv[2:]
			self.cfile = open(self.filename,'r')
			self.validateFile = self.cfile.read()
			self.headers = self.findHeader()
			self.files = self.findFiles()
			self.tafrget = os.getcwd()
		except IOError:
			print("Invalid file or path")
		except IndexError:
			print("Enter a valid file path")
			
	def showCode(self):
		try:
			print(self.validateFile)
		except AttributeError:
			print("No file passed")
	
	def findHeader(self):
		try:
			#print(len(self.validateFile))
			lines = self.validateFile.split('\n')
			headers = [m for m in lines if "#" in m]
			head = list()
			for m in headers:
				trig = 0
				ln = str()
				for i in range(0,len(m)):
					if m[i] == '<' or m[i] == '\"':
						trig = 1
						continue
					if trig == 1:
						ln = ln+m[i]
				#print(ln)
				if ln[len(ln)-1] == '>' or ln[len(ln)-1] == '\"':
					head.append(ln[:len(ln)-1])
				else:
					head.append(ln)
			
			return head
		except AttributeError:
			print("No file passed")
			
	def findFiles(self):
		lines = self.validateFile.split('\n')
		files = [m for m in lines if "fopen" in m]
		fil = list()
		for m in files:
			trig = 0
			ln = str()
			for i in range(0,len(m)):
				if m[i] == '(':
					trig = 1
					continue
				elif m[i] == ',':
					trig = 0
					continue
				if trig == 1:
					ln = ln+m[i]
				#print(ln)
			if ln[len(ln)-1] == '>' or ln[len(ln)-1] == '\"':
					fil.append(ln[:len(ln)-1])
			else:
				fil.append(ln.strip("\'"))
		return fil
		
	def macroFinder(self,pathx):
		mac = open(pathx,'r')
		macroFile = mac.read()
		lines = macroFile.split('\n')
		macrolist = list()
		for m in lines:
			for n in self.files:
				if n in m: 
					macrolist.append(n)
		#print(macrolist)
		macros = list()
		for m in lines:
				print(m)
				trig = 0
				ln = str()
				for i in range(0,len(m)):
					if m[i] == '\"':
						trig = 1
						continue
					if trig == 1:
						ln = ln+m[i]
				if len(ln) > 0:
					if ln[len(ln)-1] == '\"':
						macros.append(ln[:len(ln)-1])
					else:
						macros.append(ln)
				else:
					continue 
		#print(macros)
		return macros
		
		
	def findSource(self):
		#print(self.dirlist)
		reqFile = open("C_sources.txt","w")
		mfiles = list()
		if len(self.dirlist) == 0:
			print("ERROR: Enter the path of header files\n")
		else: 
			for p in self.dirlist:
				print(p)
				for n in self.macroFinder(p):
					mfiles.append(n)
			print(mfiles)
			for m in self.files:
				if ".txt" in m:
					mfiles.append(m)
				elif ".csv" in m:
					mfiles.append(m)
				elif "/" in m:
					mfiles.append(m)
			
			for m in mfiles:
				reqFile.write(m)
				reqFile.write("\n")
			reqFile.close() 
			
			print(mfiles)
			return mfiles
				
			
				
					
		
		
	
	
if __name__ == '__main__':
	myPyc = pyc()
	#myPyc.showCode()
	#print(myPyc.headers)
	#print(myPyc.files)
	#myPyc.macroFinder()
	myPyc.findSource()
	
