# -*- coding: utf-8 -*-
"""Dialogo para selecionar pastas."""
from os import listdir
from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.set_title(title='Dialogo para selecionar pastas')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../assets/icons/icon.png')
        self.set_border_width(border_width=10)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(widget=vbox)

        button_select_folder = Gtk.Button.new_with_label(label='Selecionar pasta')
        button_select_folder.connect("clicked", self.open_select_folder)
        vbox.add(widget=button_select_folder)

        button_select_folders = Gtk.Button.new_with_label(label='Selecionar pastas')
        button_select_folders.connect("clicked", self.open_select_folders)
        vbox.add(widget=button_select_folders)

    def open_select_folder(self, button):
        dialog = SelectFolder(parent=self)

        response = dialog.run()

        # Verificando a resposta recebida.
        if response == Gtk.ResponseType.OK:
            print('Botão ABRIR pressionado')
            print(f'Caminho até a pasta: {dialog.get_filename()}')
            print(f'URI até a pasta: {dialog.get_uri()}')

            folder = dialog.get_filename()

            print(f'Conteudo da pasta {folder}:\n {listdir(folder)}')

        dialog.destroy()

    def open_select_folders(self, button):
        dialog = SelectFolders(parent=self)

        response = dialog.run()

        # Verificando a resposta recebida.
        if response == Gtk.ResponseType.OK:
            print('Botão ABRIR pressionado')
            print(f'Caminho até a pasta: {dialog.get_filenames()}')
            print(f'URI até a pasta: {dialog.get_uris()}')

            folders = dialog.get_filenames()
            for folder in folders:
                print(f'Conteudo da pasta {folder}:\n {listdir(folder)}\n')

        dialog.destroy()


class SelectFolder(Gtk.FileChooserDialog):
    def __init__(self, parent):
        """Construtor.

        :param parent: Widget ao qual o dialogo pertence.
        """
        super().__init__(parent=parent)

        self.set_title(title='Selecionar Pasta')
        self.set_modal(modal=True)
        self.set_action(action=Gtk.FileChooserAction.SELECT_FOLDER)

        # Adicionando os botões que serão exibidos
        self.add_buttons(
            Gtk.STOCK_OPEN, Gtk.ResponseType.OK,
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL
        )

        # Definindo o diretório padrão.
        home = str(Path.home())
        self.set_current_folder(filename=home)

        # É obrigatório utilizar ``show_all()`` senão ``get_content_area()``
        # não adiciona os widgets.
        self.show_all()


class SelectFolders(Gtk.FileChooserDialog):
    def __init__(self, parent):
        """Construtor.

        :param parent: Widget ao qual o dialogo pertence.
        """
        super().__init__(parent=parent)

        self.set_title(title='Selecionar Pastas')
        self.set_modal(modal=True)
        self.set_action(action=Gtk.FileChooserAction.SELECT_FOLDER)

        self.add_buttons(
            Gtk.STOCK_OPEN, Gtk.ResponseType.OK,
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL
        )

        # Definindo a seleção múltipla.
        self.set_select_multiple(select_multiple=True)

        home = str(Path.home())
        self.set_current_folder(filename=home)

        # É obrigatório utilizar ``show_all()`` senão ``get_content_area()``
        # não adiciona os widgets.
        self.show_all()


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
