import oerplib #https://github.com/osiell/oerplib/
import getpass

SERVER = 'localhost'
PORT = '8082'

input_server = raw_input("Server (leave empty for localhost): ")
if input_server != '':
	SERVER = input_server

input_port = raw_input("Port: (leave empty for 8069): ")
if input_port != '':
	PORT = input_port

oerp = oerplib.OERP(server=SERVER, port=PORT)

#chose database
databases = oerp.db.list()

if len(databases) == 1:
	DATABASE = databases[0]
else:
	#offer a selection of databases
	print("chose one of the following databases:")
	print(oerp.db.list())
	DATABASE = raw_input("Database: ")

print("Login:")
USERNAME = raw_input("Username: ")
PASSWORD = getpass.getpass()

user = oerp.login(USERNAME, PASSWORD, DATABASE)

print("Hello " + user.name)