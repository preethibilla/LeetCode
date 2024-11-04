class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # Initialize a dictionary to store the visit counts for each subdomain
        counts = defaultdict(int)
        
        # Process each entry in cpdomains
        for entry in cpdomains:
            # Split the entry into count and domain
            count, domain = entry.split()
            count = int(count)  # Convert count to an integer
            
            # Split the domain into its parts
            fragments = domain.split('.')
            
            # Generate subdomains and add the count to each one
            for i in range(len(fragments)):
                subdomain = '.'.join(fragments[i:])
                counts[subdomain] += count
        
        # Format the result in the required format
        result = [f"{cnt} {dom}" for dom, cnt in counts.items()]
        return result
        