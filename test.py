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
      interaction.qr_popup("TEST", "This is some test data")

      return interaction

def qr_copy_popup():
      interaction = HVYMInteraction()
      interaction.qr_copy_popup("TEST", "This is some test data")

      return interaction

def custom_qr_popup():
      interaction = HVYMInteraction()
      interaction.custom_qr_popup("TEST", "This is some test data", 400, IMG, (249, 194, 10), (127, 36, 103))

      return interaction

def xro_qr_popup():
      interaction = HVYMInteraction()
      interaction.xro_qr_popup("Send Tokens Here:", "This is some test data")

      return interaction

def opus_qr_popup():
      interaction = HVYMInteraction()
      interaction.opus_qr_popup("Send Tokens Here:", "This is some test data")

      return interaction

def stellar_qr_popup():
      interaction = HVYMInteraction()
      interaction.stellar_qr_popup("Send Tokens Here:", "This is some test data")

      return interaction

def icp_qr_popup():
      interaction = HVYMInteraction()
      interaction.icp_qr_popup("Send Tokens Here:", "This is some test data")

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
#qr_popup()
#qr_copy_popup()
#custom_qr_popup()
#xro_qr_popup()
opus_qr_popup()
#stellar_qr_popup()





    