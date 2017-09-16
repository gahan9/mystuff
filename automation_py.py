__author__ = "Gahan Saraiya"

__info__ = "Windows Automation for xbmc-rebranding"

import os
import re
import shutil
from pprint import pprint
from datetime import datetime

# Constants
DEFAULT_ROOT_DIR = "D:\\"
DEFAULT_BUILD_FOLDER_NAME = "Build_17.4"
DEFAULT_VERSION_FILE = "version.txt"
NEW_BUILD_ZIP = "Build_17.4-minimal.zip"
SKINS = r"Project\SKINS"
BUILD_DIR = "project\\Win32BuildSetup"


def unzip(_in=os.path.join(DEFAULT_ROOT_DIR, NEW_BUILD_ZIP), _out=DEFAULT_ROOT_DIR):
	confirm = input("Do you want to proceed extraction process? (Y/N) [N]: ")
	if confirm == "y":
		import zipfile
		import sys
		check_path = os.path.join(DEFAULT_ROOT_DIR, DEFAULT_BUILD_FOLDER_NAME)
		if os.path.exists(check_path):
			print("The path you are creating is already exist.")
			return False
		else:
			__in = zipfile.ZipFile(_in, 'r')
			nofiles = len(__in.infolist())
			print("Extracting {} files".format(nofiles))
			progress_part = int(nofiles / 20)
			count   = 0
			print("Extracting", end="")
			for item in __in.infolist():
				count += 1
				update = int((count / nofiles) * 100)
				if count % progress_part == 0:
					print(".", sep=' ', end='', flush=True)
				# __in.extract(item, _out)
			print("Extraction process completed successfully.")
			return True
	else:
		return False


class WindowsAutomation(object):
	""" Windows Automation for xbmc-rebranding """
	def __init__(self, working_directory=None):
		if not working_directory:
			working_directory = DEFAULT_ROOT_DIR
		else:
			DEFAULT_ROOT_DIR = working_directory
		super(WindowsAutomation, self).__init__()
		print("> Initializing Service... at {0}\n".format(working_directory))
		self.root_directory = DEFAULT_ROOT_DIR
		self.working_directory = os.path.join(DEFAULT_ROOT_DIR, DEFAULT_BUILD_FOLDER_NAME)
		self.version_path = os.path.join(self.working_directory, DEFAULT_VERSION_FILE)
		self.existing_build_details = self.get_existing_info()
		self.build_directory = os.path.join(self.working_directory, BUILD_DIR)
		self.skin_choice_directory = os.path.join(DEFAULT_ROOT_DIR, SKINS)
		self.main_make_file = os.path.join(self.working_directory, "Makefile.in")
		self.configure_file = os.path.join(self.working_directory, "configure.ac")
		print("Current Working Directory: {0} \nversion file path: {1}\n".format(self.working_directory, self.version_path))


	def get_existing_info(self, version_file=None):
		existing_build_details = {}
		if not version_file:
			version_file = self.version_path
		if os.path.exists(version_file):
			print(">>reading file: {0}".format(version_file))
			with open(version_file, "r") as version_pointer:
				version_detail = version_pointer.read()
			existing_build_details["name"] = re.search("APP_NAME (\w+)", version_detail).group(1)
			existing_build_details["company_name"] = re.search("COMPANY_NAME ([A-Za-z\-]+)", version_detail).group(1)
			existing_build_details["website"] = re.search("WEBSITE ([A-Za-z\-.\/:]+)", version_detail).group(1)
			existing_build_details["version"] = re.search("VERSION_MAJOR (\d+)", version_detail).group(1)
			existing_build_details["version_minor"] = re.search("VERSION_MINOR (\d+)", version_detail).group(1)
			existing_build_details["version_code"] = re.search("VERSION_CODE (\d+)", version_detail).group(1)
			existing_build_details["api"] = re.search("ADDON_API (\d.+)", version_detail).group(1)
			print(">>Details of current build: {}\n".format(existing_build_details))
			return existing_build_details
		else:
			print(">>Directory of existing build not exist")
			return False


	def change_version_detail(self, raw, new_version_detail=None):
		name = "APP_NAME " + new_version_detail["name"]
		raw = re.sub("APP_NAME (\w+)", name, raw)
		company_name = "COMPANY_NAME " + new_version_detail["company_name"]
		raw = re.sub("COMPANY_NAME ([A-Za-z\-]+)", company_name, raw)
		website = "WEBSITE " + new_version_detail["website"]
		raw = re.sub("WEBSITE ([A-Za-z\-.\/:]+)", website, raw)
		print(">>Details of build with changes: {}\n".format(raw))
		with open(self.version_path, "w") as version_writer:
			version_writer.write(raw)
		return True


	def backup_existing_build(self, build_details=None):
		if not build_details:
			build_details = self.existing_build_details
		if build_details["name"].lower() != "kodi":
			print("Backing up existing build..")
			new_name = "build_" + build_details["name"].lower()
			new_path = os.path.join(DEFAULT_ROOT_DIR, new_name)
			print("storing build with name: {}".format(new_name))
			os.rename(self.working_directory, new_path)
			print("Build directory of {} is renamed to {} at {}".format(build_details["name"], new_name, new_path))


	def select_existing_build_rename(self, build_details=None):
		new_name = build_details[0].lower()
		new_path = os.path.join(DEFAULT_ROOT_DIR, new_name)
		print("storing build with name: {}".format(new_name))
		os.rename(build_details[1], self.working_directory)
		print("Build directory of {} is renamed to {} at {}".format(build_details[0], new_name, self.working_directory))
		return True


	def get_new_details(self, current_build_details=None):
		new_details = {}
		if not current_build_details:
			current_build_details = self.existing_build_details
		new_details = current_build_details
		print("you need to apply some new details..")
		name = input("Name for product (alphabets only) [{}]: ".format(current_build_details["name"]))
		if name:
			new_details["name"] = name
		site = input("product website [{}]: ".format(current_build_details["website"]))
		if site:
			new_details["website"] = site
		company = input("Company Name [{}]: ".format(current_build_details["company_name"]))
		if company:
			new_details["company_name"] = company
		print("New build details are: {}".format(new_details))
		return new_details


	def get_available_choice(self, flag=0):
		if flag==0:
			# return list of available builds
			no_of_dirs = [x for x in os.listdir() if x.startswith("b")]
			print("Available build choices are:")
			total_alternate_existing_choices = []
			for available_choices in range(len(no_of_dirs)):
				build_title = no_of_dirs[available_choices].replace("build_","").title()
				location = os.path.join(os.getcwd(), no_of_dirs[available_choices])
				total_alternate_existing_choices.append((available_choices+1, build_title, location))
				print("{}. {} (located at: {})".format(available_choices+1, build_title, location))
			return total_alternate_existing_choices
		elif flag==1:
			# returns possible elements to update
			choice = input("Are you sure you want to create new build?(y/n) [y]: ")
			# choice = "y"
			if choice.lower() == "y" or choice == "":
				current_build_details = self.get_existing_info()
				if not current_build_details:
					print("current build details not found!")
					self.prompt_choice(flag="new_build")
				else:
					self.backup_existing_build(current_build_details)
					self.prompt_choice(flag="new_build")


	def prompt_choice(self, choice="y", message=" [Y]: ", flag="build"):
		if flag=="build":
			if choice == "y":
				result = self.get_available_choice(flag=0)  # [(1, 'Wizetv', 'D:\\build_wizetv'), (2, 'B1', 'path')]
				mod_result = {x[0]:x[1:] for x in result}  # {1: ('Wizetv', 'D:\\build_wizetv'), 2: ('B1', 'path')}
				try:
					build_choice = int(input(message))
					if build_choice in mod_result:
						print("You have selected {} build to create from {}".format(build_choice, result))
						self.apply_modification(product_detail=mod_result[build_choice], flag="old")
					else:
						print("Invalid input..")
				except ValueError:
					print("Invalid input")
		elif flag == "new_build":
			new_build_zip = os.path.join(DEFAULT_ROOT_DIR, NEW_BUILD_ZIP)
			print("Zip Location: {}".format(new_build_zip))
			zip_extraction_result = unzip(new_build_zip)
			if zip_extraction_result:
				print("Zip Extraction completed")
			if os.path.exists(self.version_path) and self.existing_build_details["name"].lower()=="kodi":
				new_details = self.get_new_details(self.existing_build_details)
				self.apply_modification(new_details, flag="new")


	def apply_modification(self, product_detail, flag="new"):
		if flag == "old":
			print("Preparing to build {}...\n build located at : {}".format(product_detail[0], product_detail[1]))
			confirm = input("Do you want to proceed? (Y/N) [Y]:")
			if confirm == "y" or confirm == "":
				if os.path.exists(self.working_directory):
					self.backup_existing_build(self.get_existing_info(version_file=os.path.join(product_detail[1], "version.txt")))
				rename_status = self.select_existing_build_rename(product_detail)
				if rename_status:
					os.chdir(self.build_directory)
					print(os.getcwd())
					self.run_build(command="nomingwlibs noclean nobinaryaddons")
			else:
				print("Bye!!")
		elif flag == "new":
			with open(self.version_path, "r") as f:
				version_detail = f.read()
			self.change_version_detail(raw=version_detail, new_version_detail=product_detail)
			skin_choices = [skin for skin in os.listdir(self.skin_choice_directory) if skin.startswith("skin.")]
			for skins in skin_choices:
				print("{}. {}".format(skin_choices.index(skins)+1, skins))
			skin_choice = int(input("select skin for build [skin.estuary] :"))
			new_skin = skin_choices[skin_choice-1]
			new_skin_path = os.path.join(self.skin_choice_directory, new_skin)
			print("you have selected skin {} located at {}".format(new_skin, new_skin_path))
			self.make_file_skin_changes(new_skin, new_skin_path)
			return True


	def make_file_skin_changes(self, skin, skin_path):
		with open(self.main_make_file, "r") as make_file_reader:
			content = make_file_reader.read()
		content.replace("ESTUARY_MEDIA=addons/skin.estuary/media", "ESTUARY_MEDIA=addons/{}/media".format(skin))
		if r"ESTOUCHY_MEDIA=addons/skin.estouchy/media" in content:
			content.replace(r"ESTOUCHY_MEDIA=addons/skin.estouchy/media", "")
			content.replace(r"SKIN_DIRS+=$(ESTOUCHY_MEDIA)", "")

		return True


	def run_build(self, command="nomingwlibs noclean nobinaryaddons"):
		import subprocess
		subprocess.Popen("BuildSetup.bat {}".format(command))
		dir_list = os.listdir()
		generated_file_name = [file_name for file_name in dir_list if file_name.endswith(".exe")][0]
		current_timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
		new_name = self.get_existing_info()["name"] + '_' + current_timestamp
		os.rename(generated_file_name, new_name)
		return True


if __name__ == "__main__":
	automation_object = WindowsAutomation(os.getcwd())
	choice = input("Do you want to build an existing build?(Y/N) [Y]: ")
	# choice = ""
	if choice.lower() == "y" or choice == "":
		# result = automation_object.get_available_choice(flag=0)
		automation_object.prompt_choice(choice="y", flag="build", message="Select build to create:")
	elif choice.lower() == "n":
		result = automation_object.get_available_choice(flag=1)
