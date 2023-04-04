from kivymd.uix.screen import MDScreen


class CodTelaAtualizar(MDScreen):
    def on_enter(self, args):
        self.manager.current = args
