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
    runningJobs,waitingJobs = table(answer)
    return render_template('table.html',machine = "arc 1", runningJobs = runningJobs,
    waitingJobs = waitingJobs)

@main.route('/queues/arc2')
def arc2():

    connection = ssh("arc2.leeds.ac.uk", "uitjr", "Jaydee3148")
    answer = connection.sendCommand('qstat -u "*"')
    runningJobs,waitingJobs = table(answer)
    return render_template('table.html', machine = "arc 2", runningJobs = runningJobs,
    waitingJobs = waitingJobs)

@main.route('/queues/polaris')
def polaris():

    connection = ssh("polaris.leeds.ac.uk", "uitjr", "Jaydee3148")
    answer = connection.sendCommand('qstat -u "*"')
    runningJobs,waitingJobs = table(answer)
    return render_template('table.html', machine = "polaris", runningJobs = runningJobs,
    waitingJobs = waitingJobs)

@main.route('/modules')
def modules():

    connection = ssh("arc1.leeds.ac.uk", "uitjr", "Jaydee3148")
    answer = connection.sendCommand('module list')

    return(answer)
def table(answer):
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
    return (runningJobs,waitingJobs)
