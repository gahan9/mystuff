import os
import shutil
from bs4 import BeautifulSoup
ls = []
os.chdir(r"E:\XBMCprojects\update\addons")
for i in os.listdir():
	file = os.path.join(str(i),"addon.xml")
	with open(file, 'r') as f:
		try:
			f_content = f.read()
			a = BeautifulSoup(f_content, "html.parser")
			name = a.find("addon").get("id")
			version = a.find("addon").get("version")
			single_detail = "{}   -   {}".format(name, version)
			print(single_detail)
			ls.append(single_detail)
		except UnicodeDecodeError:
			pass
			
os.chdir(r"E:\XBMCprojects\update")
with open("addon_detail.txt", 'w') as fpw:
	for cont in ls:
		fpw.write(cont)
		fpw.write("\n")