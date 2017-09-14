def unzip(_in=os.path.join(DEFAULT_ROOT_DIR, NEW_BUILD_ZIP), _out=DEFAULT_ROOT_DIR):
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
			__in.extract(item, _out)
		print("Extraction process completed successfully.")
		return True

