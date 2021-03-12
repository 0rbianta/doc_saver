import os
import shutil
import time
import datetime

global_lens = []
check_time = 1

def main():
	print("Welcome to 0rbianta's document saver.")
	while 1:
		check_and_save()
		time.sleep(check_time)


def check_and_save():
	for file in list_files():
		if(file == get_file_name):	continue
		for save_d in global_lens:
			if(file == save_d.file):
				if(save_d.len != os.path.getsize(file)):
					print("SAVED: "+str(datetime.datetime.now()))
					cas(file)
					update_save(file)
					
		if(check_save_exist(file) == False):
			psave = save(file, os.path.getsize(file))
			global_lens.append(psave)

def update_save(filename):
	for save in global_lens:
		if(save.file == filename):
			save.len = os.path.getsize(filename)

def check_save_exist(filename):
	for save in global_lens:
		if(filename == save.file):	return True
	return False

def cas(filename):
	try:
		os.mkdir("bckup")
	except:
		None
	
	shutil.copyfile(filename, "bckup/"+filename+"DATE::"+str(datetime.date.today())+"TIME::"+str(datetime.datetime.now()))


def list_files():
	build = []
	for f_or_dir in os.listdir():
		if(os.path.isfile(f_or_dir)):
			build.append(f_or_dir)
	return build

def get_file_name():
	return __file__

class save:
	def __init__(self, filename, len):
		self.file = filename
		self.len = len


if(__name__ == "__main__"):
	main()

