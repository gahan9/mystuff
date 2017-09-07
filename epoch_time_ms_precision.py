import time
from datetime import datetime

x = 1
while x<11:
	t = time.time()
	print("{})	Epoch Time : {}   |||||   datetime : {}".format(x, t, datetime.fromtimestamp(t)))
	time.sleep(1)
	x+=1