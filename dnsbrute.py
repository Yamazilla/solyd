import dns.resolver

resolver = dns.resolver.Resolver()

domain = input("Target addres: ")
domain = str(domain)
wordlist = input("Wordlist or filepath: ")
wordlist = str(wordlist)

with open(wordlist, "r") as file:	
	for subdomain in file:
		try:
			sub_target = f"{subdomain}.{domain.strip()}"
			results = resolver.resolve(sub_target, "A")
			for result in results:
				print(f"{sub_target} -> {result}")
		except:
			pass