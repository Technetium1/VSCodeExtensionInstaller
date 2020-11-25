# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://github.com/Technetium1
# Licensed under The Unlicense [unlicense.org]

from shutil import which
from os import system
from time import sleep
import urllib3
import certifi

version = "1.0"
print("https://github.com/Technetium1/VSCodeExtensionInstaller\nVersion " + version + "\n")

if which("code") is None:
    print("VSCode was not found in path, try reinstalling it!")
    sleep(5)
    raise SystemExit

if which("./VSCodeExtensions.txt") is None:
    print("VSCodeExtensions.txt was not found!\nDownloading the latest from Github!\n")
    sleep(2)
    extensions_url = "https://raw.githubusercontent.com/Technetium1/VSCodeExtensionInstaller/master/VSCodeExtensions.txt"
    http = urllib3.PoolManager(ca_certs=certifi.where())
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    r = http.request(
        "GET",
        extensions_url,
        timeout=urllib3.Timeout(connect=15.0, read=15.0),
        retries=4,
        redirect=False)
    with open("VSCodeExtensions.txt", "wb") as vscodeextensions:
        vscodeextensions.write(r.data)
    print("Done!\nEdit VSCodeExtensions.txt and restart to install all the packages!")
    sleep(6)
    raise SystemExit

with open("VSCodeExtensions.txt", "r") as file:
    extensions = file.readlines()

for extension in extensions:
    print("Installing " + extension)
    system("code --install-extension " + extension)
    print()
