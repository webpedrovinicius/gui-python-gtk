# -*- coding: utf-8 -*-
"""Contêiner do tipo Stack Switcher Layout."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk

if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='./stack_switcher.glade')

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
