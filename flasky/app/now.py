from ssh import ssh

connection = ssh("arc2.leeds.ac.uk", "uitjr", "")
answer = connection.sendCommand('qstat -u "*"')

for line in answer:
    print (answer.split())
