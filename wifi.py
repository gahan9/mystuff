import re
import os
import json
from pprint import pprint
from subprocess import check_output

ALL_NETWORKS = {}

def scan_networks():
	available_networks = os.popen("netsh wlan show networks mode=bssid").read().strip()
	network_list = available_networks.split("\nSSID")[1:]
	ALL_NETWORKS["total_available_networks"] = len(network_list)
	ALL_NETWORKS["network_detail"] = []
	# pprint(network_list)
	for netowrks in network_list:
		network_dict = {}
		try:
			# x = re.search("( *)\d( *):( *)(.*)", netowrks, re.DOTALL).group(4)
			ssid = re.search("( *)\d( *):( *)([a-zA-Z0-9-~!@#$%^&*()_+=/* ]+)", netowrks, re.DOTALL).group(4)
			# # ssid = re.search(r"( *)\d( *):( *)(.*)", network_list[0], re.DOTALL).group(4)
			authentication = re.search("( *)Authentication( *):( *)([a-zA-Z0-9-. ]+)", netowrks, re.DOTALL).group(4)
			encryption = re.search("( *)Encryption( *):( *)([a-zA-Z0-9-. ]+)", netowrks, re.DOTALL).group(4)
			signal_strength = re.search("( *)Signal( *):( *)([a-zA-Z0-9-%. ]+)", netowrks, re.DOTALL).group(4)
			# pprint("{}, {}, {}, {}".format(ssid.strip(), authentication.strip(), encryption.strip(), signal_strength.strip()))
			network_dict["ssid"] = ssid.strip()
			network_dict["authentication"] = authentication.strip()
			network_dict["encryption"] = encryption.strip()
			network_dict["signal_strength"] = signal_strength.strip()
			ALL_NETWORKS["network_detail"].append(network_dict) 
		except:
			print("Network issue or hidden network")
	net_obj = json.dumps(ALL_NETWORKS, indent=4)
	pprint(net_obj)


def connect_network(network_details):
	ssid = network_details['ssid']
	status = check_output('netsh wlan connect "{}"'.format(ssid), shell=True)
	print(status)

def disconnect_network():
	status = check_output('netsh wlan disconnect', shell=True)
	print(status)


if __name__ == "__main__":
	scan_networks()
	pprint(ALL_NETWORKS)
	connect_network(network_details=ALL_NETWORKS['network_detail'][0])