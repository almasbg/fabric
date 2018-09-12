#!/usr/bin/env python

from fabric.api import *

@env.gateway = 'username@IPofgatewayHost'

#env.hosts = ['ip', 'ip']



def ipwin_status():
        env.user = 'user'
        env.password = 'password'
        open_shell("Get-Service ipwin \n"
                   "Get-Service mongodb \n"
                   "exit \n"
                  )

def ipwin_restart():
        env.user = 'ipwinpsr'
        env.password = '1pw!nPSR'
        open_shell(
                   "Stop-Service ipwin \n"
                   "Stop-Service mongodb \n"
                   "Start-Service ipwin \n"
                   "Start-Service mongodb \n"
                   "Get-Service ipwin \n"
                   "exit \n"
                  )
