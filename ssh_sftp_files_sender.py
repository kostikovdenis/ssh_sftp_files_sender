import os
import paramiko # установить командой 'pip install paramiko'

localpath = r'C:\Users\DKostikov\Desktop\drafts'
remotepath = r'/home/dkostikov/crm_receiver_separation_test/' # для Linux в конце пути должен быть '/'
extention = '.jar'
host = '****.**.*****' # имя либо IP-адрес удаленного хоста
port = 22 # порт для SSH по умолчанию: 22
username = '****'
password = '*******'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

sftp = ssh.open_sftp()

files = os.listdir(localpath)

for file in files:
    if file.endswith(extention):
          print('Отправка: "' + file + '"')
          sftp.put(os.path.join(localpath, file), remotepath + file)
          print('Файл "' + file + '" отправлен')
    else:
        print('Файл "' + file + '" пропущен')

sftp.close() 
ssh.close()
print('Завершено')
