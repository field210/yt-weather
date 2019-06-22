import subprocess


def run_command(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    return


filepath = '.env'

with open(filepath) as fp:
    for line in fp:
        command = 'heroku config:set '+line
        run_command(command)
