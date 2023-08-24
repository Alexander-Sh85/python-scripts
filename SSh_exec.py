import paramiko, sys

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=sys.argv[1], username=sys.argv[2], password=sys.argv[3])

commands = [
    'echo "Hello, world!"',
    'ls -l',
]

for command in commands:
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.read().decode())

ssh.close()