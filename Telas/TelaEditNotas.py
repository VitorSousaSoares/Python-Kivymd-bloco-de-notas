from kivymd.uix.screen import MDScreen


class CodTelaEditNotas(MDScreen):
    def atualizar(self, texto):
        self.ids.labEdi.text = texto
