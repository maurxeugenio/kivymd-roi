import kivy
from kivy.app import App
from kivymd.theming import ThemeManager


class RoiApp(App):
    theme_cls = ThemeManager()
    def calcular_roi(*args):
        lucro = args[1]
        custo = args[2]
        text = args[3]
        if not lucro == '' and not custo == '':
            lucro = int(lucro)
            custo = int(custo)
            res = str((lucro - custo) / custo)
            text.text = res
        else:
            text.text = 'Os campos devem ser preenchidos'
    def build(self):
        self.theme_cls.theme_style = 'Dark'
