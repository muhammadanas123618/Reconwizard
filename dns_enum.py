import dns.resolver

def run(domain):
   records = {}
   types = {'A' , 'MX' , 'TXT' , 'NS' }
   for rtype in types:
       try:
           answers = dns.resolver.resolve(domain,rtype,lifetime=5)
           records[rtype]=[str(r) for r in answers ]
       except Exception:
           records[rtype]=[]
   return records     
