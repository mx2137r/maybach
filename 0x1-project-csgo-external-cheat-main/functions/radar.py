import pymem
import pymem.process
import keyboard
import time

from offsets.offsets import *


def radar(pm, client):

    for i in range(1, 32):
        entity = pm.read_int(client + dwEntityList + i * 0x10)
        if entity:
            pm.write_uchar(entity + m_bSpotted, 1)
