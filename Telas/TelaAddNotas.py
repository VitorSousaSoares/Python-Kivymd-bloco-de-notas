import json
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarListItem


class Item(OneLineAvatarListItem):
    divider = None


class CodTelaAddNotas(MDScreen):
    def cr(self, obj):
        self.ids.toolbar.md_bg_color = obj
        self.dialog.dismiss()

    def show_alert_dialog(self):
        self.dialog = MDDialog(
            title="Selecione a cor da nota",
            type="simple",
            items=[
                Item(on_release=lambda x: self.cr(
                    "#FF8A80"), bg_color="#FF8A80"),
                Item(on_release=lambda x: self.cr(
                    "#1B5E20"), bg_color="#1B5E20"),
                Item(on_release=lambda x: self.cr(
                    "#FFC400"), bg_color="#FFC400"),
                Item(on_release=lambda x: self.cr(
                    "#E0E0E0"), bg_color="#E0E0E0"),
                Item(on_release=lambda x: self.cr(
                    "#212121"), bg_color="#212121"),
            ],
        )
        self.dialog.open()

    def adicionarNota(self):
        self.dialog = MDDialog(
            title="Obrigatorio",
            text="Adicione o titulo da nota",
            buttons=[MDFlatButton(
                text="OK", on_release=lambda x: self.dialog.dismiss()),],
        )

        if self.ids.TituloNota.text == "":
            self.dialog.open()
        else:
            data = {"Tipo": "Nota",
                    "Titulo": self.ids.TituloNota.text,
                    "Conteudo": self.ids.ConteudoDaNota.text,
                    "Cor": self.ids.toolbar.md_bg_color}
            self.ids.TituloNota.text = ""
            self.ids.ConteudoDaNota.text = ""
            self.ids.toolbar.md_bg_color = "#2196F3"

            with open('Json.json') as f:
                cadastro = json.load(f)

            if len(cadastro) == 0:
                ultimoCadastro = "0"
            else:
                for i in cadastro:
                    ultimoCadastro = i

            id = 1 + int(ultimoCadastro)

            cadastro[id] = data

            add = json.dumps(cadastro, indent=1)

            with open("Json.json", "w") as f:
                f.write(add)

            self.manager.current = "TelaTodasNotas"
