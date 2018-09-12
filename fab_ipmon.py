#!/usr/bin/env python

from fabric.api import *

#@env.gateway = 'username@IPofgatewayHost'

#env.hosts = ['ip', 'ip']



def ipmon_restart():
        env.user = 'user'
        env.password = 'password'
        run("for i in apache-activemq IPmon IPmonX IPmon-engine-jmx IPmon-engine-ipt IPdiscover IPadmin IP2date IPreports-client ipremote ipmonstatus; do /etc/init.d/$
i status;done")
