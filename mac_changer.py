#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address.")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address.")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[+] Please enter specify an interface.")
    elif not options.new_mac:
        parser.error("[+] Please enter a new MAC address.")
    return options
def change_MAC(interface, new_mac):
    print("[+] changing mac address for", interface, "to", new_mac)
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)
    # subprocess.call("ifconfig " + interface, shell=True)
def get_current_MAC(interface):
    ifconfig_result = subprocess.check_output("ifconfig " + interface, shell=True)
    mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode())
    if mac_search_result:
        return mac_search_result.group(0)
    else:
        print("[-] could not read MAC address.")

options = get_arguments()
current_MAC = get_current_MAC(options.interface)
print("Current MAC: ", current_MAC)

change_MAC(options.interface, options.new_mac)

current_MAC = get_current_MAC(options.interface)
if current_MAC == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_MAC)
else:
    print("[+] MAC address did not get changed.")
