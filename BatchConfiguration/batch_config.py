IP_LIST = open('switch_ip.txt')
for IP in IP_LIST:
    RTR = {
        'device_type': 'cisco_ios',
        'ip':   IP,
        'username': 'admin',
        'password': 'admin',
    }

    print ('\nConnecting to the Switch ' + IP.strip() + ' \n')
    try:
        net_connect = ConnectHandler(**RTR)
    except NetMikoTimeoutException:
        print ('Device not reachable' )
        continue

    except NetMikoAuthenticationException:
        print ('Authentication Failure' )
        continue

    except SSHException:
        print ('Make sure SSH is enabled' )
        continue

    output = net_connect.send_config_from_file(config_file='config.cfg')
    print(output)

    print('\n Saving the Switch configuration \n')
    output = net_connect.save_config()
    print(output)

    output = net_connect.send_command('show ip route')
    print(output)
