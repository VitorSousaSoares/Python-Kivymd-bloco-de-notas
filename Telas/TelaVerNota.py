from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar

import json


class CodTelaVerNota(MDScreen):
    def delet(self, *args):
        atualizarText = self.ids.ConteudoDaNota.text

        with open('Json.json') as f:
            cadastro = json.load(f)

        cadastro[args[1]]["Conteudo"] = atualizarText

        add = json.dumps(cadastro, indent=1)

        with open("Json.json", "w") as f:
            f.write(add)

        self.manager.current = args[0]

    def atualizar(self, texto):
        with open('Json.json') as f:
            cadastro = json.load(f)
        self.ids.NomeNota.title = cadastro[texto]["Titulo"]
        self.ids.ConteudoDaNota.text = cadastro[texto]["Conteudo"]

        it = MDTopAppBar(
            title="VOLTAR",
            left_action_items=[
                ["arrow-left-bold", lambda x: self.delet("TelaTodasNotas", texto)]],
        )
        self.add_widget(it)
