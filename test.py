from pathlib import Path
import os

from PyQt5.QtCore import QTimer
from qthvym import HVYMInteraction, HVYM_IMG, HVYM_LOGO_IMG
from qthvym.ui_helpers import center_on_screen


FILE_PATH = Path(__file__).parent
IMG = Path(HVYM_IMG).resolve()


def run_all_popups():
    interaction = HVYMInteraction()

    # Basic message dialogs
    interaction.msg_popup("Message dialog: long text should wrap properly.", icon=None)

    interaction.msg_popup("Icon message: long text should wrap properly.")

    # Choice dialogs
    interaction.choice_popup("Choice dialog: auto-closes in 5s.", icon=None)

    # interaction.choice_popup("Icon choice dialog: auto-closes in 5s.")

    # Options dialogs
    interaction.options_popup("Options dialog: select value.", ['1', '2', '3'], icon=None)

    interaction.options_popup("Icon options dialog: select value.", ['1', '2', '3'])

    # Text edit dialogs
    interaction.edit_line_popup("Line edit dialog:", "default text", icon=None)

    interaction.edit_line_popup("Icon line edit dialog:", "default text")

    interaction.copy_line_popup("Icon line copy dialog:", "default text")

    interaction.copy_text_popup("Icon copy text dialog:", "default text")

    # Password dialogs
    interaction.password_popup("Password dialog:")

    interaction.user_password_popup("User + Password dialog:", "user@example")

    # Media dialogs
    interaction.img_popup("Image dialog:", str(IMG))

    interaction.qr_popup("QR dialog:", "This is some test data")

    interaction.qr_copy_popup("QR copy dialog:", "This is some test data")

    interaction.custom_qr_popup(
        "Custom QR dialog:", 
        "This is some test data",
        cntrImg=HVYM_IMG,
        back_color=(152, 49, 74),
        front_color=(175, 232, 197)
    )


if __name__ == "__main__":
    run_all_popups()