import rpyc
from rpyc.utils.server import ThreadedServer
import subprocess
# this simulates the working of the console
def console_simulator(command):
    proc = subprocess.Popen(str(command), shell=True, stdout=subprocess.PIPE).stdout
    return proc.read() # arbitrary function

class MyService(rpyc.Service):
    def  exposed_line_counter(self,command): # command called line_counter with the prefix exposed
        return console_simulator(command)# upon call, the function returns result of command

t = ThreadedServer(MyService, port = 18861)
t.start()
