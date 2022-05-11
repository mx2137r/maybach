import pymem
import pymem.process
import time
from offsets.offsets import *


def manager(pm, client, engine, enginePointer):
    if client and engine and pm:
        try:
            player = pm.read_int(client + dwLocalPlayer)
            engine_pointer = pm.read_int(engine + dwClientState)
            glow_manager = pm.read_int(client + dwGlowObjectManager) 
            crosshairID = pm.read_int(player + m_iCrosshairId) 
            getcrosshairTarget = pm.read_int(client + dwEntityList + (crosshairID - 1) * 0x10)
            immunitygunganme = pm.read_int(getcrosshairTarget + m_bGunGameImmunity)
            localTeam = pm.read_int(player + m_iTeamNum)
            crosshairTeam = pm.read_int(getcrosshairTarget + m_iTeamNum)
            flashmanager = pm.read_int(client + dwLocalPlayer)
            entity = pm.read_int(client + dwEntityList)
            player = pm.read_int(client + dwEntityList)
            iFOV = pm.read_int(player + m_iDefaultFOV)
        except:
            print("[maybach.wtf]: I hope u happy :)")
            time.sleep(1)
