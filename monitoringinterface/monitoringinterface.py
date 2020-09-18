from netmiko import ConnectHandler


host = input('Enter the Device IP: ')
username = input('Username: ')
password = input('Password: ')


cisco = {
   'device_type' : 'cisco_ios', #different vendor has difference device type check "https://pynet.twb-tech.com/blog/automation/netmiko.html" for reference
   'host' : f'{host}',
   'username' : f'{username}',
   'password' : f'{password}'
}

net_connect = ConnectHandler(**cisco)
while True:
   output = net_connect.send_command('show interfaces gigabitEthernet 0/1')#change the interface base on your needs
   if ("down") in output:
      print('\n')
      print('Port status down detected, Enabling now')
      output1 = net_connect.send_config_set(['interface gigabitEthernet 0/1', 'no shutdown']) #bounce the port once detected down or shutdown
  else:
      print('Monitoring Port')
