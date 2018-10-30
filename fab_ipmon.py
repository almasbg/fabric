#!/usr/bin/env python
from getpass import getpass
from fabric.api import *
import sys
import os
#@env.gateway = 'username@IPofgatewayHost'


env.password = getpass('Enter the password for: ')
env.sudo_password = env.password
list = []

print(file)
# file function needs to be added before execution any other tasks for multiple host list in file hosts
# how to use this script: fab -f fab_ipmon_dev.py file:name=hosts ipmon_status
def file(**kwargs):
        for key, value in kwargs.iteritems():
                hosts = value
        with open(hosts, "r") as file:
                for line in file:
                        list.append(line)
                env.hosts = list;

def ipmonx_restart():
        sudo("/etc/init.d/IPmonX restart")

def ipmon_restart():
        sudo('/etc/init.d/IPmon restart')

def ipmon_disk():
        #env.user = 'user'
        #env.password = 'password'      
        sudo("find /apps/IPsoft/IPmon/var -type f -not -name '*.gz' -name '*log*' -name '*201*' -exec gzip -9v {} \;")
        sudo("find /apps/IPsoft/IPmon/var -type f -not -name '*.gz' -name '*service-perfdata*201*' -exec gzip -9v {} \;")
        sudo("find /apps/IPsoft/IPmon/engine/jmx/log/jmx1.2/ -type f -not -name '*.gz' -name 'engine.log.201*' -exec gzip -9v {} \;")
