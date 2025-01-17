# Nmap Cheat Sheet

### Basic Scanning Techniques
* Scan Agressif
       * `nmap -A [target]`
* Scan with scripts and version detection
       * `nmap -sC -sV [target]`
* Scan Vulners basique
       * `nmap -sV --script vulners [target]`
* Scan Vulners avec CVSS
       * `nmap -sV --script vulners --script-args mincvss=5.0 [target]`

### Advanced Scanning Techniques 
* Scan Vulners complet avec API
       * `nmap -sV -sC --script vulners_enterprise,http-vulners-regex --script-args api_key=[API_KEY] [target]`
* Scan Vulners Enterprise tous ports
       * `nmap -sV -p- --script vulners_enterprise --script-args api_key=[API_KEY] [target]`
* Scan HTTP avec détection vulnérabilités
       * `nmap -sV --script "http-* and vuln" [target]`

### Discovery Options
* Perform a ping scan only
       * `nmap -sP [target]`
* Don't ping
       * `nmap -PN [target]`
* TCP SYN Ping
       * `nmap -PS [target]`
* TCP ACK ping
       * `nmap -PA [target]`
* UDP ping
       * `nmap -PU [target]`
* SCTP Init Ping
       * `nmap -PY [target]`
* ICMP echo ping
       * `nmap -PE [target]`
* ICMP Timestamp ping
       * `nmap -PP [target]`
* ICMP address mask ping
       * `nmap -PM [target]`
* IP protocol ping
       * `nmap -PO [target]`
* ARP ping
       * `nmap -PR [target]`
* Traceroute
       * `nmap --traceroute [target]`
* Force reverse DNS resolution
       * `nmap -R [target]`
* Disable reverse DNS resolution
       * `nmap -n [target]`
* Alternative DNS lookup
       * `nmap --system-dns [target]`
* Manually specify DNS servers
       * `nmap --dns-servers [servers] [target]`
* Create a host list
       * `nmap -sL [targets]`

### Advanced Scanning Options
* TCP SYN Scan
       * `nmap -sS [target]`
* TCP connect scan
       * `nmap -sT [target]`
* UDP scan
       * `nmap -sU [target]`
* TCP Null scan
       * `nmap -sN [target]`
* TCP Fin scan
       * `nmap -sF [target]`
* Xmas scan
       * `nmap -sX [target]`
* TCP ACK scan
       * `nmap -sA [target]`
* Custom TCP scan
       * `nmap --scanflags [flags] [target]`
* IP protocol scan
       * `nmap -sO [target]`
* Send Raw Ethernet packets
       * `nmap --send-eth [target]`
* Send IP packets
       * `nmap --send-ip [target]`
