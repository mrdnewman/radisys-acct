#!/usr/bin/env python

import requests
import os
os.system('clear')

get_web = requests.get("http://www.hipstercode.com")
print(get_web)
