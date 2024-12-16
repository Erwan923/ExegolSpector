# OWASP Testing Guide Integration

## Information Gathering
- Web Technology Detection
  ```bash
  whatweb {target}
  wappalyzer-cli {target}
  ```
- Subdomain Enumeration
  ```bash
  subfinder -d {domain}
  amass enum -d {domain}
  ```

## Authentication Testing
- Brute Force
  ```bash
  hydra -L users.txt -P pass.txt {target} http-post-form
  ```
- Session Management
  ```bash
  burpsuite -> scanner -> session handling
  ```

## Authorization
- IDOR Testing
  ```bash
  # Script Python de test d'IDOR
  for id in range(1000):
    curl -H "Cookie: session={token}" {target}/api/user/{id}
  ```
- Access Control
  ```bash
  # Test des points d'accès sensibles
  curl -X POST -H "Role: admin" {target}/admin/
  ```

## Input Validation
- XSS Detection
  ```bash
  xsser --url {target}
  ```
- SQLi Testing
  ```bash
  sqlmap -u {target} --forms --batch
  ```

## Error Handling
- Fuzzing
  ```bash
  wfuzz -c -z file,wordlist.txt {target}
  ```
- Error Message Analysis
  ```bash
  nuclei -u {target} -t exposures/
  ```

## Cryptography
- TLS Testing
  ```bash
  sslyze --regular {target}
  testssl.sh {target}
  ```
- Weak Cipher Detection
  ```bash
  nmap --script ssl-enum-ciphers -p 443 {target}
  ```