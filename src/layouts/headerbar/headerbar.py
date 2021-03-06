# -*- coding: utf-8 -*-
"""Contêiner do tipo Headerbar Layout.

Este gerenciador de layout permite a inserção de widgets na barra de
titulo.
"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.set_title(title='Headerbar Layout')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')
        self.set_border_width(border_width=10)

        headerbar = Gtk.HeaderBar.new()
        # Definindo o título que será exibido na barra.
        # O titulo definido aqui sobrescreve o titulo da janela principal.
        headerbar.set_title(title='Contêiner')
        # Definindo um sub titulo para o HeaderBar.
        headerbar.set_subtitle(subtitle='HeaderBar Layout')
        # Torna visível os botões de minimizar, maximizar e fechar.
        # Por padrão essa opção é False.
        headerbar.set_show_close_button(setting=True)
        # Adicionando o HeaderBar na janela principal.
        self.set_titlebar(titlebar=headerbar)

        button_mail = Gtk.Button.new_from_icon_name(
            icon_name='mail-send-receive-symbolic',
            size=Gtk.IconSize.BUTTON
        )
        button_mail.connect('clicked', self._send_mail)
        headerbar.pack_end(child=button_mail)

        # Criando um Box Layout horizontal para conter os botões com seta.
        # Utilizando um Box Layout os botões ficam melhore distribuidos.
        hbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        # Adicionando o Box Layout no começo do HeaderBar.
        headerbar.pack_start(child=hbox)

        button_left_arrow = Gtk.Button.new_from_icon_name(
            icon_name='go-previous-symbolic',
            size=Gtk.IconSize.BUTTON
        )
        button_left_arrow.connect('clicked', self._left_arrow)
        hbox.add(widget=button_left_arrow)

        button_right_arrow = Gtk.Button.new_from_icon_name(
            icon_name='go-previous-symbolic-rtl',
            size=Gtk.IconSize.BUTTON
        )
        button_right_arrow.connect('clicked', self._right_arrow)
        hbox.add(widget=button_right_arrow)

        # Adicionando um widget do tipo TextView()
        # na janela principal (só para não ficar vazio).
        self.add(widget=Gtk.TextView.new())

    @staticmethod
    def _send_mail(widget):
        print('Você clicou no botão que tem o icone de enviar/receber email')

    @staticmethod
    def _left_arrow(widget):
        print('Você clicou no botão que tem uma seta para a esquerda')

    @staticmethod
    def _right_arrow(widget):
        print('Você clicou no botão que tem uma seta para a direita')


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
