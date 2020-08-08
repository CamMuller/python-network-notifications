import os
import configparser
import nmap
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class NetworkNotification:

    def __init__(self, config_path):
        # Read the config file
        config = configparser.ConfigParser() 
        config.read(config_path)
        self.kel_mac_address = config['kelly']['mac']
        self.from_email = config['kelly']['from_email']
        self.notify_email = config['kelly']['notify_email']
        self.smtp = config['kelly']['smtp']
        self.port = config['kelly']['port']
        self.app_password = config['kelly']['app_password']

    def send_mail(self):

        # Configure SMTP server
        s = smtplib.SMTP(host=self.smtp, port=int(self.port))
        s.starttls()
        s.login(self.notify_email,self.app_password)
        
        # Message method
        msg = MIMEMultipart()

        # Create the message
        message = 'Hi Cam,\nKel is home safely!'

        # Message context
        msg['From']=self.from_email
        msg['To']=self.notify_email
        msg['Subject']="Kel is Home"
            
        # Message body
        msg.attach(MIMEText(message, 'plain'))
        s.send_message(msg)
        del msg
            
        # Terminate the SMTP session
        s.quit()

    def monitor_kelly(self):
    
        target_mac = self.kel_mac_address 
        print("Target Mac: " + target_mac)

        nm = nmap.PortScanner()
        nm.scan(hosts='192.168.0.0/24', arguments='-sP')

        host_list = nm.all_hosts()
        print(host_list)
        for host in host_list:
            if 'mac' in nm[host]['addresses']:
                print(host+' : '+nm[host]['addresses']['mac'])
                if target_mac == nm[host]['addresses']['mac']:
                    print('Target Found')
                    self.send_mail()
                    print('Email Sent!')

if __name__ == '__main__':
    kelly = NetworkNotification('YOUR CONFIG FILE PATH')
    kelly.monitor_kelly()