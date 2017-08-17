import os
import json
# device = os.popen("adb reconnect").read()
# print(device)

x = os.popen("adb shell getprop").read()
# print(x)
prop_details = [{t.split(':')[0]:t.split(':')[1] for t in [i.replace('[','').replace(']','')]} for i in x.split('\n') if len(i)>1]
# print(prop_details)

json_obj = json.dumps(prop_details, indent=4)


from pprint import pprint
pprint(json_obj)