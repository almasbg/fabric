#!/usr/bin/env python
from getpass import getpass
from fabric.api import *

#@env.gateway = 'username@IPofgatewayHost'

#env.hosts = ['ip', 'ip', 'ip']



def ipmon_restart():
        env.password = getpass('Enter the password for:')
        env.password = env.password
        sudo("/etc/init.d/IPmonX restart")

def ipmon_status():
        env.password = getpass('Enter the password for: ')
        env.sudo_password = env.password
        sudo('sudo /etc/init.d/IPmonX status')

def ipmon_disk():
        #env.user = 'user'
        #env.password = 'password'      
        env.password = getpass('Enter the password for: ')
        env.sudo_password = env.password
        sudo("find /apps/IPsoft/IPmon/var -type f -not -name '*.gz' -name '*log*' -name '*201*' -exec gzip -9v {} \;")
        sudo("find /apps/IPsoft/IPmon/var -type f -not -name '*.gz' -name '*service-perfdata*201*' -exec gzip -9v {} \;")
