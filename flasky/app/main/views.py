from flask import render_template
from . import main
from ..ssh import ssh


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/queues/arc1')
def arc1():
    connection = ssh("arc1.leeds.ac.uk", "uitjr", "Jaydee3148")
    answer = connection.sendCommand('qstat -u "*"')
    print(answer)
    numberOfLines = len(answer.split("\n"))
    lines = answer.split("\n")
    runningJobs = []
    waitingJobs = []
    for i in range (3, numberOfLines - 1 ):
        line = lines[i].split()
        if line[4] == 'r':
            runningJobs.append(line)
        else:
            waitingJobs.append(line)

    return render_template('arc1.html', runningJobs = runningJobs,
    waitingJobs = waitingJobs)

@main.route('/queues/arc2')
def arc2():

    connection = ssh("arc2.leeds.ac.uk", "uitjr", "Jaydee3148")
    answer = connection.sendCommand('qstat -u "*"')
    numberOfLines = len(answer.split("\n"))
    lines = answer.split("\n")
    runningJobs = []
    waitingJobs = []
    for i in range (3, numberOfLines - 1 ):
        line = lines[i].split()
        if line[4] == 'r':
            runningJobs.append(line)
        else:
            waitingJobs.append(line)
    return render_template('arc2.html', runningJobs = runningJobs,
    waitingJobs = waitingJobs)

@main.route('/queues/polaris')
def polaris():

    connection = ssh("polaris.leeds.ac.uk", "uitjr", "Jaydee3148")
    answer = connection.sendCommand('qstat -u "*"')
    numberOfLines = len(answer.split("\n"))
    lines = answer.split("\n")
    runningJobs = []
    waitingJobs = []
    for i in range (3, numberOfLines - 1 ):
        line = lines[i].split()
        if line[4] == 'r':
            runningJobs.append(line)
        else:
            waitingJobs.append(line)
    return render_template('polaris.html', runningJobs = runningJobs,
    waitingJobs = waitingJobs)
