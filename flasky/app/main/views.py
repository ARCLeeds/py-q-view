from flask import render_template, g
from flask_login import current_user
from flask import flash, session
from . import main
from ..ssh import ssh
from ..models import User
from ..forms import PathForm

@main.before_request
def before_request():
    g.user = current_user


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

@main.route('/personal/queues')
def personal_queues():
    try:
        name = current_user.username
    except AttributeError:
        return render_template('empty.html', machine = "all Arc and Polaris Machines")

    connection = ssh("arc2.leeds.ac.uk", "uitjr", "Jaydee3148")
    answer = connection.sendCommand('qstat -u '+ name)

    if not answer :
        return render_template('empty.html', machine = "all Arc and Polaris Machines")

    runningJobs, waitingJobs = table(answer)

    return render_template('table.html', machine = "all Arc and Polaris Machines", runningJobs = runningJobs,
    waitingJobs = waitingJobs)

@main.route('/personal/queues/arc1')
def personal_arc1():
    try:
        name = current_user.username
    except AttributeError:
        return render_template('empty.html', machine = "Arc 1")

    connection = ssh("arc1.leeds.ac.uk", "uitjr", "Jaydee3148")
    answer = connection.sendCommand('qstat -u '+ name)

    if not answer :
        return render_template('empty.html', machine = "Arc1")

    runningJobs, waitingJobs = table(answer)

    return render_template('table.html', machine = "Arc1", runningJobs = runningJobs,
    waitingJobs = waitingJobs)


@main.route('/personal/queues/arc2')
def personal_arc2():
    try:
        name = current_user.username
    except AttributeError:
        return render_template('empty.html', machine = "Arc2")

    connection = ssh("arc2.leeds.ac.uk", "uitjr", "Jaydee3148")
    answer = connection.sendCommand('qstat -u '+ name)

    if not answer :
        return render_template('empty.html', machine = "Arc2")

    runningJobs, waitingJobs = table(answer)

    return render_template('table.html', machine = "Arc2", runningJobs = runningJobs,
    waitingJobs = waitingJobs)

@main.route('/personal/queues/polaris')
def personal_polaris():
    try:
        name = current_user.username
    except AttributeError:
        return render_template('empty.html', machine = "Polaris")

    connection = ssh("polaris.leeds.ac.uk", "uitjr", "Jaydee3148")
    answer = connection.sendCommand('qstat -u '+ name)

    if not answer :
        return render_template('empty.html', machine = "Polaris")

    runningJobs, waitingJobs = table(answer)

    return render_template('table.html', machine = "Polaris", runningJobs = runningJobs,
    waitingJobs = waitingJobs)


@main.route('/modules')
def modules():
    return render_template('modules.html')

@main.route('/bugs')
def bugs():
    return render_template('bugs.html')

@main.route('/info')
def info():
    return render_template('info.html')
@main.route('/fileviewer', methods=['GET', 'POST'])
def fileViewer ():
    form = PathForm()
    try:
        name = current_user.username
    except AttributeError:
        return render_template('empty.html', machine = "arc2")

    if not form.path.data :
        connection = ssh("arc2.leeds.ac.uk", "uitjr", "Jaydee3148")
        answer = connection.sendCommand('cd /nobackup/' + name + ' && ls -lh')

    else :
        path = form.path.data
        connection = ssh("arc2.leeds.ac.uk", "uitjr", "Jaydee3148")
        answer = connection.sendCommand('cd /nobackup/' + path +' && ls -lh ')


    if not answer :
        return render_template('empty.html', machine = "arc2")

    numberOfLines = len(answer.split("\n"))
    lines = answer.split("\n")
    header = lines[0]
    size = header [6:10]
    fileList = []
    for i in range (1, numberOfLines - 1 ):
        fileList.append(lines[i].split())

    return render_template('file.html',fileList = fileList, machine = "arc2", form = form)


def table(answer):
    numberOfLines = len(answer.split("\n"))
    lines = answer.split("\n")
    runningJobs = []
    waitingJobs = []
    for i in range (2, numberOfLines - 1 ):
        line = lines[i].split()
        if line[4] == 'r':
            runningJobs.append(line)
        else:
            waitingJobs.append(line)
    return (runningJobs,waitingJobs)
