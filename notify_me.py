import os
import configparser
import nmap

class NetworkNotification:

    def __init__(self, config_path):
        # Read the config file
        config = configparser.ConfigParser() 
        config.read(config_path)
        self.kel_mac_address = config['kelly']['mac']
        self.cam_mac_address = config['cameron']['mac']

    def monitor_kelly(self):
        
        target_mac = self.kel_mac_address 
        print("Target Mac: " + target_mac)
        





if __name__ == '__main__':
    kelly = NetworkNotification(r"E:\DevWork\Python\python-network-notificaitons\config.ini")
    kelly.monitor_kelly()