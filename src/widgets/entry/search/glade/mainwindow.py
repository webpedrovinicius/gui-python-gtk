# -*- coding: utf-8 -*-
"""GTK SearchEntry, realizando pesquisas."""
import sqlite3

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class Handler:
    def __init__(self):
        self.con = sqlite3.connect('../../../data/db.sqlite3')
        self.cur = self.con.cursor()

        self.revealer = builder.get_object(name='revealer')

        self.liststore = builder.get_object(name='liststore')
        brazilian_states = self.get_brazilian_states()
        for state in brazilian_states:
            self.liststore.append(row=state)

    def show_hide_search(self, widget):
        show = self.revealer.get_reveal_child()
        if show:
            self.revealer.set_reveal_child(reveal_child=False)
        else:
            self.revealer.set_reveal_child(reveal_child=True)

    def on_search_changed(self, widget):
        # Pegando o texto do entry.
        entry_text = widget.get_text()
        if entry_text:
            # Buscando no banco.
            rows = self.search_state(state=entry_text)
            # Limpando os valores existentes no `Gtk.ListStore()`.
            self.liststore.clear()
            # Adicionando novos valores.
            for row in rows:
                self.liststore.append(row=row)
        else:
            # Caso o entry esteja vazio.
            self.liststore.clear()

    def get_brazilian_states(self):
        query = 'SELECT rowid, state FROM brazilian_states;'
        data = self.cur.execute(query)
        return data.fetchall()

    def search_state(self, state):
        query = 'SELECT rowid, state FROM brazilian_states WHERE state LIKE "%"||?||"%";'
        data = self.cur.execute(query, (state,))
        return data.fetchall()


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='mainwindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
