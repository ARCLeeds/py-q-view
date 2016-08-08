from ssh import ssh

connection = ssh("arc2.leeds.ac.uk", "uitjr", "Jaydee3148")
answer = connection.sendCommand('qstat -u "*"')
    
for line in answer:
    print (answer.split())
   
