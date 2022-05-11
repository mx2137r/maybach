import pymem
import pymem.process
import time
import keyboard

from offsets.offsets import *


def foved(pm, client):

	player = pm.read_int(client + dwEntityList)
	iFOV = pm.read_int(player + m_iDefaultFOV)

	if keyboard.is_pressed("/"):
			pm.write_int(player + m_iDefaultFOV, 0)
	if keyboard.is_pressed("-"):
			pm.write_int(player + m_iDefaultFOV, 90)
	if keyboard.is_pressed("+"):
			pm.write_int(player + m_iDefaultFOV, 120)