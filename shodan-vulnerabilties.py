import shodan

api_key = "CLzTVytZKBotVevMIWFQDSryjaO5buCg"
api = shodan.Shodan(api_key)


try:
    # use the host method to get information about the IP address
    host = api.host('152.14.93.106')
    print(f"IP: {host['ip_str']}")
    print(f"Organization: {host.get('org', 'n/a')}")
    print(f"Operating System: {host.get('os', 'n/a')}")
    print(f"Ports: {', '.join(str(p) for p in host['ports'])}")

    # print out information about any vulnerabilities found on the host
    if 'vulns' in host:
        print("Vulnerabilities:")
        for vuln in host['vulns']:
            print(f"\t{vuln}")
            if vuln in host["data"][0]["vulns"]:
                print(host["data"][0]["vulns"][vuln]["summary"])
    else:
        print("No vulnerabilities found.")

except shodan.APIError as e:
    print(f"Error: {e}")
