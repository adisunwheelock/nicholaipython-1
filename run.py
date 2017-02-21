import os
PORT = int(os.getenv('PORT', 8000))
cmd = ['jupyter', 'jupyter', 'notebook', '--config=jupyter_notebook_config.py', '--port={}'.format(PORT)]
print("starting notebook server with command: '{}'".format(cmd))
os.execvp(cmd[0], cmd[1:])
