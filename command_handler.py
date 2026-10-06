import subprocess

def run_command(user_input):
    return subprocess.run(user_input, shell=True)
