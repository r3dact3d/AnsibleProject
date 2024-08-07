#!/usr/bin/env python3

import requests
import json
import os
import sys

# DataDog API credentials from environment variables
DATADOG_API_KEY = os.getenv('DATADOG_API_KEY', 'your_datadog_api_key')
DATADOG_APP_KEY = os.getenv('DATADOG_APP_KEY', 'your_datadog_app_key')

# DataDog API endpoint
DATADOG_API_URL = 'https://api.datadoghq.com/api/v1/hosts'

def get_datadog_hosts():
    headers = {
        'DD-API-KEY': DATADOG_API_KEY,
        'DD-APPLICATION-KEY': DATADOG_APP_KEY
    }

    response = requests.get(DATADOG_API_URL, headers=headers)
    response.raise_for_status()
    
    return response.json()

def list_inventory():
    hosts_data = get_datadog_hosts()
    inventory = {'_meta': {'hostvars': {}}}
    all_hosts = []

    for host in hosts_data.get('host_list', []):
        host_name = host.get('name')
        all_hosts.append(host_name)
        inventory['_meta']['hostvars'][host_name] = {
            'datadog_tags': host.get('tags', []),
            'datadog_agent_version': host.get('agent_version', '')
        }

    inventory['all'] = {'hosts': all_hosts}
    print(json.dumps(inventory, indent=2))

def host_vars(hostname):
    hosts_data = get_datadog_hosts()
    hostvars = {}

    for host in hosts_data.get('host_list', []):
        if host.get('name') == hostname:
            hostvars = {
                'datadog_tags': host.get('tags', []),
                'datadog_agent_version': host.get('agent_version', '')
            }
            break

    print(json.dumps(hostvars, indent=2))

def verify_file(path):
    return os.path.isfile(path) and path.endswith('.py')

def main():
    if len(sys.argv) == 2 and sys.argv[1] == '--list':
        list_inventory()
    elif len(sys.argv) == 3 and sys.argv[1] == '--host':
        host_vars(sys.argv[2])
    elif len(sys.argv) == 3 and sys.argv[1] == '--verify':
        if verify_file(sys.argv[2]):
            print(json.dumps({"status": "success"}))
        else:
            print(json.dumps({"status": "failure"}))
        sys.exit(0)
    else:
        print("Usage: {} --list or --host <hostname> or --verify <path>".format(sys.argv[0]))
        sys.exit(1)

if __name__ == '__main__':
    main()
