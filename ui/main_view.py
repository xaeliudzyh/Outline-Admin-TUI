# ui/main_view.py
#UNUSED
from textual.widgets import Static, Button, Footer
from textual.containers import Vertical

from ui.base_screen import BaseScreen
from ui.keys_view import KeysView
from ui.login_view import LoginView

class MainView(BaseScreen):
    def compose(self):
        yield Footer()
        yield Static("Main menu:")
        yield Vertical(
            Button("Manage Keys", name="show_keys"),
            Button("Close", name="exit")
        )



    def on_button_pressed(self, event):
        if event.button.name == "show_keys":
            self.app.push_screen(KeysView())
        #elif event.button.name == "sign_out":
        #    self.app.push_screen(LoginView())
        elif event.button.name == "exit":
            self.app.exit()
        '''
        elif event.button.name == "refresh":
            self.refresh_keys(mode="refresh")
        elif event.button.name == "add_key":
            from ui.add_key_view import AddKeyView
            self.app.push_screen(AddKeyView())
        elif event.button.name == "del_key":
            # Откроем KeysView с режимом удаления
            self.app.push_screen(KeysView(mode="delete"))
        elif event.button.name == "rename_key":
            self.app.push_screen(KeysView(mode="rename"))
        '''
