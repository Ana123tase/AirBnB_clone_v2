#!/usr/bin/python3
""" Function that deploys """
from fabric.api import *


env.hosts = ['44.210.150.159', '35.173.47.15']
env.user = "ubuntu"


def do_clean(number=0):
    """ CLEANS """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1
