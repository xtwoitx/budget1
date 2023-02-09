from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class BudgetManagerApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, BudgetManager", halign="center")


BudgetManagerApp().run()