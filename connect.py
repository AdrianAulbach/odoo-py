import oerplib

SERVER = 'localhost'
PORT = '8082'

input_server = raw_input("Server (leave empty for localhost):")
if input_server != '':
	SERVER = input_server

input_port = raw_input("Port: (leave empty for 8069):")
if input_port != '':
	PORT = input_port

oerp = oerplib.OERP(server=SERVER, port=PORT)

databases = oerp.db.list()

if len(databases) == 1:
	DATABASE = databases[0]
else:
	print("chose one of the following databases:")
	print(oerp.db.list())
	DATABASE = raw_input("Database:")