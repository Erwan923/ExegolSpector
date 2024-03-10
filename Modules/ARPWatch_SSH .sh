TCPDUMP_O=$(tcpdump -c 1 -i enp0s3 arp)
LIST_IP=$(echo $TCPDUMP_O| sed 's/^.*who-has //g' |sed 's/^\([0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\).*tell \([0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\).*$/\1\t\2/g')
reporting="# Scan de port sur les addresses "
open_ports=$'IP\t\tPORT\n'
for ip in $LIST_IP
do
  reporting="$reporting $ip,"
   regex="s/\(.*\)/$ip\t\1/"
  sortie_port=$(nmap -n -vv -p22 $ip | grep 'tcp open' | sed $regex)
  open_ports="$open_ports$sortie_port"
  open_ports+=$'\n'
done
echo $reporting > report.md
echo "$open_ports" >> report.md
cat report.md
