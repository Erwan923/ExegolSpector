Netcat Cheat Sheet
Netcat, also known as the "Swiss army knife" of networking, is a versatile tool for networking debugging, exploration, and scripting. It allows for arbitrary TCP and UDP connections and listens.

Usage and Syntax
The normal syntax for Netcat is as follows:

css
Copy code
nc [options] [host] [port]
This command establishes arbitrary TCP and UDP connections and listens.

General Options
IPv4 Only: nc -4 [options] [host] [port] - Use IPv4 addressing only.
IPv6 Only: nc -6 [options] [host] [port] - Use IPv6 addressing only.
UDP Mode: nc -u [options] [host] [port] - Use UDP instead of TCP.
Listening Mode: nc -l [host] [port] - Listen for an incoming connection.
Keep Listening: nc -k -l [host] [port] - Continue listening after the client has disconnected.
No DNS Lookups: nc -n [host] [port] - Perform no DNS lookups.
Specific Source Port: nc -p [source port] [host] [port] - Use a specific source port.
Specify Source IP: nc -s [source ip] [host] [port] - Specify the source IP address.
Timeout: nc -w [timeout] [host] [port] - Apply 'n' second timeout.
Verbose Output: nc -v [host] [port] - Enable verbose output.
Client Examples
Transmit File: nc 192.168.0.1 5051 < filename.in - Transmit contents of file "filename.in".
Receive Data to File: nc 192.168.0.1 5051 > filename.out - Send incoming data to "filename.out".
Server Examples
TCP Listen: netcat -l 5050 - Listen for TCP connections on port 5050. Data received is printed to STDOUT.
Receive Data to File: netcat -l 5051 > filename.out - Direct incoming data to "filename.out".
Web Server Example
Single Use Web Server: Listening on port 8080:
swift
Copy code
( echo -ne "HTTP/1.1 200 OK\nContent-Length: $(wc -c <index.html)\r\n\r\n"; cat index.html ) | nc -l 8080
Persistent Web Server:
Using a Bash while loop to restart the web server after each request:
swift
Copy code
while : ; do ( echo -ne "HTTP/1.1 200 OK\r\nContent-Length: $(wc -c <index.html)\r\n\r\n"; cat index.html; ) | nc -l -p 8080 ; done
Simple Proxy
css
Copy code
mknod backpipe p ; nc -l [proxy port] < backpipe | nc [destination host] [destination port] > backpipe
Create a named pipe ("backpipe"), setup a listener on proxy port, and forward requests to the destination host. The client redirects the response from the destination host into the named pipe, allowing for bi-directional data transmission.

Port Scanning
Single TCP Port: nc -zv hostname.com 80 - Scan a single TCP port.
Range of Ports: nc -zv hostname.com 80-84 - Scan a range of ports.
Multiple Specific Ports: nc -zv hostname.com 80 84 - Scan multiple specified TCP ports.
Netcat's flexibility and wide range of options make it an indispensable tool for anyone involved in networking.


