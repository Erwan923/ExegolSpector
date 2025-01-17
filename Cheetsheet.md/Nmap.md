# Nmap Cheat Sheet

### Basic Scanning Techniques
* Scan standard sans Vulners
        * `nmap -sV -sC [target]`
* Scan Vulners basique
        * `nmap -sV --script vulners [target]`
* Scan rapide avec Vulners
        * `nmap -F --script vulners [target]`
* Scan avec score CVSS minimum
        * `nmap -sV --script vulners --script-args mincvss=5.0 [target]`

### Advanced Scanning Options
* Scan Vulners Enterprise complet
        * `nmap -sV -sC --script vulners_enterprise,http-vulners-regex --script-args api_key=YD91PRTK933VDGEE3BUB3YM5BCAK57751VMJ86YPOSY3I2JFDZE4CFDVIA42CKB8 [target]`
* Scan tous ports avec Vulners
        * `nmap -p- -sV --script vulners_enterprise --script-args api_key=YD91PRTK933VDGEE3BUB3YM5BCAK57751VMJ86YPOSY3I2JFDZE4CFDVIA42CKB8 [target]`
* Scan stealth avec Vulners
        * `nmap -sS -T2 --script vulners_enterprise --script-args api_key=YD91PRTK933VDGEE3BUB3YM5BCAK57751VMJ86YPOSY3I2JFDZE4CFDVIA42CKB8 [target]`
