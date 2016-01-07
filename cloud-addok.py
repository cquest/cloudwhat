#!/usr/bin/env python
import os
import keystoneclient.v2_0.client as ksclient
from novaclient import client as novaclient

def get_keystone_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = os.environ['OS_TENANT_NAME']
    return d

def get_nova_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d

creds_keystone = get_keystone_creds()
creds_nova = get_nova_creds()

keystone = ksclient.Client(**creds_keystone)

nova = novaclient.Client("2", **creds_nova)
print nova.servers.list()

