import os

condition_success = 0 # set initial 0 
while True:
	condition_success += 1 # get counter for condition to increment if condition is true:
	# By default this will create folder within same directory
	os.makedirs("folder"+str(condition_success)) # creates folder1 if condition_success is 1
	# to create directory somewhere else set path to it
	path = "/path/"
	os.makedirs(path + "folder"+str(condition_success))
	# or you can directly create it as 
	os.makedirs("/path/folder"+str(condition_success))


# if you want that condition within sub condition you can use if statement to execute it or to break your condition to prevent infinite loop
condition_success = 0
usr_input = int(input("Enter number to create number of folder/execute condition: ")) # get number from user input
while True:
	condition_success += 1 # get counter for condition to increment if condition is true:
	# By default this will create folder within same directory
	os.makedirs("folder"+str(condition_success)) # creates folder1 if condition_success is 1
	# to create directory somewhere else set path to it
	path = "/path/"
	os.makedirs(path + "folder"+str(condition_success))
	# or you can directly create it as 
	os.makedirs("/path/folder"+str(condition_success))
	if condition_success >= usr_input:
		break

