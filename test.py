from qthvym import *

FILE_PATH = Path(__file__).parent 
IMG = os.path.join(FILE_PATH, 'img.png')

def splash():
    interaction = HVYMInteraction()
    interaction.splash("TEST!!")

def msg_popup():
      interaction = HVYMInteraction()
      interaction.msg_popup("TEST!!!")

def options_popup():
      interaction = HVYMInteraction()
      interaction.options_popup("TEST!!!!!", ['1', '2', '3'])
      
      return interaction

def user_popup():
      interaction = HVYMInteraction()
      interaction.user_popup("TEST")

      return interaction

def password_popup():
      interaction = HVYMInteraction()
      interaction.password_popup("TEST")

      return interaction

def user_password_popup():
      interaction = HVYMInteraction()
      interaction.user_password_popup("TEST", "defaultText")

      return interaction

def copy_line_popup():
      interaction = HVYMInteraction()
      interaction.copy_line_popup("TEST", "defaultText")

      return interaction

def copy_text_popup():
      interaction = HVYMInteraction()
      interaction.copy_text_popup("TEST", "defaultText")

      return interaction

def choice_popup():
      """ Show choice popup, message based on passed msg arg."""
      interaction = HVYMInteraction()
      interaction.choice_popup("TEST?")

      return interaction

def file_select_popup():
      interaction = HVYMInteraction()
      interaction.file_select_popup("TEST", ["Images (*.png *.svg)"])

      return interaction

def img_popup():
      interaction = HVYMInteraction()
      interaction.img_popup("TEST", IMG)

      return interaction

def qr_popup():
      interaction = HVYMInteraction()
      interaction.qr_popup("TEST", "dsfsdfsdfWEidjwqofhrqhddnialdjaidadnwquhdfuoihwudhahawudhauiodhawudhawudhauwhauiwdh")

      return interaction


#splash()
#msg_popup()
#print(options_popup().value)
#print(user_popup().value)
#print(password_popup().value)
#print(user_password_popup().value)
#print(copy_line_popup().value)
#print(copy_text_popup().value)
#print(choice_popup().value)
#print(file_select_popup().value)
#img_popup()
qr_popup()





    