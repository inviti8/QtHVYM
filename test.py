from pathlib import Path
import os

from PyQt5.QtCore import QTimer
from qthvym import (
    MsgDialog,
    IconMsgBox,
    ChoiceDialog,
    IconChoiceMsgBox,
    OptionsDialog,
    IconOptionsMsgBox,
    TextEditDialog,
    IconEditTextMsgBox,
    IconCopyTextMsgBox,
    LineEditDialog,
    IconLineEditMsgBox,
    IconLineCopyMsgBox,
    ImageMsgBox,
    QrMsgBox,
    QrCopyMsgBox,
    CustomQrMsgBox,
    IconPasswordTextMsgBox,
    IconUserPasswordTextMsgBox,
    HVYM_IMG,
    HVYM_LOGO_IMG,
)
from qthvym.ui_helpers import center_on_screen


FILE_PATH = Path(__file__).parent
IMG = Path(HVYM_IMG).resolve()


def show_for_5s(dialog):
    center_on_screen(dialog)
    QTimer.singleShot(5000, dialog.accept)
    dialog.exec()


def run_all_popups():
    # Basic message dialogs
    show_for_5s(MsgDialog("Message dialog: long text should wrap properly."))
    show_for_5s(IconMsgBox("Icon message: long text should wrap properly.", icon=str(HVYM_LOGO_IMG)))

    # Choice dialogs
    show_for_5s(ChoiceDialog("Choice dialog: auto-closes in 5s."))
    show_for_5s(IconChoiceMsgBox("Icon choice dialog: auto-closes in 5s.", icon=str(HVYM_LOGO_IMG)))

    # Options dialogs
    show_for_5s(OptionsDialog("Options dialog: select value.", ['1', '2', '3']))
    show_for_5s(IconOptionsMsgBox("Icon options dialog: select value.", ['1', '2', '3'], icon=str(HVYM_LOGO_IMG)))

    # Text edit dialogs
    show_for_5s(TextEditDialog("Text edit dialog:", defaultTxt="default text"))
    show_for_5s(IconEditTextMsgBox("Icon text edit dialog:", defaultTxt="default text", icon=str(HVYM_LOGO_IMG)))
    show_for_5s(IconCopyTextMsgBox("Icon copy text dialog:", defaultTxt="default text", icon=str(HVYM_LOGO_IMG)))

    # Line edit dialogs
    show_for_5s(LineEditDialog("Line edit dialog:", defaultTxt="default text"))
    show_for_5s(IconLineEditMsgBox("Icon line edit dialog:", defaultTxt="default text", icon=str(HVYM_LOGO_IMG)))
    show_for_5s(IconLineCopyMsgBox("Icon line copy dialog:", defaultTxt="default text", icon=str(HVYM_LOGO_IMG)))

    # Password dialogs
    show_for_5s(IconPasswordTextMsgBox("Password dialog:", icon=str(HVYM_LOGO_IMG)))
    show_for_5s(IconUserPasswordTextMsgBox("User + Password dialog:", defaultTxt="user@example", icon=str(HVYM_LOGO_IMG)))

    # Media dialogs
    show_for_5s(ImageMsgBox("Image dialog:", str(IMG), width=400, icon=str(HVYM_LOGO_IMG)))
    show_for_5s(QrMsgBox("QR dialog:", data="This is some test data", width=400, icon=str(HVYM_LOGO_IMG)))
    show_for_5s(QrCopyMsgBox("QR copy dialog:", data="This is some test data", width=400, icon=str(HVYM_LOGO_IMG)))
    show_for_5s(CustomQrMsgBox("Custom QR dialog:", data="This is some test data", width=400, cntrImg=HVYM_IMG, back_color=(152,49,74), front_color=(175,232,197), icon=str(HVYM_LOGO_IMG)))


if __name__ == "__main__":
    run_all_popups()