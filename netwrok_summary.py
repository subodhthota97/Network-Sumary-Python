import sys
import requests
import plotly.graph_objects as go
from censys.search import CensysHosts
from collections import Counter




def plot_g(hosts, search, field):
    search_results = hosts.aggregate(search, field, num_buckets = 1000)
    data = search_results["buckets"]

    type = {"operating_system.product" : "Operating systems", "services.software.product": "Web servers", "services.service_name": "Protocols"}

    x = [item['key'] for item in data]
    y = [item['count'] for item in data]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=x, y=y))
    fig.update_layout(title=f"{search} - {type[field]}")
    fig.show()
    
UID = "3bfaaf39-f657-4796-9931-51cd2cab7845"
SECRET = "gL4RIv7dLEMZ5989Z3VmcEvmYAEGvSWP" 

    
censys = CensysHosts(UID, SECRET)

hosts = ["152.1.0.0/16", "152.14.0.0/16", "152.7.0.0/16"]
fields = ["operating_system.product", "services.software.product", "services.service_name"]

for field in fields:
    for host in hosts:
        plot_g(censys, host, field)
