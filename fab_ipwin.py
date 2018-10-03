#!/usr/bin/env python
from getpass import getpass, getuser
from fabric.api import *
import sys
import os
#@env.gateway = 'username@IPofgatewayHost'

#env.user = getuser('Enter username: ')
env.user = prompt("Enter ipwin username:  ", default="ipwin")
env.password = getpass('Enter the password: ')
#env.sudo_password = env.password
list = []

# file function needs to be added before execution any other tasks for multiple host list in file hosts
# how to use this script: fab -f fab_ipmon_dev.py file:name=hosts ipmon_status
def file(**kwargs):
        for key, value in kwargs.iteritems():
                hosts = value
        with open(hosts, "r") as file:
                for line in file:
                        list.append(line)
                env.hosts = list;




def ipwin_status():
        env.user = 'user'
        env.password = 'password'
        open_shell("Get-Service ipwin \n"
                   "Get-Service mongodb \n"
                   "exit \n"
                  )

def ipwin_restart():
        env.user = 'user'
        env.password = 'password'
        open_shell(
                   "Stop-Service ipwin \n"
                   "Stop-Service mongodb \n"
                   "Start-Service ipwin \n"
                   "Start-Service mongodb \n"
                   "Get-Service ipwin \n"
                   "exit \n"
                  )
