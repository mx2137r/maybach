import pymem
import pymem.process
import keyboard
from offsets.offsets import *


def noflash(pm, client):

    flashmanager = pm.read_int(client + dwLocalPlayer)

    if flashmanager:
        flash_value = flashmanager + m_flFlashMaxAlpha

        if flash_value:
            pm.write_float(flash_value, float(0))
    