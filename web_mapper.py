import queuelib
import threading
import os
import urllib3

target = "http://www.tryhackme.com"
filters = [".jpg",".gif","png",".css"]

os.chdir(os.getcwd())


