import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('remote_host', username='user', password='password')

commands = [
    'echo "Hello, world!"',
    'ls -l',
]

for command in commands:
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.read().decode())

ssh.close()