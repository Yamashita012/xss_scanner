#!/usr/bin/env python3

import requests
import sys


target_url = sys.argv[1]
payload_path = sys.argv[2]

def payLoad():
    with open(payload_path,'r') as payload_file:
        xss_line = payload_file.readlines()
        for xss in xss_line:
            sent_xss_request = requests.get(target_url + xss)
            if xss in sent_xss_request.text:
                print("XSS Found")
                print(f"[+] Successful Payload: {xss}")
                break
            else:
                print(f"[-] {xss}: Secure")


payLoad()
