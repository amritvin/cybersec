from subprocess import call
import shlex
#call(shlex.split('bash run .sh'))
#call(['bash', 'run.sh'])
call(["gdb","./bof","set disassembly-flavour","intel"])
