import sys
from censys.search import CensysHosts




    
UID = "3bfaaf39-f657-4796-9931-51cd2cab7845"
SECRET = "gL4RIv7dLEMZ5989Z3VmcEvmYAEGvSWP" 

    
censys = CensysHosts(UID, SECRET)
shadow_it = []
results = censys.search("ncsu.edu", per_page=100, pages=10)
for result in results:
    for i in range(len(result)):
        if result[i]['autonomous_system']['asn'] != 11442:
            if 'dns' in result[i] and "ncsu.edu" in result[i]['dns']['reverse_dns']['names'][0]:
                print( result[i]['dns']['reverse_dns']['names'][0] + "  "+ result[i]['ip'])
            
