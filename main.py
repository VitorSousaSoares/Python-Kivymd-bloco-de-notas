import json
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import DictProperty

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

from Telas.TelaInicial import CodTelaInicial
from Telas.TelaDeNotasVazia import CodTelaDeNotasVazia
from Telas.TelaAddNotas import CodTelaAddNotas
from Telas.TelaDeInfo import CodTelaDeInfo
from Telas.TelaTodasNotas import CodTelaTodasNotas
from Telas.TelaVerNota import CodTelaVerNota
from Telas.TelaAtualizar import CodTelaAtualizar
from Telas.ItemConfirm import CodItemConfirm

Builder.load_file('main.kv')


class MainApp(MDApp):
    Window.size = (300, 600)
    data = DictProperty()

    def build(self):
        self.sm = MDScreenManager()
        self.sm.add_widget(CodTelaInicial(name="TelaInicial"))
        self.sm.add_widget(CodTelaDeNotasVazia(name="TelaDeListaVazia"))
        self.sm.add_widget(CodTelaAddNotas(name="TelaAddNotas"))
        self.sm.add_widget(CodTelaDeInfo(name="TelaDeInfo"))
        self.sm.add_widget(CodTelaTodasNotas(name="TelaTodasNotas"))
        self.sm.add_widget(CodTelaVerNota(name="TelaVerNota"))
        self.sm.add_widget(CodTelaAtualizar(name="TelaAtualizar"))
        self.sm.add_widget(CodItemConfirm(name="ItemConfirm"))
        self.data = {
            'Notas': [
                'note-text',
                "on_release", lambda x: self.callback("Notas")
            ],
            'Informações': [
                'list-box',
                "on_release", lambda x: self.callback("Informações")
            ],
        }

        return self.sm

    def callback(self, args):
        with open('Json.json') as f:
            cadastro = json.load(f)
        if args == "Notas":

            if len(cadastro) != 0:
                self.sm.current = "TelaTodasNotas"
            else:
                self.sm.current = "TelaDeListaVazia"
        else:
            self.sm.current = "TelaDeInfo"

    def voltar(self, v):
        self.sm.current = v

    def voltarEsalvarNota(self, *args):
        self.sm.current = args[0]
        print(args[1])

    def info(self, v):
        self.sm.current = v


MainApp().run()
