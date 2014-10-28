#!/usr/bin/env python

#import pygtk
#pygtk.require('3.10')
import gtk
import oerplib

class OdooGtk(object):
    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("odoo-gtk.ui")
        self.builder.connect_signals(self)

    def obj(self, name):
    	"""
        Gibt Glade-Object 'name' zur&uuml;ck
        """
        return self.builder.get_object(name)

    def run(self):
        """
	Startet die zentrale Warteschleife von Gtk
	"""
        try:
            gtk.main()
        except KeyboardInterrupt:
            pass
    
    def quit(self):
		gtk.main_quit()

###############################
## Signal-Behandlungsroutinen
###############################

#################
## Hauptfenster

    def on_window1_delete_event(self, *args):
        self.quit()
    
    def on_connect_btn_clicked(self, button, *args):
        server = self.builder.get_object('server_input').get_text()
        port = self.builder.get_object('port_input').get_text()
        print "connecting to " + server +":"+ port
        oerp = oerplib.OERP(server=server, port=port)
        print oerp.db.list()
        





if __name__ == '__main__':
    app = OdooGtk()
    app.run()
