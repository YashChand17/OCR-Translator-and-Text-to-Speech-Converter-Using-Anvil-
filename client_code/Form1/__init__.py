from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def submit_img_click(self, **event_args):
    image_link = self.image_link.text
    language_text = self.lang_img.text
    image_text = anvil.server.call("detection",image_link,language_text)
    self.image_text.text = image_text
    

  def submit_translang_click(self, **event_args):
     trans_language = self.lang_dropdown.selected_value
     image_text = self.image_text.text 
     translated_text = anvil.server.call("translator_fn",trans_language,image_text)
     self.translated_text.text = translated_text

  def download_audio_click(self, **event_args):
    tts = anvil.server.call("speak",self.translated_text.text,self.lang_dropdown.selected_value)
    anvil.media.download(tts)

  def image_link_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass







