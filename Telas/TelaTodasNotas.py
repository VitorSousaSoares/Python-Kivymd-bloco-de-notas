from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDList, IconRightWidget, TwoLineRightIconListItem
import json


class CodTelaTodasNotas(MDScreen):
    def delet(self, args):
        print(args)
        with open('Json.json') as f:
            cadastro = json.load(f)

        with open('Json.json') as f:
            cadastro = json.load(f)

        del cadastro[args]

        delet = json.dumps(cadastro, indent=1)

        with open("Json.json", "w") as f:
            f.write(delet)

        self.manager.current = "TelaAtualizar"
        self.manager.get_screen("TelaAtualizar").on_enter("TelaTodasNotas")

    def edit(self, args):
        self.manager.current = "TelaVerNota"
        self.manager.get_screen("TelaVerNota").atualizar(args)

    def on_enter(self):

        with open('Json.json') as f:
            cadastro = json.load(f)

        container = self.ids.container
        container.clear_widgets()

        self.list = MDList()
        for it in cadastro:
            i = cadastro[it]
            if i["Tipo"] == "Nota":
                item = TwoLineRightIconListItem(
                    bg_color=i["Cor"],
                    text=i["Titulo"],
                    on_press=lambda x, Tela=it: self.edit(Tela),
                )
                self.list.add_widget(item)
                item.add_widget(IconRightWidget(
                    icon="delete",
                    on_press=lambda x, Tela=it: self.delet(Tela),
                ))
        self.list.spacing = "10dp"
        container.add_widget(self.list)
