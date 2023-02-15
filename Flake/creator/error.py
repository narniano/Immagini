
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

def throwError(self, error, title):
                 
        dialog = Gtk.MessageDialog(
                parent         = None,
                message_type   = Gtk.MessageType.ERROR,
                secondary_text = error,
                text           = title,
                buttons        = Gtk.ButtonsType.CLOSE,
        )

        dialog.set_transient_for(None)
        dialog.set_modal(True)
        dialog.show()
        
        dialog.connect("response", on_response, dialog)
        
def on_response(dialog: Gtk.Dialog, response: Gtk.ResponseType, _dialog: Gtk.Dialog) -> None:
        _dialog.destroy()
        
