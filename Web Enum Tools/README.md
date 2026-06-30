# autorecon.sh

**1. Subdomain Discovery (assetfinder & amass):** Combines passive scraping and active OSINT techniques to map out the target's entire public infrastructure and discover hidden subdomains.

**2. Live Host Verification (httprobe):** Filters the massive list of subdomains to identify which servers are actually alive and accepting HTTP/HTTPS traffic.

**3. Takeover Detection (subjack):** Scans the live subdomains for broken or dangling DNS records pointing to unclaimed cloud services (detecting easy Subdomain Takeover vulnerabilities).

**4. Port Scanning (nmap):** Probes the verified infrastructure to discover open ports, running network services, and potential entry points.

**5. URL Harvesting (waybackurls):** Mines historical internet archives to extract old URLs, parameters, and forgotten endpoints belonging to the target.

**6. Visual Auditing (eyewitness):** Automatically takes screenshots of all discovered web pages and organizes them into a clean HTML report for quick visual triage.
